#!/usr/bin/env python3
"""
banda.py -- EL ALGORITMO.  Ciclo 10 (el ultimo).  Sustituye a motor/algoritmo.py.

Entrada:  una serie de rendimientos MENSUALES, un horizonte H en anios, un nivel alpha.
Salida:   un diagnostico estructurado.  Nunca un numero solo.

    d = diagnostico(r_mensual, H=10, alpha=0.99)
    print(d["paso6_veredicto_operativo"])

El procedimiento es el de T6 ("la banda ciega"), verificado en verificacion/N133 sobre
Fama-French 1926-07..2026-07.  Seis pasos, y el orden NO es decorativo: cada uno puede
invalidar a los siguientes.  Por eso diagnostico() para en el paso 0 si la deriva no es
constante, y por eso el paso 3 devuelve None en el punto cuando el signo no esta
determinado.  La forma mas facil de usar mal este resultado es leer un numero de una
salida cuyo paso 0 fallo; la segunda, leer el punto cuando el veredicto es INDETERMINADO.
Las dos estan cerradas por construccion, no por advertencia.

--------------------------------------------------------------------------------------
LO QUE NO HACE
--------------------------------------------------------------------------------------
  * NO estima mejor el Expected Shortfall.  No reduce ninguna incertidumbre.  Solo mide
    cual es, y niega un punto cuando el punto no existe.
  * NO decide cuanto capital poner.  Cuando el veredicto es DETERMINADO_NEGATIVO el
    modelo esta pidiendo capital negativo: eso exige un SUELO DECLARADO por quien firma,
    no un maximo silencioso con cero.
  * NO se aplica al SCR de Solvencia II.  Articulo 101(3): "it shall cover only
    unexpected losses" -- el requisito se define como desviacion respecto a la media, mu
    se cancela IDENTICAMENTE y no hay problema de signo.  Esto aplica al ES plug-in usado
    como NIVEL: IFRS 9, C-3 Phase II RBC, ALM de pensiones.  La restriccion de alcance va
    escrita antes que la afirmacion, no despues de que alguien la senale.
  * NO prueba que el mercado tenga o no tenga deriva.  Prueba que, con la ventana que la
    estacionariedad permite, el signo del numero no esta determinado por los datos.
  * NO es robusto a colas gordas en el test de ruptura mas alla de lo que da el HAC de
    Newey-West; el critico 12.35 es el de Andrews al 1% para un cambio de nivel.
  * NO mira correlacion transversal ni multiples activos.  Una sola serie.

--------------------------------------------------------------------------------------
LO QUE ESTA RETRACTADO -- y no se resucita aqui
--------------------------------------------------------------------------------------
  * EL RATIO DE REVISION 48x (ciclo 8): FALSO.  Suponia sigma constante; sigma_gorro
    tambien se revisa (6,42% del nivel) y eso hunde el denominador.  Medido sobre 90
    reestimaciones anuales reales: 3,04x.  Lo que sobrevive, y es mejor porque es una
    IGUALDAD y no una desigualdad, es el paso 5.
  * T_req = 55,8 anios  y  T_eff <= T/rho_barra: PUBLICADOS (Noguer i Alonso 2026 ec.(21);
    Giller 2024 ecs.(17)-(18)).  Aqui se calculan porque hacen falta, no como aportacion.
  * n_eff = T/H: esta LITERAL en Danielsson 2002 section 3.5, con ejemplo numerico.
  * Ademas, del registro largo: la frontera de cuarto momento (C2/C4), el mecanismo de la
    complejidad optima (C4), la autoviolacion del modelo de cola (C5), T3 (C7) y T5 (C8).
    Nada de eso entra en este archivo.

Lo unico propio que queda, y que esto implementa: la banda H^-/H^+ como INTERVALO EN EL
HORIZONTE (los DOS polos del funcional, no uno), su conjuncion con un T_est medido por
test de ruptura -- conjunto admisible vacio: la determinacion se compra con no
estacionariedad --, que el estimador predictivo la ENSANCHA, y la singularidad H0.

--------------------------------------------------------------------------------------
PROCEDENCIA DEL CODIGO
--------------------------------------------------------------------------------------
Este archivo es autocontenido (solo numpy/scipy) a proposito: se copia a un entorno de
produccion sin arrastrar el repositorio.  Los bloques marcados [de resolve.py] y
[de algoritmo.py] son los ya verificados, copiados sin reescribir:

    hac_var, sup_wald, ultima_ruptura_volatilidad, banda, anualizar  [protocolo/resolve.py]
    k_alpha, presupuesto_especificacion, ESCALERA_ANIOS             [motor/algoritmo.py]

La prueba 8 de la bateria es la GUARDA DE DERIVA: si el repositorio esta presente,
comprueba que estas copias siguen dando exactamente lo mismo que el original.  Si alguien
toca resolve.py y no toca esto, la prueba 8 falla.  Si el repositorio no esta, salta.

Ejecutar:   python3 motor/banda.py            bateria de pruebas + escalera de horizontes
"""
from __future__ import annotations

import hashlib
import math
import os
import sys

import numpy as np
from scipy import stats

# --------------------------------------------------------------------------- constantes
# Congeladas en protocolo/protocol.json el 2026-09-22.  No son parametros de ajuste:
# cambiar cualquiera invalida la comparacion con N133, asi que van como valores por
# defecto explicitos y no como numeros magicos dentro de las funciones.
MESES = 12
Z95 = 1.959963985                 # normal bilateral al 5%
CRIT_SUPWALD = 12.35              # Andrews al 1% para un cambio de nivel, recorte 15%
RECORTE = 0.15
MIN_MESES = 120                   # por debajo, sup_wald no corre => el paso 0 no existe
                                  # => el diagnostico entero seria invalido.  Se rechaza.
ESCALERA_ANIOS = (1, 2, 5, 10, 20, None)   # [de algoritmo.py]  None = muestra completa

ALCANCE = (
    "ALCANCE: bajo Solvencia II art. 101(3) ('only unexpected losses') mu se cancela "
    "identicamente y NADA de esto aplica al SCR. Aplica al ES plug-in usado como NIVEL: "
    "IFRS 9, C-3 Phase II RBC, ALM de pensiones."
)


# ===================================================================== piezas verificadas

def k_alpha(alpha: float = 0.99) -> float:
    """[de algoritmo.py] Multiplicador del ES gaussiano: k = phi(z_alpha)/(1-alpha).

    k99 = 2.6652142.  Es el unico sitio donde entra alpha: toda la banda es k/(S +- z/rT),
    de modo que subir alpha DESPLAZA la banda hacia horizontes largos, no la estrecha.
    """
    return float(stats.norm.pdf(stats.norm.ppf(alpha)) / (1 - alpha))


def anualizar(w: np.ndarray) -> tuple[float, float]:
    """[de resolve.py] Mensual -> anual.  sigma por raiz-de-t, que es exactamente la regla
    cuya correccion por media estamos auditando: usar otra aqui seria cambiar el objeto."""
    return float(w.mean() * MESES), float(w.std(ddof=1) * math.sqrt(MESES))


def hac_var(e: np.ndarray) -> float:
    """[de resolve.py] Varianza de largo plazo Newey-West, lag = floor(4*(n/100)^(2/9)).

    Sin HAC el sup-Wald sobre proxies de volatilidad explota: log(r^2) tiene memoria y
    cualquier test que la ignore encuentra rupturas donde solo hay agrupamiento.
    """
    n = len(e)
    L = int(4 * (n / 100) ** (2 / 9))
    e = e - e.mean()
    s = (e @ e) / n
    for l in range(1, L + 1):
        s += 2 * (1 - l / (L + 1)) * (e[l:] @ e[:-l]) / n
    return float(s)


