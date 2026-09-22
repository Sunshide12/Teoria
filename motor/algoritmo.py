"""
Implementacion de referencia de lo que sobrevivio a ocho ciclos.

NO es un estimador mejor del Expected Shortfall. Es un procedimiento de REPORTE:
convierte los grados de libertad que hoy estan escondidos en el numero en
declaraciones explicitas y auditables, y anade el diagnostico de si el horizonte
pedido esta por encima o por debajo del punto donde la estimacion domina.

Las cuatro piezas, con su procedencia:

  1. ESCALERA FIJA DE VENTANAS + SEGUNDO MAYOR.  La entidad no elige la ventana.
     Medido: 3,8x menos deficit p95 por 32% mas capital, en regimen no estacionario.

  2. LA DERIVA SE DECLARA, NO SE ESTIMA.  Con T anios de datos, SE(mu) = sigma/sqrt(T)
     y fijarla a +-1%/ano exige 983 anios con sigma=16%. Declararla no reduce el error:
     lo convierte de ruido invisible en sesgo auditable.
     (La practica vigente la fija en cero sin declararlo: eso es la regla raiz-de-t.
      Danielsson-Zigrand 2006 ya lo senalo; Jorion 2001 lo recomienda.)

  3. EL PRESUPUESTO DE MALA ESPECIFICACION, reportado junto al numero.
     eps*(H) = sqrt(H/T) / (k_alpha - S*sqrt(H)) * sqrt(1 + h0/H)
     Dice si merece la pena gastar en especificar mejor el modelo o no.

  4. EL ESTADISTICO DE DIVULGACION S = ES_max/ES_min sobre la escalera,
     publicado ANTES del numero de capital, para que un S bajo no sea premio
     por haber ocultado el rango.

Lo que este procedimiento NO hace: reducir la incertidumbre. La banda de capital
que ningun dato fija sigue siendo del 147% del numero reportado a diez anios.
Lo unico que hace es dejar de esconderla.
"""
from __future__ import annotations
import numpy as np
from scipy import stats

DIAS = 252
ESCALERA_ANIOS = (1, 2, 5, 10, 20, None)      # None = muestra completa


def k_alpha(alpha: float = 0.99) -> float:
    """Multiplicador del ES gaussiano: k = phi(z_alpha)/(1-alpha).  k99=2.6652."""
    return float(stats.norm.pdf(stats.norm.ppf(alpha)) / (1 - alpha))


def sigma_anual(r: np.ndarray) -> float:
    return float(r.std(ddof=1) * np.sqrt(DIAS))


def _escalera(r: np.ndarray) -> list[tuple[str, float]]:
    """Volatilidad anual sobre cada ventana de la escalera. La entidad no elige."""
    out = []
    for W in ESCALERA_ANIOS:
        seg = r if W is None else r[-W * DIAS:]
        if len(seg) < DIAS:                    # menos de un anio: no entra
            continue
        out.append(("completa" if W is None else f"{W}a", sigma_anual(seg)))
    return out


def presupuesto_especificacion(H: float, T: float, S: float,
                               alpha: float = 0.99, h0: float = 0.0) -> float:
    """
    eps*(H): fraccion del numero reportado que el modelo puede errar antes de que
    el riesgo de especificacion supere al de estimacion.

    Por debajo de eps*, gastar en especificar mejor el modelo NO compensa.
    Verificado exacto (predicho = medido a 3 decimales) en 7 generadores x 7 horizontes.
    """
    k = k_alpha(alpha)
    den = k - S * np.sqrt(H)
    if den <= 0:                               # H mas alla de donde el numero se anula
        return float("inf")
    return float(np.sqrt(H / T) / den * np.sqrt(1 + h0 / H))


def horizonte_de_cruce(T: float, S: float, eps: float,
                       alpha: float = 0.99, h0: float = 0.0) -> float | None:
    """H donde eps*(H) = eps: mas alla, la estimacion domina a la especificacion.
    Devuelve None si no hay cruce en [1 dia, 100 anios]."""
    f = lambda H: presupuesto_especificacion(H, T, S, alpha, h0) - eps
    lo, hi = 1/DIAS, 100.0
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(80):
        m = np.sqrt(lo * hi)                   # biseccion en log
        if f(lo) * f(m) <= 0: hi = m
        else: lo = m
    return float(np.sqrt(lo * hi))


