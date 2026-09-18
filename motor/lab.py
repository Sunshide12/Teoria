"""
Laboratorio numerico. Herramientas neutras, sin tesis: lo que cualquier ciclo
necesite para comprobar una afirmacion en vez de argumentarla.

Solo numpy/scipy.
"""
from __future__ import annotations
import numpy as np
from scipy import stats

DIAS = 252
RNG = np.random.default_rng(20260918)


def serie_gjr(n, omega=2.0e-6, alpha=.04, gamma=.08, beta=.90, nu=5.0,
              mu=3e-4, p_salto=.004, rng=RNG):
    """Retornos log diarios con clustering, apalancamiento, colas gordas y saltos.
    Los cuatro defectos que el GBM ignora, en un generador que SI los tiene, para
    poder medir cuanto los recupera cada metodo."""
    s2 = omega / max(1e-12, 1 - alpha - gamma / 2 - beta)
    out = np.empty(n)
    for t in range(n):
        z = rng.standard_t(nu) / np.sqrt(nu / (nu - 2))
        eps = np.sqrt(s2) * z
        if rng.random() < p_salto:
            eps += rng.normal(-.03, .05)
        out[t] = mu + eps
        s2 = omega + (alpha + gamma * (eps < 0)) * eps ** 2 + beta * s2
    return out


def bloques_independientes(T_anios, H_anios):
    """Cuantas observaciones REALMENTE independientes del retorno a horizonte H
    caben en T anios. No es T*252: es T/H. Muestrear mas fino no crea bloques."""
    return T_anios / H_anios


def se_mu(sigma, T_anios):
    """Merton 1980. Depende del span, no de la frecuencia."""
    return sigma / np.sqrt(T_anios)


def var_predictiva(sigma, H_anios, T_anios):
    """Varianza del log-retorno acumulado a horizonte H cuando mu se estimo con
    T anios de datos:  Var = sigma^2*H (aleatoria) + H^2*sigma^2/T (epistemica).
    Devuelve (total, aleatoria, epistemica, factor_de_inflacion)."""
    alea = sigma ** 2 * H_anios
    epis = H_anios ** 2 * sigma ** 2 / T_anios
    return alea + epis, alea, epis, np.sqrt(1 + H_anios / T_anios)


def escalamiento(r, horizontes=(1, 5, 20, 60, 120, 250), q=.01, solapado=True):
    """Ajusta  M(H) = c * H^alpha  sobre una medida de cola M a varios horizontes.
    Bajo GBM alpha=1/2 exacto. Se devuelve tambien el n efectivo por horizonte
    para no confundir precision con solapamiento."""
    xs, ys, ns = [], [], []
    for H in horizontes:
        if solapado:
            acc = np.convolve(r, np.ones(H), "valid")
            n_ef = len(r) / H              # bloques realmente independientes
        else:
            m = (len(r) // H) * H
            acc = r[:m].reshape(-1, H).sum(1)
            n_ef = len(acc)
        if len(acc) < 30:
            continue
        cuantil = np.quantile(acc, q)
        es = -acc[acc <= cuantil].mean()
        xs.append(np.log(H)); ys.append(np.log(es)); ns.append(n_ef)
    xs, ys = np.array(xs), np.array(ys)
    A = np.vstack([xs, np.ones_like(xs)]).T
    (alpha, logc), *_ = np.linalg.lstsq(A, ys, rcond=None)
    resid = ys - A @ np.array([alpha, logc])
    dof = max(1, len(xs) - 2)
    se = np.sqrt((resid @ resid / dof) * np.linalg.inv(A.T @ A)[0, 0])
    return {"alpha": float(alpha), "se_alpha": float(se), "c": float(np.exp(logc)),
            "H": list(horizontes)[:len(xs)], "n_efectivo": ns}


def poder_backtest(n_obs, q=.01, alt=2.0):
    """Poder del test de cobertura de Kupiec para detectar que la tasa real de
    excedencias es 'alt' veces la nominal, con n_obs observaciones independientes.
    Responde: cuantos anios hacen falta para poder falsar una afirmacion de cola."""
    p0, p1 = q, min(q * alt, .5)
    k = np.arange(0, n_obs + 1)
    ll0 = k * np.log(p0) + (n_obs - k) * np.log1p(-p0)
    ph = np.clip(k / n_obs, 1e-12, 1 - 1e-12)
    ll1 = k * np.log(ph) + (n_obs - k) * np.log1p(-ph)
    lr = 2 * (ll1 - ll0)
    rechaza = lr > stats.chi2.ppf(.95, 1)
    return float(stats.binom.pmf(k, n_obs, p1)[rechaza].sum())


def max_drawdown(paths):
    return (paths / np.maximum.accumulate(paths, axis=1) - 1).min(axis=1)