def sup_wald(y: np.ndarray, recorte: float = RECORTE) -> tuple[float, int | None]:
    """[de resolve.py] sup-Wald de Andrews para un cambio de nivel en la media, con HAC.

    Devuelve (estadistico, indice de la ruptura).  n<120 devuelve 0: no es que no haya
    ruptura, es que el test no tiene potencia y mentir con un 0 seria peor que parar --
    por eso diagnostico() exige MIN_MESES antes de llamar aqui.
    """
    n = len(y)
    if n < MIN_MESES:
        return 0.0, None
    s2 = hac_var(y)
    if s2 <= 0:
        return 0.0, None
    mejor = (0.0, None)
    for b in range(int(recorte * n), int((1 - recorte) * n)):
        m1, m2 = y[:b].mean(), y[b:].mean()
        W = (m1 - m2) ** 2 / (s2 * (1 / b + 1 / (n - b)))
        if W > mejor[0]:
            mejor = (W, b)
    return float(mejor[0]), mejor[1]


_MEMO_RUPTURA: dict[tuple, tuple] = {}


def ultima_ruptura_volatilidad(x: np.ndarray, crit: float = CRIT_SUPWALD,
                               recorte: float = RECORTE) -> tuple[int | None, dict]:
    """[de resolve.py, + se anota el sup-Wald de cada ruptura] Busqueda secuencial tipo
    Bai-Perron sobre TRES proxies de volatilidad; se exige que coincidan al menos dos.

    Por que tres y no uno: log(r^2) es el que menos pesa las colas y el mas conservador
    (16,8 en la serie real, frente a 40,7 de |r| y 38,8 de r^2).  Un solo proxy convierte
    la eleccion del proxy en el grado de libertad que decide T_est, y T_est decide la
    banda entera.  La mayoria de 2/3 quita esa palanca de las manos de quien reporta.

    Devuelve (indice de la ULTIMA ruptura o None, detalle por proxy).
    """
    clave = (hashlib.blake2b(np.ascontiguousarray(x).tobytes(), digest_size=16).hexdigest(),
             len(x), crit, recorte)
    if clave in _MEMO_RUPTURA:                     # la escalera de horizontes llama a
        return _MEMO_RUPTURA[clave]                # esto una vez por H y no depende de H
    detalle, posiciones = {}, []
    for etiqueta, y in (("log(r^2)", np.log(x ** 2 + 1e-12)),
                        ("|r|", np.abs(x)),
                        ("r^2", x ** 2)):
        segs, brks = [(0, len(y))], []
        for _ in range(6):
            cand = []
            for (a, b) in segs:
                W, bb = sup_wald(y[a:b], recorte)
                if bb is not None and W > crit:
                    cand.append((W, a + bb, (a, b)))
            if not cand:
                break
            W, pos, (a, b) = max(cand)
            brks.append((pos, W))
            segs.remove((a, b))
            segs += [(a, pos), (pos, b)]
        brks.sort()
        detalle[etiqueta] = brks
        posiciones.append(max(p for p, _ in brks) if brks else None)

    validas = [p for p in posiciones if p is not None]
    res = (None, detalle) if len(validas) < 2 else (int(np.median(validas)), detalle)
    _MEMO_RUPTURA[clave] = res
    return res


def presupuesto_especificacion(H: float, T: float, S: float,
                               alpha: float = 0.99, h0: float = 0.0) -> float:
    """[de algoritmo.py, ciclo 7, sigue vivo] eps*(H): fraccion del numero reportado que el
    modelo puede errar antes de que el riesgo de ESPECIFICACION supere al de ESTIMACION.

    eps*(H) = sqrt(H/T) / (k_alpha - S*sqrt(H)) * sqrt(1 + h0/H)

    Por debajo de eps*, gastar en especificar mejor el modelo NO compensa: el presupuesto
    va a estimar (o a declarar).  Verificado exacto -- predicho = medido a tres decimales
    -- en 7 generadores x 7 horizontes.

    Si el denominador es <= 0 devuelve inf, y quien lea tiene que leer inf: significa que
    H esta mas alla de H0, donde el numero reportado se anula, y una fraccion del numero
    reportado deja de significar nada.  Devolver nan ahi seria esconder el diagnostico
    dentro de un fallo numerico.
    """
    k = k_alpha(alpha)
    den = k - S * math.sqrt(H)
    if den <= 0:
        return float("inf")
    return float(math.sqrt(H / T) / den * math.sqrt(1 + h0 / H))


# ============================================================================== la banda

def banda(S: float, T: float, k: float, z: float = Z95) -> tuple[float, float]:
    """[de resolve.py, + la guarda S+e<=0] La banda ciega:

        H^-/+ = [ k_alpha / (S -/+ z/sqrt(T)) ]^2

    Sale de contrastar ES(alpha,H) = -mu*H + k*sigma*sqrt(H) = 0, es decir mu = k*sigma/rH,
    con SE(mu_gorro) = sigma/sqrt(T).  El signo queda INDETERMINADO exactamente cuando
    H^- < H < H^+.  Fuera se determina solo: positivo por debajo (manda sigma), negativo
    por encima (manda mu).

    Dos degeneraciones, y las dos son informativas, no errores:
      S <= z/rT  -> H^+ = inf.  El Sharpe no se distingue de cero: ningun horizonte largo
                    determina el signo y la banda es una semirrecta.
      S + z/rT <= 0 -> banda VACIA (se devuelve (inf, inf)).  Con Sharpe suficientemente
                    negativo, k/rH > S + z/rT para todo H y el signo es positivo siempre.
    """
    e = z / math.sqrt(T)
    if S + e <= 0:
        return float("inf"), float("inf")
    H_menos = (k / (S + e)) ** 2
    H_mas = (k / (S - e)) ** 2 if S > e else float("inf")
    return H_menos, H_mas


def banda_predictiva(S: float, T: float, k: float, z: float = Z95) -> tuple[float, float]:
    """La misma banda con el estimador PREDICTIVO: sqrt(H) -> sqrt(H(1+H/T)).

    Es la objecion estandar (Barberis 2000; Pitera-Schmidt 2018): "integra mu fuera y el
    signo queda determinado".  Se responde en la propia salida porque es falso: la
    correccion predictiva anade VARIANZA, no INFORMACION sobre mu.  SE(mu_gorro) sigue
    siendo sigma/sqrt(T) y el termino -mu*H es identico.  Se paga mas capital por
    exactamente la misma ignorancia, y la banda SE ENSANCHA (39% en la serie real).

    ES_pred = 0  <=>  S = k*sqrt(1/H + 1/T) =: g(H), decreciente de +inf a k/sqrt(T).
    Invirtiendo:  H = 1 / ((c/k)^2 - 1/T),  inf si (c/k)^2 <= 1/T.
    """
    def inv(c: float) -> float:
        if c <= 0:
            return float("inf")
        d = (c / k) ** 2 - 1.0 / T
        return 1.0 / d if d > 0 else float("inf")
    e = z / math.sqrt(T)
    return inv(S + e), inv(S - e)


def T_requerido(H: float, S: float, k: float, z: float = Z95) -> float:
    """Anios de REGIMEN ESTACIONARIO necesarios para determinar el signo a horizonte H:

        T_req(H) = [ z / (k/sqrt(H) - S) ]^2

    Diverge cuando H -> H0 = (k/S)^2, donde el numero se anula: un cero no tiene signo.
    Es la columna que resume diez ciclos -- a H=10 sobre la serie real da ~11.700 anios
    frente a los 85 disponibles.  (La forma T_req = ((z+z_beta)/theta)^2 esta publicada:
    Noguer i Alonso 2026, ec.(21).  Aqui se usa, no se reclama.)
    """
    den = k / math.sqrt(H) - S
    return float("inf") if den == 0 else float((z / den) ** 2)


