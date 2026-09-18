"""
ACC - Algoritmo de Correlacion de Conclusiones.

El nucleo del bucle de retroalimentacion. Cada ciclo despliega 3 agentes que
devuelven, ademas de su analisis, un vector de posicion en 6 ejes. Este modulo
convierte esas 3 posiciones en:

  1. un centroide (la conclusion del ciclo),
  2. una coherencia kappa (cuanto coinciden),
  3. un eje de maxima divergencia (la grieta),
  4. una decision de control para el ciclo siguiente.

El punto 4 es lo que hace que esto sea un bucle y no una lista: la grieta
del ciclo n es la pregunta del ciclo n+1, y si la coherencia sube demasiado
rapido el motor inyecta un agente adversarial para romper el pensamiento
de grupo. Sin eso, 10 ciclos de 3 agentes convergen a un eco.

Ejes (todos en [0,1]):
  A  aleatorio (0) <-> epistemico (1)   : naturaleza de la incertidumbre dominante
  E  no estacionario (0) <-> estacionario (1)
  F  infalsificable (0) <-> falsable hoy (1)
  P  libre de modelo (0) <-> parametrico (1)
  H  invariante al horizonte (0) <-> crece con el horizonte (1)
  O  teorico puro (0) <-> implementable ya (1)
"""

from __future__ import annotations

import json
import math
import sys
from itertools import combinations

EJES = ["A", "E", "F", "P", "H", "O"]
DIAG = math.sqrt(len(EJES))          # distancia maxima en el hipercubo [0,1]^6

# Umbrales del controlador. KAPPA_ECO no es arbitrario: con 3 agentes en [0,1]^6,
# kappa > 0.92 significa distancia media < 0.20 en el hipercubo, es decir que los
# tres estan diciendo lo mismo con distinto vocabulario.
KAPPA_ECO = 0.92        # por encima: riesgo de pensamiento de grupo
KAPPA_CAOS = 0.55       # por debajo: los agentes no hablan del mismo problema