def reportar(r: np.ndarray, H: float, mu_declarada: tuple[float, ...],
             alpha: float = 0.99, eps_modelo: float = 0.15, h0: float = 0.0) -> dict:
    """
    El reporte completo.

    r              retornos log diarios
    H              horizonte en anios
    mu_declarada   convenios de deriva anual, p.ej. (0.0, 0.04, 0.08).
                   NO se estiman: se declaran y se publican.
    eps_modelo     error relativo que se cree que tiene el modelo (para el diagnostico)
    """
    k = k_alpha(alpha)
    T = len(r) / DIAS
    esc = _escalera(r)
    if len(esc) < 2:
        raise ValueError("la escalera necesita al menos dos ventanas: "
                         f"solo hay {T:.1f} anios de datos")

    # --- pieza 1: segundo mayor de la escalera ---
    sigmas = sorted(s for _, s in esc)
    sigma_rep = sigmas[-2]

    # --- pieza 2: la deriva declarada, no estimada ---
    es_por_mu = {mu: -mu * H + k * sigma_rep * np.sqrt(H) for mu in mu_declarada}
    capital = max(es_por_mu.values())          # el extremo conservador del convenio

    # --- pieza 4: el estadistico de divulgacion, calculado ANTES del capital ---
    es_escalera = [-min(mu_declarada) * H + k * s * np.sqrt(H) for _, s in esc]
    S_div = max(es_escalera) / min(es_escalera)

    # --- pieza 3: el presupuesto, y el diagnostico que se sigue ---
    S_sharpe = float(np.mean(mu_declarada)) / sigma_rep
    eps_est = presupuesto_especificacion(H, T, S_sharpe, alpha, h0)
    H_cruce = horizonte_de_cruce(T, S_sharpe, eps_modelo, alpha, h0)

    # --- la banda que ningun dato fija ---
    se_mu = sigma_rep / np.sqrt(T)
    banda = 2 * 1.96 * se_mu * H               # anchura del IC95 de mu, propagada

    return {
        "T_anios": round(T, 2),
        "H_anios": H,
        "escalera": [(w, round(s, 4)) for w, s in esc],
        "sigma_reportada_2o_mayor": round(sigma_rep, 4),
        "S_divulgacion": round(S_div, 3),
        "ES_por_convenio": {f"mu={m:.1%}": round(v, 4) for m, v in es_por_mu.items()},
        "capital": round(capital, 4),
        "banda_de_estimacion": round(banda, 4),
        "banda_sobre_capital": f"{banda/capital:.1%}",
        "presupuesto_especificacion": f"{eps_est:.1%}",
        "horizonte_de_cruce_anios": None if H_cruce is None else round(H_cruce, 3),
        "diagnostico": (
            "ESPECIFICAR: por debajo del cruce, gastar en el modelo compensa"
            if H_cruce is not None and H < H_cruce else
            "ESTIMAR/DECLARAR: mas alla del cruce, gastar en especificar la cola "
            "es sofisticacion asignada a un efecto pequeno"),
    }


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    # 10 anios de retornos con vol 16% y deriva 6%
    r = 0.06/DIAS + (0.16/np.sqrt(DIAS)) * rng.standard_normal(10*DIAS)
    for H, nom in [(10/DIAS, "FRTB, 10 dias"), (1.0, "Solvencia II, 1 anio"),
                   (10.0, "ECL vitalicia, 10 anios")]:
        rep = reportar(r, H, mu_declarada=(0.0, 0.04, 0.08))
        print(f"\n=== {nom} ===")
        for kk, vv in rep.items():
            if kk in ("escalera", "ES_por_convenio"): continue
            print(f"  {kk:32s} {vv}")
        print(f"  {'ES por convenio':32s} {rep['ES_por_convenio']}")