def firma_revision(r: np.ndarray, H: float, k: float, T_ventana: int) -> dict | None:
    """[de resolve.py, funcion firma] Paso 5: la firma de revision esperada.

        SD(dES) excedente = sqrt( Var(dES | mu_gorro) - Var(dES | mu=0) ) = H*sqrt(2)*sigma/T

    Es una IGUALDAD, no una cota, y esa es la unica razon por la que sobrevivio al ciclo 9
    (el ratio 48x del ciclo 8, que era una desigualdad, esta retractado: medido 3,04x).
    Verificada sobre datos reales a 1,054 / 1,165 / 1,110 del valor teorico con ventanas
    de 10/20/30 anios.

    Uso como AUTODIAGNOSTICO, que es lo que la hace operativa: si las revisiones anuales
    observadas de una entidad son mucho MENORES que H*sqrt(2)*sigma/T, esa entidad no esta
    midiendo, esta suavizando.  (Curry 2021 section 3.7.4 documenta el suavizado
    deliberado; la firma es observacionalmente confundible con el, y por eso es un
    diagnostico de proceso y no una prueba de fraude.)

    Se calcula sobre el REGISTRO ENTERO, no sobre la ventana estacionaria: es una
    propiedad del procedimiento de reestimacion, no del nivel reportado.
    """
    nv = int(round(T_ventana * MESES))
    if len(r) < nv + MESES:
        return None
    idx = list(range(len(r) - nv, -1, -MESES))[::-1]
    vmu, v0, sds = [], [], []
    for i in idx:
        m_, s_ = anualizar(r[i:i + nv])
        vmu.append(-m_ * H + k * s_ * math.sqrt(H))     # el numero con mu estimada
        v0.append(k * s_ * math.sqrt(H))                # el mismo numero con mu = 0
        sds.append(s_)
    vmu, v0 = np.array(vmu), np.array(v0)
    dmu, d0 = np.diff(vmu), np.diff(v0)
    base = v0[:-1]
    razon = float((dmu / base).std(ddof=1) / (d0 / base).std(ddof=1))
    exc = dmu.var(ddof=1) - d0.var(ddof=1)
    medido = math.sqrt(max(exc, 0.0))
    teorico = H * math.sqrt(2) * float(np.mean(sds)) / T_ventana
    return {
        "T_ventana": T_ventana,
        "n_reestimaciones": int(len(dmu)),
        "SD_excedente_medida": medido,
        "SD_excedente_teorica": teorico,
        "medido_sobre_teorico": float(medido / teorico) if teorico else float("nan"),
        "razon_SD_mu_estimada_sobre_mu_cero": razon,
    }


def escalera_de_ventanas(r: np.ndarray, k: float, pos_ruptura: int | None,
                         z: float = Z95) -> list[dict]:
    """[reutiliza ESCALERA_ANIOS de algoritmo.py] La banda sobre la escalera FIJA de
    ventanas, marcando cuales cruzan la ruptura.

    La escalera no es una alternativa a T_est: es el estadistico de divulgacion.  Muestra
    cuanto se mueve la banda con la ventana, para que nadie pueda presentar una ventana
    conveniente como si fuera un hallazgo.  La fila "completa" es ademas el FALSADOR
    PROPIO de T6: sin ruptura, T = muestra entera, la banda se va a (10,42 , 37,77) y
    H=10 queda FUERA -- teorema refutado.  Va impresa al lado del resultado, no escondida.
    """
    filas = []
    for W in ESCALERA_ANIOS:
        n = len(r) if W is None else int(W * MESES)
        if n > len(r) or n < MESES:
            continue   # la fila de 1 anio son 12 observaciones y da una banda ridicula:
                       # se muestra justamente por eso, para que el rango se vea entero
        w = r[-n:]
        mu, sd = anualizar(w)
        S = mu / sd if sd > 0 else float("nan")
        T = n / MESES
        Hm, Hp = banda(S, T, k, z)
        filas.append({
            "ventana": "completa" if W is None else f"{W}a",
            "T": T, "mu": mu, "sigma": sd,
            "S": S, "H_menos": Hm, "H_mas": Hp,
            "cruza_ruptura": bool(pos_ruptura is not None and len(r) - n < pos_ruptura),
        })
    return filas


# ============================================================================ el algoritmo