def _dist(u: list[float], v: list[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def _pearson(u: list[float], v: list[float]) -> float:
    """Correlacion de forma: si dos agentes discrepan en NIVEL pero coinciden en
    QUE eje importa mas, esto lo detecta y la distancia euclidea no."""
    n = len(u)
    mu, mv = sum(u) / n, sum(v) / n
    du = [a - mu for a in u]
    dv = [b - mv for b in v]
    num = sum(a * b for a, b in zip(du, dv))
    den = math.sqrt(sum(a * a for a in du) * sum(b * b for b in dv))
    return num / den if den > 1e-12 else 0.0


def centroide(vs: list[list[float]], pesos: list[float] | None = None) -> list[float]:
    w = pesos or [1.0] * len(vs)
    tot = sum(w)
    return [sum(v[k] * wi for v, wi in zip(vs, w)) / tot for k in range(len(EJES))]


def coherencia(vs: list[list[float]]) -> float:
    """kappa en [0,1]: 1 = los agentes ocupan el mismo punto, 0 = esquinas opuestas."""
    pares = list(combinations(vs, 2))
    d = sum(_dist(u, v) for u, v in pares) / len(pares)
    return 1.0 - d / DIAG


def coherencia_forma(vs: list[list[float]]) -> float:
    """Media de las correlaciones de Pearson por pares. Distingue 'discrepan en
    todo' de 'discrepan en cuanto, coinciden en que'."""
    pares = list(combinations(vs, 2))
    return sum(_pearson(u, v) for u, v in pares) / len(pares)


def divergencia(vs: list[list[float]]) -> dict[str, float]:
    """Desviacion tipica poblacional por eje. El argmax es la grieta del ciclo."""
    n = len(vs)
    out = {}
    for k, eje in enumerate(EJES):
        col = [v[k] for v in vs]
        m = sum(col) / n
        out[eje] = math.sqrt(sum((x - m) ** 2 for x in col) / n)
    return out


def consenso_claims(claims_por_agente: list[list[dict]], umbral: float = 0.70) -> dict:
    """Particiona los claims en tres cubos segun su etiqueta de ancla semantica.

    Cada claim lleva un campo 'ancla': un identificador corto del concepto que
    afirma. Dos agentes que llegan al mismo concepto por caminos distintos usan
    la misma ancla, y eso es exactamente la senal que buscamos: convergencia
    independiente. Un claim con ancla unica es una aportacion no corroborada;
    dos anclas iguales con confianzas opuestas son una contradiccion explicita.
    """
    reg: dict[str, list[dict]] = {}
    for i, claims in enumerate(claims_por_agente):
        for c in claims:
            c = dict(c, agente=i)
            reg.setdefault(c["ancla"], []).append(c)

    convergente, unico, contradictorio = [], [], []
    for ancla, grupo in reg.items():
        confs = [c["conf"] for c in grupo]
        if len(grupo) == 1:
            unico.append((ancla, grupo))
        elif max(confs) - min(confs) > 0.40:
            contradictorio.append((ancla, grupo))
        elif sum(confs) / len(confs) >= umbral:
            convergente.append((ancla, grupo))
        else:
            unico.append((ancla, grupo))

    # Confianza agregada de un claim convergente. NO es el promedio: dos agentes
    # que llegan al mismo sitio por rutas independientes se refuerzan, asi que se
    # combinan las probabilidades de fallo (1-conf) como si fueran independientes,
    # y se penaliza con un factor por la correlacion residual entre agentes que
    # comparten el mismo modelo base. rho=0.5 es deliberadamente conservador.
    def agregada(grupo, rho=0.5):
        fallo = 1.0
        for c in grupo:
            fallo *= (1.0 - c["conf"])
        indep = 1.0 - fallo
        prom = sum(c["conf"] for c in grupo) / len(grupo)
        return rho * prom + (1 - rho) * indep

    return {
        "convergente": [(a, round(agregada(g), 3), [c["agente"] for c in g])
                        for a, g in convergente],
        "unico": [(a, g[0]["conf"], g[0]["agente"]) for a, g in unico],
        "contradictorio": [(a, [(c["agente"], c["conf"]) for c in g])
                           for a, g in contradictorio],
    }


def controlador(kappa: float, kappa_prev: float | None, div: dict[str, float]) -> dict:
    """Decide la composicion del ciclo siguiente. Esta es la retroalimentacion.

    - Si kappa es muy alto y ya venia subiendo, los agentes se estan haciendo eco:
      el ciclo siguiente incluye un agente cuyo unico trabajo es romper la tesis.
    - Si kappa es muy bajo, los agentes ni siquiera comparten el problema:
      el ciclo siguiente se estrecha a una sola pregunta.
    - En medio, se ataca la grieta: el eje de maxima divergencia manda.
    """
    grieta = max(div, key=div.get)
    delta = None if kappa_prev is None else kappa - kappa_prev

    if kappa > KAPPA_ECO and (delta is None or delta >= -0.02):
        modo, razon = "ADVERSARIAL", f"kappa={kappa:.2f} > {KAPPA_ECO}: consenso sospechoso, forzar refutacion"
    elif kappa < KAPPA_CAOS:
        modo, razon = "CONVERGENTE", f"kappa={kappa:.2f} < {KAPPA_CAOS}: los agentes no comparten problema, estrechar"
    else:
        modo, razon = "GRIETA", f"atacar eje {grieta} (sigma={div[grieta]:.2f})"

    return {"modo": modo, "grieta": grieta, "delta_kappa": delta, "razon": razon}


def ciclo(vectores: dict[str, list[float]], claims=None, kappa_prev=None) -> dict:
    vs = list(vectores.values())
    c = centroide(vs)
    k = coherencia(vs)
    kf = coherencia_forma(vs)
    d = divergencia(vs)
    out = {
        "agentes": list(vectores.keys()),
        "centroide": {e: round(x, 3) for e, x in zip(EJES, c)},
        "kappa": round(k, 4),
        "kappa_forma": round(kf, 4),
        "divergencia": {e: round(x, 3) for e, x in d.items()},
        "control": controlador(k, kappa_prev, d),
    }
    if claims:
        out["claims"] = consenso_claims(claims)
    return out


def linea_mem(n: int, res: dict, nodos: str, sintesis: str, q: str) -> str:
    """Serializa el ciclo a UNA linea del ledger comprimido. Este formato es el
    que permite recargar 10 ciclos de investigacion en ~1.5k tokens."""
    c = res["centroide"]
    vec = ",".join(f"{c[e]:.2f}".lstrip("0") for e in EJES)
    g = res["control"]["grieta"]
    return (f"C{n:02d}|k{res['kappa']:.2f}|c[{vec}]|D={g}{res['divergencia'][g]:.2f}"
            f"|{res['control']['modo'][:3]}|N:{nodos}|>{sintesis}|q:{q}")


if __name__ == "__main__":
    datos = json.load(open(sys.argv[1]))
    res = ciclo(datos["vectores"], datos.get("claims"), datos.get("kappa_prev"))
    print(json.dumps(res, indent=2, ensure_ascii=False))