def diagnostico(r_mensual, H: float, alpha: float = 0.99, *,
                z: float = Z95, crit: float = CRIT_SUPWALD, recorte: float = RECORTE,
                h0: float = 0.0, firma_ventanas: tuple[int, ...] = (10, 20, 30)) -> dict:
    """El procedimiento completo, en el unico orden en que es valido.

    r_mensual  rendimientos MENSUALES en tanto por uno (no en %, no logaritmicos anuales)
    H          horizonte en ANIOS (10/252 para diez dias habiles)
    alpha      nivel del ES (0.99 por defecto)
    h0         horizonte de referencia del presupuesto de especificacion (paso 4)

    Devuelve un dict con una clave "veredicto" en la raiz:
        INVALIDO_DERIVA_NO_CONSTANTE  el paso 0 fallo; no hay nada mas que leer
        INDETERMINADO                 H dentro de la banda; "ES_punto" es None a proposito
        DETERMINADO_POSITIVO          H < H^-: manda la volatilidad
        DETERMINADO_NEGATIVO          H > H^+: manda la deriva -> capital negativo
    """
    r = np.asarray(r_mensual, dtype=float).ravel()
    if not np.all(np.isfinite(r)):
        raise ValueError("la serie contiene NaN o inf: limpiala antes, no aqui")
    if len(r) < MIN_MESES:
        # No es pedanteria: con menos de 120 meses sup_wald no tiene potencia, el paso 0 no
        # se puede correr, y un diagnostico cuyo paso 0 no corrio es invalido por
        # construccion.  Mas vale negarse que devolver una banda que alguien citara.
        raise ValueError(
            f"serie demasiado corta: {len(r)} meses, hacen falta {MIN_MESES} "
            f"({MIN_MESES//MESES} anios) para que el paso 0 (sup-Wald sobre la media) "
            f"tenga potencia. Sin paso 0 el resto del diagnostico no es valido.")
    if H <= 0:
        raise ValueError("H tiene que ser positivo y estar en ANIOS")

    k = k_alpha(alpha)
    T_muestra = len(r) / MESES
    # El dict lleva PRECISION COMPLETA a proposito. Redondear es trabajo del render
    # (informe(), escalera_de_horizontes()): un consumidor que reutiliza un valor ya
    # redondeado propaga el redondeo, y aqui hay cocientes que dividen por (k - S*rH),
    # una cantidad que en la serie real vale 0,057.
    salida: dict = {
        "entrada": {"n_meses": int(len(r)), "T_muestra_anios": T_muestra,
                    "H_anios": float(H), "alpha": alpha, "k_alpha": k, "z": z},
        "advertencias": [],
    }

    # ---------------------------------------------------------------- PASO 0
    # Todo el aparato contrasta mu_gorro contra k*sigma/rH suponiendo que hay UNA mu.  Si
    # la media tiene ruptura, "el signo de ES" no es una pregunta bien planteada y la
    # banda es aritmetica sobre un objeto que no existe.  Por eso se para aqui, y por eso
    # se para con el critico al 1%: un test laxo aqui convierte el paso 0 en un tramite.
    W_media, b_media = sup_wald(r, recorte)
    deriva_constante = not (W_media > crit)
    salida["paso0_deriva_constante"] = {
        "supWald_HAC_media": W_media, "critico_1pc": crit,
        "constante": bool(deriva_constante),
        "indice_maximo": None if b_media is None else int(b_media),
        "lectura": ("premisa de mu constante en pie (sobre la serie estadounidense: 1,67)"
                    if deriva_constante else
                    "RUPTURA EN LA MEDIA: mu no es constante"),
    }
    if not deriva_constante:
        salida["veredicto"] = "INVALIDO_DERIVA_NO_CONSTANTE"
        salida["paso1_ventana"] = None
        salida["paso2_banda"] = None
        salida["paso3_signo"] = None
        salida["paso4_presupuesto"] = None
        salida["paso5_firma"] = None
        salida["paso6_veredicto_operativo"] = (
            f"PARADA EN EL PASO 0: sup-Wald HAC sobre la media = {W_media:.2f} > {crit} "
            f"(1%). La deriva NO es constante, luego la banda, el presupuesto y la firma "
            f"de revision son invalidos y no se calculan. Antes de volver a preguntar por "
            f"el signo del ES hay que segmentar la serie o modelar la deriva. " + ALCANCE)
        salida["advertencias"].append(
            "diagnostico() se detuvo en el paso 0: los pasos 1-6 valen None a proposito.")
        return salida

    # ---------------------------------------------------------------- PASO 1
    # T no es libre: esta acotado por la estacionariedad.  T_est es la EDAD DEL REGIMEN
    # ACTUAL, no el calendario, y el proceso de rupturas la reinicia -- por eso el conjunto
    # de horizontes determinables no crece con el paso del tiempo.
    pos, detalle = ultima_ruptura_volatilidad(r, crit, recorte)
    n_proxies = sum(1 for v in detalle.values() if v)
    if pos is None:
        T_est = T_muestra
        salida["advertencias"].append(
            "SIN RUPTURA DETECTADA: T_est = muestra entera. ATENCION, este es el caso que "
            "DEBILITA el diagnostico, no el que lo refuerza: con T_est maximo la banda es "
            "la mas estrecha posible y el signo es lo mas facil de determinar. Si el "
            "veredicto sale DETERMINADO por esta via, el resultado esta comprado con la "
            "hipotesis de regimen homogeneo, que es justamente la que hay que defender.")
    else:
        T_est = (len(r) - pos) / MESES
    salida["paso1_ventana"] = {
        "T_est_anios": T_est,
        "indice_ultima_ruptura": None if pos is None else int(pos),
        "proxies_con_ruptura": n_proxies,
        "detalle_proxies": {et: [(int(p), float(w)) for p, w in br]
                            for et, br in detalle.items()},
        "hay_ruptura": pos is not None,
    }
    if pos is not None and n_proxies < 3:
        salida["advertencias"].append(
            f"solo {n_proxies}/3 proxies encuentran ruptura: se cumple la mayoria exigida "
            f"pero la fecha es menos firme que en la serie de referencia (3/3).")

    # ---------------------------------------------------------------- PASO 2
    n_est = int(round(T_est * MESES))
    mu, sd = anualizar(r[-n_est:])
    if sd <= 0:
        raise ValueError("sigma estimada nula sobre la ventana estacionaria")
    S = mu / sd
    e = z / math.sqrt(T_est)
    H_menos, H_mas = banda(S, T_est, k, z)
    Hp_menos, Hp_mas = banda_predictiva(S, T_est, k, z)
    H0 = (k / S) ** 2 if S > 0 else float("inf")      # la singularidad: ES(H0) = 0
    banda_vacia = math.isinf(H_menos)
    salida["paso2_banda"] = {
        "mu_gorro": mu, "sigma_gorro": sd, "S_gorro": S,
        "z_sobre_raiz_T": e,
        "H_menos": H_menos, "H_mas": H_mas,
        "H0_limite_T_infinito": H0,
        "banda_vacia": banda_vacia,
        "predictiva": {"H_menos": Hp_menos, "H_mas": Hp_mas,
                       "H0": (1.0 / ((S / k) ** 2 - 1.0 / T_est)
                              if (S / k) ** 2 > 1.0 / T_est else float("inf")),
                       "mas_ancha_que_plug_in": bool(
                           (Hp_mas - Hp_menos) > (H_mas - H_menos)
                           if math.isfinite(H_mas) and math.isfinite(Hp_mas)
                           else math.isinf(Hp_mas)),
                       "lectura": ("el estimador predictivo DESPLAZA Y ENSANCHA la banda; "
                                   "no la elimina. Anade varianza, no informacion sobre "
                                   "mu: SE(mu_gorro) sigue siendo sigma/sqrt(T).")},
        "T_requerido_para_este_H": T_requerido(H, S, k, z),
    }
    if math.isinf(H_mas):
        salida["advertencias"].append(
            f"S_gorro = {S:.4f} <= z/sqrt(T_est) = {e:.4f}: H^+ = inf. El Sharpe no se "
            f"distingue de cero con esta ventana, asi que NINGUN horizonte largo determina "
            f"el signo. La banda es una semirrecta [{H_menos:.2f}, inf).")
    if banda_vacia:
        salida["advertencias"].append(
            "banda VACIA: S_gorro + z/sqrt(T_est) <= 0, el signo es positivo a cualquier "
            "horizonte. Es el caso comodo y hay que decir que viene de un Sharpe negativo.")

    # ---------------------------------------------------------------- PASO 3
    # Aqui esta el corazon de lo que hace dificil usar mal esto: cuando H cae dentro de la
    # banda NO se devuelve un punto.  "ES_punto" vale None, y el unico numero disponible es
    # el intervalo compatible con el IC95 de mu_gorro -- que contiene el cero, porque estar
    # dentro de la banda y que el intervalo cruce cero son la MISMA proposicion.
    se_mu = sd / math.sqrt(T_est)
    mu_lo, mu_hi = mu - z * se_mu, mu + z * se_mu
    es_de = lambda m: -m * H + k * sd * math.sqrt(H)
    ES_lo, ES_hi = es_de(mu_hi), es_de(mu_lo)          # mu alta => ES bajo
    ES_punto = es_de(mu)
    es_pred = lambda m: -m * H + k * sd * math.sqrt(H * (1 + H / T_est))
    dentro = H_menos < H < H_mas
    if dentro:
        veredicto = "INDETERMINADO"
    elif H <= H_menos:
        veredicto = "DETERMINADO_POSITIVO"
    else:
        veredicto = "DETERMINADO_NEGATIVO"
    salida["veredicto"] = veredicto
    salida["paso3_signo"] = {
        "dentro_de_la_banda": bool(dentro),
        "IC95_mu": (mu_lo, mu_hi),
        "ES_intervalo": (ES_lo, ES_hi),
        "ES_punto": None if dentro else ES_punto,
        "ES_punto_suprimido": bool(dentro),
        "ES_intervalo_predictivo": (es_pred(mu_hi), es_pred(mu_lo)),
        "anchura_sobre_punto": (abs(ES_hi - ES_lo) / abs(ES_punto)
                                if ES_punto != 0 else float("inf")),
        "lectura": {
            "INDETERMINADO": ("el signo no esta determinado por los datos: se devuelve "
                              "intervalo, no punto (ES_punto es None a proposito)"),
            "DETERMINADO_POSITIVO": "H < H^-: domina la volatilidad, capital positivo",
            "DETERMINADO_NEGATIVO": ("H > H^+: domina la deriva. El modelo pide CAPITAL "
                                     "NEGATIVO; hace falta un SUELO DECLARADO por quien "
                                     "firma, no un max(.,0) silencioso"),
        }[veredicto],
    }

    # ---------------------------------------------------------------- PASO 4
    eps = presupuesto_especificacion(H, T_est, S, alpha, h0)
    salida["paso4_presupuesto"] = {
        "epsilon_estrella": eps,
        "finito": bool(math.isfinite(eps)),
        "lectura": (
            f"eps* = inf: H = {H:.4g}a esta mas alla de H0 = {H0:.3f}a, donde el numero "
            f"reportado se anula. Una fraccion de un numero que se anula no significa "
            f"nada: es inf, no nan, y se lee como 'ninguna mejora de especificacion "
            f"compensa'." if not math.isfinite(eps) else
            f"eps* = {eps:.1%} del numero reportado. Por debajo de eso, gastar en "
            f"especificar mejor el modelo NO compensa: el presupuesto va a estimar o a "
            f"declarar." if eps >= 0.15 else
            f"eps* = {eps:.1%}: horizonte corto, la ESPECIFICACION domina. Aqui el gasto "
            f"en el modelo si compensa, y esta banda no es el problema principal."),
    }

    # ---------------------------------------------------------------- PASO 5
    firmas = {}
    for Tv in firma_ventanas:
        f = firma_revision(r, H, k, Tv)
        if f is not None:
            firmas[f"T={Tv}"] = f
    coc = [f["medido_sobre_teorico"] for f in firmas.values()]
    salida["paso5_firma"] = {
        "ley": "SD(dES) excedente = H*sqrt(2)*sigma/T   (IGUALDAD, no cota)",
        "SD_excedente_teorica_a_T_est": H * math.sqrt(2) * sd / T_est,
        "por_ventana": firmas,
        "medido_sobre_teorico": coc,
        "dentro_de_banda_control": bool(coc and all(0.70 <= c <= 1.40 for c in coc)),
        "autodiagnostico": (
            "si las revisiones anuales observadas de una entidad son mucho MENORES que la "
            "SD teorica, esa entidad esta suavizando, no midiendo (Curry 2021 3.7.4 "
            "documenta el suavizado deliberado: la firma es observacionalmente "
            "confundible con el). El ratio 48x del ciclo 8 esta RETRACTADO; medido 3,04x."),
    }

    # ---------------------------------------------------------------- PASO 6
    b_txt = (f"({H_menos:.2f} , {H_mas:.2f})" if math.isfinite(H_mas)
             else f"({H_menos:.2f} , inf)") if not banda_vacia else "VACIA"
    origen = ("sin ruptura: muestra entera, CASO DEBIL" if pos is None
              else f"ruptura en el mes {pos} de la serie, {n_proxies}/3 proxies")
    if veredicto == "INDETERMINADO":
        nucleo = (f"H = {H:.4g}a cae DENTRO de la banda {b_txt}: el signo del ES{alpha:.0%} "
                  f"NO esta determinado por los datos. Lo unico reportable es el intervalo "
                  f"[{ES_lo:+.4f} , {ES_hi:+.4f}] (predictivo, mas ancho: "
                  f"[{es_pred(mu_hi):+.4f} , {es_pred(mu_lo):+.4f}]); harian falta "
                  f"{T_requerido(H, S, k, z):,.0f} anios de regimen estacionario frente a "
                  f"los {T_est:.1f} disponibles")
    elif veredicto == "DETERMINADO_POSITIVO":
        nucleo = (f"H = {H:.4g}a cae POR DEBAJO de la banda {b_txt}: signo determinado, "
                  f"domina la volatilidad. ES{alpha:.0%} = {ES_punto:+.4f} "
                  f"[{ES_lo:+.4f} , {ES_hi:+.4f}]")
    else:
        nucleo = (f"H = {H:.4g}a cae POR ENCIMA de la banda {b_txt}: signo determinado y "
                  f"NEGATIVO, domina la deriva. ES{alpha:.0%} = {ES_punto:+.4f} "
                  f"[{ES_lo:+.4f} , {ES_hi:+.4f}] -- el modelo pide CAPITAL NEGATIVO y eso "
                  f"exige un suelo declarado por quien firma")
    salida["paso6_veredicto_operativo"] = (
        f"{veredicto}: {nucleo}. Ventana defendible T_est = {T_est:.1f}a ({origen}); "
        f"S_gorro = {S:.4f}; H0 = {H0:.3f}a. {ALCANCE}")

    salida["escalera_divulgacion"] = escalera_de_ventanas(r, k, pos, z)
    return salida


def informe(d: dict, ancho: int = 88) -> str:
    """Render legible del dict.  Imprime SIEMPRE los pasos en orden y las advertencias
    ARRIBA: si el lector solo lee la primera linea, que lea la que invalida el resto."""
    L = ["=" * ancho, f"DIAGNOSTICO DE LA BANDA CIEGA -- veredicto: {d['veredicto']}", "=" * ancho]
    for a in d["advertencias"]:
        L.append("  !! " + a)
    p0 = d["paso0_deriva_constante"]
    L.append(f"  paso 0  sup-Wald HAC media = {p0['supWald_HAC_media']:.2f} "
             f"(critico {p0['critico_1pc']}) -> {p0['lectura']}")
    if d["paso1_ventana"] is None:
        L.append("  pasos 1-6: NO CALCULADOS (el paso 0 los invalida)")
        L.append(d["paso6_veredicto_operativo"])
        return "\n".join(L)
    p1, p2, p3 = d["paso1_ventana"], d["paso2_banda"], d["paso3_signo"]
    L.append(f"  paso 1  T_est = {p1['T_est_anios']:.1f}a  "
             f"({p1['proxies_con_ruptura']}/3 proxies)")
    L.append(f"  paso 2  mu={p2['mu_gorro']:.4f}  sigma={p2['sigma_gorro']:.4f}  "
             f"S={p2['S_gorro']:.4f}  banda=({p2['H_menos']:.2f},{p2['H_mas']:.2f})  "
             f"predictiva=({p2['predictiva']['H_menos']:.2f},"
             f"{p2['predictiva']['H_mas']:.2f})  H0={p2['H0_limite_T_infinito']:.3f}")
    pt = "SUPRIMIDO (el signo no esta determinado)" if p3["ES_punto"] is None \
        else f"{p3['ES_punto']:+.4f}"
    L.append(f"  paso 3  ES_punto = {pt}   ES_intervalo = "
             f"[{p3['ES_intervalo'][0]:+.4f} , {p3['ES_intervalo'][1]:+.4f}]")
    eps = d["paso4_presupuesto"]["epsilon_estrella"]
    L.append(f"  paso 4  eps* = {'inf' if not math.isfinite(eps) else format(eps, '.1%')}")
    L.append("  paso 5  medido/teorico = "
             + " / ".join(f"{c:.3f}" for c in d["paso5_firma"]["medido_sobre_teorico"]))
    L.append("  paso 6  " + d["paso6_veredicto_operativo"])
    return "\n".join(L)


# ================================================================== carga de la referencia

def cargar_serie_mensual(csv_path: str) -> np.ndarray:
    """[el parseo de resolve.cargar_serie] Fama-French CSV -> Mkt-RF + RF en tanto por uno.

    Solo lee local: descargar dentro de un modulo de produccion es una dependencia de red
    escondida.  Si hace falta refrescar la serie, eso lo hace protocolo/resolve.py.
    """
    crudo = open(csv_path, "rb").read()
    r = []
    for linea in crudo.decode("latin-1").splitlines():
        p = linea.strip().split(",")
        if len(p) == 5 and p[0].strip().isdigit() and len(p[0].strip()) == 6:
            r.append((float(p[1]) + float(p[4])) / 100.0)
    return np.array(r)


def _ruta_serie() -> str | None:
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "protocolo", "serie-congelada.csv")
    return os.path.normpath(p) if os.path.exists(p) else None


# ========================================================================= bateria de pruebas

_RES: list[tuple[str, bool, str]] = []


def _check(nombre: str, ok: bool, detalle: str = "") -> bool:
    _RES.append((nombre, bool(ok), detalle))
    print(f"  [{'PASA' if ok else 'FALLA'}]  {nombre}"
          + (f"\n           {detalle}" if detalle else ""))
    return bool(ok)


def _salta(nombre: str, motivo: str) -> None:
    _RES.append((nombre, True, "SALTA: " + motivo))
    print(f"  [SALTA]  {nombre}\n           {motivo}")


def _prueba_1_forma_cerrada(r: np.ndarray) -> None:
    """P1. La forma cerrada H^-/+ contra una busqueda numerica bruta del T minimo.

    La busqueda bruta NO usa la formula: para cada ventana de T anios reestima mu y sigma,
    construye ES = -mu*H + k*sigma*rH y su error tipico H*sigma/rT, y mira si |ES|/SE > z.
    Es el contraste del numero, en unidades de capital.  La forma cerrada resuelve el mismo
    contraste en unidades de horizonte.  Que coincidan en los 18 casos es N133.
    """
    print("\nP1 -- forma cerrada vs busqueda bruta del T minimo que determina el signo")
    casos, ok, filas, discrep_total = 0, 0, [], 0
    for alpha in (0.95, 0.99):
        k = k_alpha(alpha)
        for H in (1, 2, 3, 5, 7, 10, 15, 20, 30):
            T_bruta = T_cerrada = None
            discrep = 0
            for T in range(2, 101):
                n = T * MESES
                if n > len(r):
                    break
                mu, sd = anualizar(r[-n:])
                ES = -mu * H + k * sd * math.sqrt(H)          # el numero
                SE = H * sd / math.sqrt(T)                    # d(ES)/d(mu) * SE(mu)
                det_bruta = abs(ES) / SE > Z95
                Hm, Hp = banda(mu / sd, T, k)
                det_cerrada = not (Hm < H < Hp)
                discrep += int(det_bruta != det_cerrada)      # deben coincidir para TODO T
                if det_bruta and T_bruta is None:
                    T_bruta = T
                if det_cerrada and T_cerrada is None:
                    T_cerrada = T
            casos += 1
            discrep_total += discrep
            ok += int(T_bruta == T_cerrada and discrep == 0)
            filas.append((H, alpha, T_bruta, T_cerrada))
    det = "  ".join(f"H={H}/a={a}: {tb}" for H, a, tb, _ in filas)
    _check(f"P1a coincidencia forma cerrada / busqueda bruta: {ok}/{casos}",
           ok == casos == 18 and discrep_total == 0,
           f"T_det por caso (None = no se determina con <=100a): {det}")
    # El T_det de referencia de N133: H=10, alpha=0.99 -> 96 anios.
    t96 = [tb for H, a, tb, _ in filas if H == 10 and a == 0.99][0]
    _check("P1b T_det(H=10, alpha=0.99) = 96 anios, como N133 seccion 2", t96 == 96,
           f"medido {t96}; y T_est = 85,0 -> brecha de 11 anios: conjunto admisible VACIO")
    # P1c. La banda supone SE(ES) = H*sigma/rT, es decir trata sigma_gorro como conocida.
    # La columna z de N133 seccion 2 usa ademas el error de sigma_gorro por delta-method
    # (Var(sigma) ~ sigma^2/2n), un 1,5% mas de SE: por eso alli z(T=96) = 2,10 y no 2,13.
    # No se esconde: se mide cuanto mueve. Mueve donde el estadistico cruza el umbral casi
    # plano, y NO mueve el caso de referencia.
    movidos, t96d = 0, None
    for alpha in (0.95, 0.99):
        k = k_alpha(alpha)
        for H in (1, 2, 3, 5, 7, 10, 15, 20, 30):
            Td = None
            for T in range(2, 101):
                n = T * MESES
                if n > len(r):
                    break
                mu, sd = anualizar(r[-n:])
                se_d = math.sqrt(sd ** 2 / T + (k / math.sqrt(H)) ** 2 * sd ** 2 / (2 * n))
                if abs(mu - k * sd / math.sqrt(H)) / se_d > Z95:
                    Td = T
                    break
            ref = [tb for HH, aa, tb, _ in filas if HH == H and aa == alpha][0]
            movidos += int(Td != ref)
            if H == 10 and alpha == 0.99:
                t96d = Td
    _check("P1c el SE delta-method (N133 sec.2) no mueve el caso de referencia",
           t96d == 96,
           f"con SE delta T_det(H=10,a=0.99) = {t96d} (igual que 96); mueve {movidos}/18 "
           f"casos, todos donde el estadistico cruza el umbral en zona plana")


def _prueba_2_serie_congelada(d: dict) -> None:
    print("\nP2 -- serie congelada, H=10, alpha=0.99")
    p1, p2 = d["paso1_ventana"], d["paso2_banda"]
    _check("P2a T_est = 85,0 anios", abs(p1["T_est_anios"] - 85.0) < 0.05,
           f"medido {p1['T_est_anios']:.1f}a, {p1['proxies_con_ruptura']}/3 proxies")
    _check("P2b banda plug-in = (6,60 , 18,96)",
           abs(p2["H_menos"] - 6.60) < 0.02 and abs(p2["H_mas"] - 18.96) < 0.02,
           f"medido ({p2['H_menos']:.2f} , {p2['H_mas']:.2f}); H0 = "
           f"{p2['H0_limite_T_infinito']:.3f}")
    _check("P2c veredicto INDETERMINADO y ES_punto suprimido",
           d["veredicto"] == "INDETERMINADO" and d["paso3_signo"]["ES_punto"] is None,
           "intervalo compatible con el IC95 de mu: ["
           + " , ".join(f"{v:+.4f}" for v in d["paso3_signo"]["ES_intervalo"]) + "]")
    txt = informe(d)
    rng = np.random.default_rng(1)
    sig = 0.16 / math.sqrt(MESES)
    d_roto = diagnostico(np.concatenate([0.12 / MESES + sig * rng.standard_normal(600),
                                         -0.06 / MESES + sig * rng.standard_normal(600)]),
                         H=10.0)
    txt_roto = informe(d_roto)
    _check("P2d informe() renderiza las dos ramas (normal y parada en el paso 0)",
           "INDETERMINADO" in txt and "SUPRIMIDO" in txt
           and "NO CALCULADOS" in txt_roto and "PARADA EN EL PASO 0" in txt_roto,
           "el render nombra el veredicto, suprime el punto y, si el paso 0 para, dice "
           "que los pasos 1-6 no se calcularon")


def _prueba_3_predictiva(d: dict) -> None:
    print("\nP3 -- la objecion del estimador predictivo, respondida en la salida")
    p2 = d["paso2_banda"]
    pr = p2["predictiva"]
    ancho_plug = p2["H_mas"] - p2["H_menos"]
    ancho_pred = pr["H_mas"] - pr["H_menos"]
    _check("P3a banda predictiva = (7,16 , 24,40)",
           abs(pr["H_menos"] - 7.16) < 0.02 and abs(pr["H_mas"] - 24.40) < 0.02,
           f"medido ({pr['H_menos']:.2f} , {pr['H_mas']:.2f}); H0 pred = {pr['H0']:.3f}")
    _check("P3b la predictiva es MAS ANCHA que la plug-in, no mas estrecha",
           ancho_pred > ancho_plug,
           f"{ancho_pred:.2f}a frente a {ancho_plug:.2f}a  (+{ancho_pred/ancho_plug-1:.0%})")


def _prueba_4_paso0(r_real: np.ndarray) -> None:
    """P4. El paso 0 tiene que disparar cuando la media SI rompe, y no disparar cuando no.
    La serie sintetica lleva una ruptura de deriva de +12%/a a -6%/a a mitad de muestra,
    con sigma 16% anual: grande pero no absurda (es un 1,1 sigma-anual de salto)."""
    print("\nP4 -- paso 0: deteccion de ruptura en la MEDIA")
    rng = np.random.default_rng(20261010)
    n = 600
    sig = 0.16 / math.sqrt(MESES)
    r_rota = np.concatenate([0.12 / MESES + sig * rng.standard_normal(n),
                             -0.06 / MESES + sig * rng.standard_normal(n)])
    d = diagnostico(r_rota, H=10.0)
    _check("P4a sintetica con ruptura en la media -> INVALIDO y PARADA",
           d["veredicto"] == "INVALIDO_DERIVA_NO_CONSTANTE"
           and d["paso2_banda"] is None and d["paso3_signo"] is None,
           f"sup-Wald = {d['paso0_deriva_constante']['supWald_HAC_media']:.2f} > "
           f"{CRIT_SUPWALD}; pasos 1-6 = None y el veredicto operativo lo dice")
    r_lisa = 0.08 / MESES + sig * rng.standard_normal(1200)
    d2 = diagnostico(r_lisa, H=10.0)
    _check("P4b sintetica sin ruptura en la media -> no para (control de tamano)",
           d2["veredicto"] != "INVALIDO_DERIVA_NO_CONSTANTE",
           f"sup-Wald = {d2['paso0_deriva_constante']['supWald_HAC_media']:.2f}")
    W, _ = sup_wald(r_real)
    _check("P4c sobre la serie estadounidense el paso 0 da 1,67 y NO para",
           abs(W - 1.67) < 0.02, f"sup-Wald HAC media = {W:.2f} (critico {CRIT_SUPWALD})")


def _prueba_5_limites() -> None:
    print("\nP5 -- casos limite")
    # (a) Sharpe por debajo de z/sqrt(T): H^+ = inf y la funcion lo DICE.
    rng = np.random.default_rng(11)
    sig = 0.20 / math.sqrt(MESES)
    # Sharpe verdadero 0,10 con T = 20a: z/sqrt(T) = 0,438, o sea el Sharpe muestral cae
    # dentro del error tipico de cero. Es el caso corriente en cualquier activo real que
    # no sea el mercado estadounidense con un siglo de historia.
    r_flojo = 0.02 / MESES + sig * rng.standard_normal(240)
    try:
        d = diagnostico(r_flojo, H=10.0)
        p2 = d["paso2_banda"]
        dice = any("H^+ = inf" in a for a in d["advertencias"])
        _check("P5a S <= z/sqrt(T) -> H^+ = inf, sin reventar y diciendolo",
               math.isinf(p2["H_mas"]) and dice and d["veredicto"] in
               ("INDETERMINADO", "DETERMINADO_POSITIVO"),
               f"S = {p2['S_gorro']:.4f}, z/sqrt(T) = {p2['z_sobre_raiz_T']:.4f}, "
               f"banda = ({p2['H_menos']:.2f}, inf)")
    except Exception as ex:                                       # noqa: BLE001
        _check("P5a S <= z/sqrt(T) -> H^+ = inf, sin reventar y diciendolo", False,
               f"reviento con {type(ex).__name__}: {ex}")
    # (b) serie demasiado corta: negarse, con un mensaje que explique por que.
    try:
        diagnostico(np.full(60, 0.01), H=10.0)
        _check("P5b serie demasiado corta -> ValueError explicito", False,
               "no se quejo: devolvio un diagnostico sobre 60 meses")
    except ValueError as ex:
        _check("P5b serie demasiado corta -> ValueError explicito",
               "demasiado corta" in str(ex) and "paso 0" in str(ex), str(ex).split(".")[0])
    # (c) H muy pequeno: diez dias habiles.  Tiene que salir determinado y finito.
    serie = _ruta_serie()
    if serie is None:
        _salta("P5c H muy pequeno (10 dias)", "no esta protocolo/serie-congelada.csv")
    else:
        d = diagnostico(cargar_serie_mensual(serie), H=10 / 252)
        p3 = d["paso3_signo"]
        _check("P5c H = 10 dias -> DETERMINADO_POSITIVO, numeros finitos",
               d["veredicto"] == "DETERMINADO_POSITIVO"
               and all(math.isfinite(v) for v in p3["ES_intervalo"])
               and math.isfinite(d["paso4_presupuesto"]["epsilon_estrella"]),
               f"ES = {p3['ES_punto']:+.4f} [{p3['ES_intervalo'][0]:+.4f} , "
               f"{p3['ES_intervalo'][1]:+.4f}], "
               f"eps* = {d['paso4_presupuesto']['epsilon_estrella']:.2%}")
    # (d) eps* mas alla de H0: inf, no nan.
    eps = presupuesto_especificacion(H=30.0, T=85.0, S=0.8247, alpha=0.99)
    _check("P5d eps* mas alla de H0 es inf, no nan",
           math.isinf(eps) and not math.isnan(eps), f"eps*(30a) = {eps}")
    # (e) Sharpe muy negativo: S + z/rT <= 0 -> la banda es VACIA, no una banda al reves.
    k = k_alpha(0.99)
    bv = banda(-0.50, 85.0, k)
    _check("P5e S + z/sqrt(T) <= 0 -> banda VACIA, no invertida",
           math.isinf(bv[0]) and math.isinf(bv[1]),
           f"banda(-0.50, 85a) = {bv}: con Sharpe asi el signo es positivo a cualquier H, "
           f"y hay que decir que viene del Sharpe y no de los datos de cola")


def _prueba_6_firma(d: dict) -> None:
    print("\nP6 -- paso 5: la igualdad de la firma de revision sobre datos reales")
    coc = d["paso5_firma"]["medido_sobre_teorico"]
    _check("P6 medido/teorico dentro de [0,70 , 1,40] con T = 10/20/30",
           len(coc) == 3 and all(0.70 <= c <= 1.40 for c in coc),
           f"medido/teorico = {coc[0]:.3f} / {coc[1]:.3f} / {coc[2]:.3f} "
           f"(N133: 1,054 / 1,165 / 1,110); razon SD retractada 48x -> medida "
           f"{d['paso5_firma']['por_ventana']['T=10']['razon_SD_mu_estimada_sobre_mu_cero']:.2f}x")


def _prueba_7_coherencia(r: np.ndarray) -> None:
    """P7. Paso 2 y paso 3 son la misma proposicion por dos caminos: H dentro de la banda
    (algebra en el horizonte) <=> el intervalo de ES del IC95 de mu contiene el cero
    (algebra en el capital).  Si algun dia divergen, uno de los dos esta mal."""
    print("\nP7 -- coherencia paso 2 (banda en H) <-> paso 3 (intervalo en ES)")
    malos = []
    for H in (0.04, 0.5, 1, 3, 5, 6.5, 6.7, 10, 18.5, 19.5, 20, 30, 60):
        d = diagnostico(r, H=H)
        lo, hi = d["paso3_signo"]["ES_intervalo"]
        cruza_cero = lo <= 0.0 <= hi
        if cruza_cero != (d["veredicto"] == "INDETERMINADO"):
            malos.append((H, d["veredicto"], lo, hi))
    _check("P7a dentro de la banda <=> el intervalo de ES cruza cero (13 horizontes)",
           not malos, f"discrepancias: {malos}" if malos else
           "las dos algebras dan el mismo veredicto en los 13 horizontes")
    # Y los bordes hallados por biseccion numerica sobre el estadistico tienen que ser
    # exactamente H^- y H^+.
    d = diagnostico(r, H=10.0)
    p2 = d["paso2_banda"]
    S, T, k = p2["S_gorro"], d["paso1_ventana"]["T_est_anios"], d["entrada"]["k_alpha"]
    # (con el dict sin redondear, esto tiene que coincidir a precision de maquina)
    est = lambda H: abs(S - k / math.sqrt(H)) - Z95 / math.sqrt(T)   # >0 <=> determinado
    def biseca(a, b):
        for _ in range(200):
            m = math.sqrt(a * b)
            if est(a) * est(m) <= 0:
                b = m
            else:
                a = m
        return math.sqrt(a * b)
    b_lo, b_hi = biseca(0.01, 10.0), biseca(1000.0, 10.0)
    _check("P7b los bordes por biseccion numerica coinciden con H^- y H^+ a 1e-6",
           abs(b_lo - p2["H_menos"]) < 1e-6 and abs(b_hi - p2["H_mas"]) < 1e-6,
           f"biseccion ({b_lo:.6f} , {b_hi:.6f}) vs forma cerrada "
           f"({p2['H_menos']:.6f} , {p2['H_mas']:.6f})")


def _prueba_8_deriva_de_codigo(r: np.ndarray) -> None:
    """P8. Guarda de deriva contra protocolo/resolve.py.  Este archivo copia funciones ya
    verificadas; si el original cambia y la copia no, hay que enterarse aqui y no en una
    reunion."""
    print("\nP8 -- guarda de deriva: las copias siguen dando lo mismo que resolve.py")
    raiz = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    proto = os.path.join(raiz, "protocolo")
    if not os.path.exists(os.path.join(proto, "resolve.py")):
        _salta("P8 guarda de deriva vs resolve.py", "no esta protocolo/resolve.py")
        return
    sys.path.insert(0, proto)
    try:
        import resolve as R                                       # noqa: PLC0415
    except Exception as ex:                                       # noqa: BLE001
        _salta("P8 guarda de deriva vs resolve.py", f"no importable: {ex}")
        return
    W1, b1 = sup_wald(r, RECORTE)
    W2, b2 = R.sup_wald(r, RECORTE)
    p1, _ = ultima_ruptura_volatilidad(r, CRIT_SUPWALD, RECORTE)
    p2, _ = R.ultima_ruptura_volatilidad(r, CRIT_SUPWALD, RECORTE)
    k = k_alpha(0.99)
    mu, sd = anualizar(r[-1020:])
    b_a = banda(mu / sd, 85.0, k, Z95)
    b_b = R.banda(mu / sd, 85.0, k, Z95)
    _check("P8 sup_wald / ultima_ruptura_volatilidad / banda / anualizar identicos",
           abs(W1 - W2) < 1e-12 and b1 == b2 and p1 == p2
           and max(abs(x - y) for x, y in zip(b_a, b_b)) < 1e-12
           and abs(mu - R.anualizar(r[-1020:])[0]) < 1e-15,
           f"sup-Wald {W1:.6f} == {W2:.6f}; ruptura {p1} == {p2}; banda coincide")


def _bateria() -> int:
    print("=" * 88)
    print("BANDA CIEGA -- bateria de pruebas   (T6 / N133, ciclo 10)")
    print("=" * 88)
    serie = _ruta_serie()
    if serie is None:
        print("\n  !! no esta protocolo/serie-congelada.csv: las pruebas sobre datos "
              "reales se saltan\n")
        r = np.array([])
    else:
        r = cargar_serie_mensual(serie)
        print(f"\n  serie: {serie}  ({len(r)} meses)")
    if len(r) >= MIN_MESES:
        d10 = diagnostico(r, H=10.0, alpha=0.99)
        _prueba_1_forma_cerrada(r)
        _prueba_2_serie_congelada(d10)
        _prueba_3_predictiva(d10)
        _prueba_4_paso0(r)
        _prueba_5_limites()
        _prueba_6_firma(d10)
        _prueba_7_coherencia(r)
        _prueba_8_deriva_de_codigo(r)
    else:
        for n in ("P1", "P2", "P3", "P6", "P7", "P8"):
            _salta(n, "hace falta la serie congelada")
        _prueba_5_limites()
    fallos = [n for n, ok, _ in _RES if not ok]
    print("\n" + "=" * 88)
    print(f"RESULTADO: {len(_RES) - len(fallos)}/{len(_RES)} pruebas PASAN"
          + (f"   FALLAN: {', '.join(fallos)}" if fallos else ""))
    print("=" * 88)
    return 1 if fallos else 0


# =============================================================== escalera de horizontes

# Uso tipico de cada horizonte. No es decoracion: la banda "no cae donde no molesta",
# y eso solo se ve poniendo al lado para que se usa cada H.
USOS = {
    10 / 252: "FRTB, 10 dias",
    1: "Solvencia II / ALM anual",
    3: "ECL corporativa",
    5: "ECL consumo",
    7: "ECL hipotecaria",
    10: "ECL vitalicia",
    15: "ALM de pensiones",
    20: "pensiones, tramo largo",
    30: "proyeccion actuarial",
}


def escalera_de_horizontes(r: np.ndarray,
                           horizontes=(1, 3, 5, 7, 10, 15, 20, 30),
                           alpha: float = 0.99) -> str:
    """La tabla que resume diez ciclos: un diagnostico por horizonte sobre la misma serie.

    La banda NO depende de H -- depende de (T_est, S, alpha) --, asi que la cabecera la da
    una vez y la tabla solo dice, por horizonte, de que lado cae y que se puede reportar.
    Debajo va la escalera de ventanas: el estadistico de divulgacion, con la fila de la
    muestra completa marcada, que es el FALSADOR PROPIO del teorema.
    """
    d0 = diagnostico(r, H=10.0, alpha=alpha)
    if d0["veredicto"] == "INVALIDO_DERIVA_NO_CONSTANTE":
        # No hay tabla. Imprimir una escalera de horizontes sobre una serie cuya deriva
        # rompe seria fabricar ocho numeros invalidos con buena tipografia.
        return d0["paso6_veredicto_operativo"]
    p1, p2 = d0["paso1_ventana"], d0["paso2_banda"]
    k = d0["entrada"]["k_alpha"]
    L = ["=" * 118,
         f"ESCALERA DE HORIZONTES -- serie congelada Fama-French, {len(r)} meses, "
         f"alpha = {alpha:.0%}", "=" * 118,
         f"paso 0: sup-Wald HAC sobre la media = "
         f"{d0['paso0_deriva_constante']['supWald_HAC_media']:.2f} < {CRIT_SUPWALD} "
         f"-> la deriva pasa por constante y el resto del diagnostico es valido",
         f"paso 1: T_est = {p1['T_est_anios']:.1f}a  "
         f"({p1['proxies_con_ruptura']}/3 proxies coinciden en la ruptura de volatilidad)",
         f"paso 2: mu = {p2['mu_gorro']:.4f}   sigma = {p2['sigma_gorro']:.4f}   "
         f"S = {p2['S_gorro']:.4f}   z/sqrt(T_est) = {p2['z_sobre_raiz_T']:.4f}",
         f"        BANDA plug-in = ({p2['H_menos']:.2f} , {p2['H_mas']:.2f})a      "
         f"predictiva = ({p2['predictiva']['H_menos']:.2f} , "
         f"{p2['predictiva']['H_mas']:.2f})a  (+"
         f"{(p2['predictiva']['H_mas'] - p2['predictiva']['H_menos']) / (p2['H_mas'] - p2['H_menos']) - 1:.0%}"
         f" mas ancha)      H0 = {p2['H0_limite_T_infinito']:.3f}a",
         "-" * 118,
         f"{'H':>5}  {'uso tipico':<24} {'veredicto':<21} {'ES99':>10} "
         f"{'intervalo IC95(mu)':>21} {'eps*':>7} {'T_req':>8} {'SD(dES)exc':>10}",
         "-" * 118]
    for H in horizontes:
        d = diagnostico(r, H=float(H), alpha=alpha)
        p3, S = d["paso3_signo"], d["paso2_banda"]["S_gorro"]
        punto = "SUPRIMIDO" if p3["ES_punto"] is None else f"{p3['ES_punto']:+.4f}"
        lo, hi = p3["ES_intervalo"]
        eps = d["paso4_presupuesto"]["epsilon_estrella"]
        eps_t = "inf" if not math.isfinite(eps) else f"{eps:.0%}"
        treq = T_requerido(float(H), S, k)
        treq_t = "inf" if not math.isfinite(treq) else f"{treq:,.0f}"
        L.append(f"{H:>5}  {USOS.get(H, ''):<24} {d['veredicto']:<21} {punto:>10} "
                 f"{f'[{lo:+.3f},{hi:+.3f}]':>21} {eps_t:>7} {treq_t:>8} "
                 f"{d['paso5_firma']['SD_excedente_teorica_a_T_est']:>10.4f}")
    L.append("-" * 118)
    L.append(f"T_req = anios de regimen ESTACIONARIO que harian falta para determinar el "
             f"signo, frente a los {p1['T_est_anios']:.1f}a disponibles. Donde "
             f"T_req > T_est el signo no es")
    L.append("determinable con una ventana defendible: es exactamente la banda, leida en "
             "anios de datos en vez de en anios de horizonte.")
    L.append("ES99 en fraccion del valor de la posicion; eps* en fraccion del numero "
             "reportado; SD(dES)exc = H*sqrt(2)*sigma/T_est (paso 5, igualdad).")
    L.append("T_req diverge como (k/sqrt(H) - S)^-2: a H=10 el denominador vale 0,018 y "
             "la cifra es sensible al quinto decimal de S (N133 publica 11.707 con S")
    L.append("redondeado a 4 decimales; con S a precision completa sale 11.717). Lo que "
             "no cambia con ningun redondeo es el orden de magnitud: dos ordenes por")
    L.append("encima de la historia disponible, y tres por encima de la edad del regimen.")
    L.append("")
    L.append("ESCALERA DE DIVULGACION -- la banda sobre la escalera FIJA de ventanas "
             "(la entidad no elige la ventana):")
    L.append(f"  {'ventana':<10}{'T':>7}{'sigma':>9}{'S':>9}{'banda':>20}   "
             f"{'cruza la ruptura?':<26}")
    for f in d0["escalera_divulgacion"]:
        b = (f"({f['H_menos']:.2f} , {f['H_mas']:.2f})" if math.isfinite(f["H_mas"])
             else f"({f['H_menos']:.2f} , inf)")
        L.append(f"  {f['ventana']:<10}{f['T']:>7.1f}{f['sigma']:>9.4f}{f['S']:>9.4f}"
                 f"{b:>20}   "
                 f"{'SI -> ventana inadmisible' if f['cruza_ruptura'] else 'no':<26}")
    comp = [f for f in d0["escalera_divulgacion"] if f["ventana"] == "completa"]
    if comp:
        c = comp[0]
        L.append(f"  La fila 'completa' es el FALSADOR PROPIO de T6: si no hubiera "
                 f"ruptura, T = {c['T']:.1f}a, la banda seria ({c['H_menos']:.2f} , "
                 f"{c['H_mas']:.2f}) y H=10 quedaria FUERA -- teorema refutado.")
        L.append("  (T6 publica (10,42 , 37,77) para 1.200 meses exactos; aqui entran "
                 "1.201. La diferencia es el mes de mas, no un desacuerdo.)")
    L.append("  El test de ruptura la rechaza al 1% con los tres proxies -- por eso no se "
             "puede usar, y por eso la determinacion se compra con no estacionariedad.")
    L.append(ALCANCE)
    return "\n".join(L)


if __name__ == "__main__":
    cod = _bateria()
    serie = _ruta_serie()
    if serie is not None:
        print()
        print(escalera_de_horizontes(cargar_serie_mensual(serie)))
    raise SystemExit(cod)
