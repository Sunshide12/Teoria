# Análisis: reel de Monte Carlo sobre fondos de inversión + modelo realista

Contexto para retomar en Claude Code. Resume todo lo discutido: análisis del video/comentarios, transcripción real, y el motor de simulación Monte Carlo mejorado (con código).

---

## 1. Origen

Reel de IG (autor "intitnet", cuenta de finanzas/marketing) sobre simulación de Monte Carlo aplicada a fondos de inversión. Se analizó a partir de capturas de pantalla (video + comentarios) y luego con la transcripción real obtenida vía Inkr.

## 2. Transcripción real del video

> [00:00] Esa nube de líneas grises que ves en la imagen no es puro adorno, es una simulación de Monte Carlo, un método que en vez de intentar adivinar un solo futuro, corre cientos o miles de futuros posibles al mismo tiempo, cada uno con un poco de aleatoriedad metida a propósito, para ver qué tan probable es cada resultado. La línea negra del medio es el drift, la tendencia promedio esperada, la banda roja marca donde cae el 90% de los escenarios simulados, y la banda azul el 98%, o sea que casi todos los caminos posibles quedan atrapados ahí adentro.
>
> [00:25] Esto es exactamente lo que hacen por dentro los fondos de inversión y los fondos buitre para justificar sus comisiones absurdas, corren miles de simulaciones de un activo, calculan probabilidades, y con eso arman un discurso de gestión experta, que en la práctica, según los informes SPIVA, hace que el 60% de los fondos activos en Estados Unidos ni siquiera le gane al simple S&P 500 en un año normal, y casi el 90% pierde contra el índice a 15 años.
>
> [00:46] La buena noticia es que este mismo método ya no es secreto de nadie, con Python hasta con Excel, cualquiera puede correr su propia simulación de Monte Carlo sobre una acción o un portafolio, ver el rango probable de resultados, y tomar una decisión informada sin pagarle una comisión anual a alguien que, estadísticamente, probablemente le va a ir peor que a un algoritmo simple.
>
> [01:02] Y ya que hablamos de simular miles de escenarios, la única simulación segura es que te vas a ver bien con Intinet, sin necesidad de intervalo de confianza. *(cierre publicitario)*

Nota: la transcripción automática decía "informes Espiba" (= **SPIVA**, S&P Indices Versus Active) y "País Ano" (= **Python**); corregido arriba.

## 3. Veredicto sobre el video

**Acierta:**
- Explicación técnica del gráfico correcta: drift = tendencia media, banda roja = percentiles 5-95 (90% de las simulaciones), banda azul = percentiles 1-99.
- Datos de SPIVA verificados y correctos: a 15 años (cierre 2024) el 89,50% de los fondos large-cap activos en EE.UU. quedó por debajo del S&P 500. En 2024 el 65% underperformed (no 60% como dice el video, pero cercano); en 2025 subió a 79%.

**Falla:**
- **Salto lógico central**: si el 90% de los profesionales pierde contra el índice, la conclusión correcta es "indexa y no hagas nada", no "hazlo tú mismo en Excel". El video usa el dato para vender justo lo contrario de lo que el dato recomienda.
- **Monte Carlo no predice, propaga supuestos**: el cono depende enteramente de μ (drift) y σ que tú metes. μ es casi inestimable (ver sección de incertidumbre abajo).
- **"Casi todos los caminos quedan atrapados ahí" es engañoso**: eso es cierto solo dentro del modelo (GBM = log-normal, vol constante, sin saltos). Los mercados reales tienen colas gordas, clustering de volatilidad y crashes que el GBM subestima sistemáticamente.
- **"Fondos buitre" es un error de categoría**: son fondos de deuda distressed, no tienen que ver con los fondos activos de renta variable que mide SPIVA.
- **Es un anuncio**: el cierre revela que todo el arco (indignación → "hazlo tú" → producto) estaba construido para vender "Intinet".

## 4. Análisis de los comentarios

| Comentario / autor | Categoría | Nota |
|---|---|---|
| "90% pierde en bolsa, 99% para 2030" (exeevil.ok) | Media verdad | El ~90% real viene de day trading/CFDs apalancados (ESMA: 74-89%), no de "la bolsa". La cifra de 2030 está inventada. Además: el video habla de fondos activos vs índice, no de "la gente pierde en bolsa" — son estadísticas distintas que comparten número por casualidad. |
| "el sistema siempre fue manipulado" (balatro_balatrez23) | Conspiración | Infalsificable. |
| Nvidia/Lockheed/Tesla "demasiado grandes para caer" (joserkysnthz) | Error técnico | Tesla no fue "rescatada" (préstamo DOE 2010, devuelto en 2013). "Too big to fail" ≠ "la acción no puede caer" — Nvidia ya cayó >50% varias veces. |
| "sistemas cazan stop loss, todo manipulado desde arriba" (exeevil.ok) | Media verdad | Los barridos de liquidez existen y son reales, pero la explicación suficiente es spread + comisión + apalancamiento + slippage + varianza, sin necesidad de conspiración. |
| "las noticias son el plan para ponerse corto" | Conspiración | Infalsificable. |
| Meme "MONTE CARLO METHODS BE LIKE: RANDOM BULLSHIT GO!!!!" (luis.espinoza.j) | Chiste | El comentario más lúcido del hilo: resume bien que el modelo solo devuelve ruido estructurado alrededor de tu propio supuesto. |
| "tremendo comercial me comí" (erizo_boy_mma2) | Acertado | Correcto: todo el video es un anuncio disfrazado. |

## 5. El gráfico, línea por línea

- **Gris tenue**: cada trayectoria simulada individual.
- **Negra ("drift")**: tendencia media esperada = el parámetro μ metido a mano, no una predicción.
- **Roja (banda 90%)**: percentiles 5-95 de las simulaciones.
- **Azul (banda 98%)**: percentiles 1-99, por eso va por fuera de la roja.

Errores comunes al leerlo:
1. No son soporte/resistencia — son cuantiles del conjunto simulado.
2. El cono se abre con √t, no linealmente.
3. Hay más espacio arriba que abajo por ser lognormal (precio no puede bajar de 0, no tiene techo arriba) → la mediana queda por debajo de la media.

Con los parámetros implícitos en la captura (drift ~50-55% anual, σ~17%) la probabilidad de terminar en verde es >99%, pero es circular: es lo que el autor metió, no un hallazgo. Con parámetros realistas de un índice amplio (μ≈8-9%, σ≈18%): ~65-70% a 1 año, ~85-90% a 10 años, ~95%+ a 20 años — eso es invertir. El trading intradía apalancado es otro juego, con esperanza negativa por costes, y ahí sí aplica el 90% que citaban los comentarios.

## 6. Por qué el GBM del video subestima el riesgo — y cómo arreglarlo

El modelo del video es un **Movimiento Browniano Geométrico (GBM)**:
```
dS/S = μ dt + σ dW      (log-normal, vol constante, sin saltos)
```
Tiene cuatro defectos conocidos, cada uno con arreglo distinto:

### Nivel 1 — Saltos (Merton 1976)
```
dS/S = (μ − λk)dt + σ dW + (J−1)dN
N ~ Poisson(λ), ln J ~ N(μⱼ, σⱼ²), k = E[J−1] = e^(μⱼ+σⱼ²/2) − 1
```
Captura noticias/crashes discretos, pero se diluye con √t por el TCL: a horizontes largos vuelve a parecer normal.

### Nivel 2 — Volatilidad estocástica (Heston 1993)
```
dS = μS dt + √v · S dW₁
dv = κ(θ − v)dt + ξ√v dW₂ ,  corr(dW₁,dW₂) = ρ
```
ρ < 0 (~−0.7) reproduce el efecto apalancamiento: la vol sube cuando el precio cae. Genera la asimetría real. No se diluye con el tiempo (persistente). Condición de Feller: 2κθ > ξ².

### Nivel 3 — Bates / SVJ
Heston + Merton combinados. Estándar en pricing de opciones.

### Nivel 4 — GJR-GARCH-t + Filtered Historical Simulation (el mejor, no paramétrico)
```
σ²ₜ = ω + (α + γ·1{εₜ₋₁<0})·ε²ₜ₋₁ + β·σ²ₜ₋₁     (γ>0 = efecto apalancamiento)
zₜ = εₜ/σₜ    (residuos estandarizados, t de Student con ν grados)
```
Se ajusta por máxima verosimilitud y se **re-muestrean los residuos empíricos z** en vez de asumir una distribución. Barone-Adesi et al. (1999).

### Nivel 5 — Teoría de Valores Extremos (EVT) para lo no observado
Pickands–Balkema–de Haan: los excesos sobre un umbral alto convergen a una Pareto generalizada:
```
P(X − u > y | X > u) = (1 + ξy/β)^(−1/ξ)
```
ξ > 0 = cola de potencia. Se empalma cuerpo empírico + colas GPD para poder simular un shock peor que cualquiera observado en la muestra.

### El problema que ningún modelo arregla: incertidumbre de μ
Error estándar de μ ≈ σ/√(T en años). Con σ=20% y 20 años de datos: ±9% al 95% (Merton, 1980). Esto importa según el horizonte:
- A 1 año: ensancha la banda del 98% ~1% (irrelevante).
- A 10 años: la ensancha ~65% (dominante).

### Métricas que sí importan (dejar de mirar la banda del 90%)
- **Expected Shortfall / CVaR** (media de la cola, no un cuantil — Basilea III reemplazó VaR por ES en 2016 por esto).
- **Distribución del máximo drawdown**, no solo el valor final.
- **Probabilidad de ruina** (P(drawdown > X%)).

### Resultados obtenidos (datos sintéticos con clustering/asimetría/colas/saltos, horizonte 1 año, 40k trayectorias)

| Modelo | Mediana | P(pérdida) | VaR 99% | ES 99% | DD p95 | P(DD>50%) |
|---|---|---|---|---|---|---|
| 1. GBM (el del video) | 1.4% | 46.7% | 31.7% | 35.4% | −30.0% | 0.01% |
| 2. Bates (Heston+saltos) | 4.2% | 41.5% | 45.1% | 52.2% | −40.1% | 1.40% |
| 3. GARCH-FHS + EVT | 5.3% | 39.2% | 52.5% | **65.9%** | −44.2% | **3.26%** |
| 4. (3) + incertidumbre de μ | 5.0% | 40.4% | 52.0% | 64.9% | −44.3% | 3.19% |

**El GBM subestima la pérdida esperada en cola casi a la mitad, y la probabilidad de un drawdown del 50% por un factor de ~300.**

Siguiente paso natural si se pasa a multiactivo: **cópula t** en vez de gaussiana — la gaussiana tiene dependencia de cola exactamente cero (asume que en un crash las correlaciones no se van a 1), que es justo lo que falló con la fórmula de Li en 2008.

## 7. Código completo (`montecarlo_realista.py`)

Requiere solo `numpy` y `scipy`. Uso: `python montecarlo_realista.py [retornos.csv]` (sin argumento usa datos sintéticos de demo).

```python
"""
Monte Carlo realista: colas gordas, volatilidad estocástica, saltos y EVT.

Tres motores, de peor a mejor:
  1. GBM              - el del video. Baseline para comparar.
  2. Bates (SVJ)      - Heston + saltos de Merton. Parametrico.
  3. GJR-GARCH-t+FHS  - filtrado + bootstrap de residuos. Sin asumir distribucion.
     (+ opcion EVT: empalma colas Pareto generalizada mas alla de la muestra)

Extra: propagacion de la incertidumbre de mu, que suele dominar todo lo demas.

Uso:
    python montecarlo_realista.py                      # demo con datos sinteticos
    python montecarlo_realista.py retornos.csv         # CSV con columna de retornos

Solo requiere numpy y scipy.
"""

from __future__ import annotations

import sys
import numpy as np
from scipy import optimize, special, stats

RNG = np.random.default_rng(42)
TRADING_DAYS = 252


# ---------------------------------------------------------------------------
# 0. Datos
# ---------------------------------------------------------------------------

def synthetic_returns(n: int = 3000, seed: int = 7) -> np.ndarray:
    """Retornos log diarios con clustering, asimetria, colas gordas y saltos.

    No es un mercado real, pero tiene los cuatro defectos que el GBM ignora,
    asi que sirve para ver si cada motor los recupera.
    """
    rng = np.random.default_rng(seed)
    omega, alpha, gamma, beta, nu = 2.0e-6, 0.04, 0.08, 0.90, 5.0
    s2 = omega / max(1e-12, 1 - alpha - gamma / 2 - beta)
    out = np.empty(n)
    for t in range(n):
        z = rng.standard_t(nu) / np.sqrt(nu / (nu - 2))
        eps = np.sqrt(s2) * z
        if rng.random() < 0.004:                       # salto ~1 vez al año
            eps += rng.normal(-0.03, 0.05)
        out[t] = 0.0003 + eps
        s2 = omega + (alpha + gamma * (eps < 0)) * eps ** 2 + beta * s2
    return out


def load_returns(path: str | None) -> np.ndarray:
    if path is None:
        return synthetic_returns()
    raw = np.genfromtxt(path, delimiter=",", skip_header=1)
    col = raw if raw.ndim == 1 else raw[:, -1]
    col = col[np.isfinite(col)]
    # Si parecen precios en vez de retornos, los convierte.
    if np.nanmedian(np.abs(col)) > 0.5:
        col = np.diff(np.log(col))
    return col


# ---------------------------------------------------------------------------
# 1. GBM  (el modelo del video)
# ---------------------------------------------------------------------------

def simulate_gbm(s0, mu, sigma, horizon, n_paths, rng=RNG):
    """dS/S = mu dt + sigma dW.  Log-normal, vol constante, sin saltos."""
    dt = 1.0 / TRADING_DAYS
    drift = (mu - 0.5 * sigma ** 2) * dt
    shock = sigma * np.sqrt(dt) * rng.standard_normal((n_paths, horizon))
    return s0 * np.exp(np.cumsum(drift + shock, axis=1))


# ---------------------------------------------------------------------------
# 2. Bates / SVJ  =  Heston + saltos de Merton
# ---------------------------------------------------------------------------

def simulate_bates(s0, mu, v0, kappa, theta, xi, rho,
                   lam, mu_j, sigma_j, horizon, n_paths, rng=RNG):
    """
    dS/S = (mu - lam*k) dt + sqrt(v) dW1 + (J-1) dN      N ~ Poisson(lam)
    dv   = kappa (theta - v) dt + xi sqrt(v) dW2         corr(dW1,dW2) = rho
    ln J ~ N(mu_j, sigma_j^2)   ,   k = E[J-1] = exp(mu_j + sigma_j^2/2) - 1

    rho < 0 reproduce el efecto apalancamiento (la vol sube cuando el precio cae),
    que es lo que genera la asimetria real de la distribucion.
    Euler con truncamiento total en v para que no se vuelva negativa.
    """
    dt = 1.0 / TRADING_DAYS
    k = np.exp(mu_j + 0.5 * sigma_j ** 2) - 1.0
    log_s = np.full(n_paths, np.log(s0))
    v = np.full(n_paths, v0)
    out = np.empty((n_paths, horizon))

    for t in range(horizon):
        z1 = rng.standard_normal(n_paths)
        z2 = rho * z1 + np.sqrt(1 - rho ** 2) * rng.standard_normal(n_paths)
        v_pos = np.maximum(v, 0.0)
        sq = np.sqrt(v_pos)

        n_jumps = rng.poisson(lam * dt, n_paths)
        jump = np.where(
            n_jumps > 0,
            rng.normal(mu_j * n_jumps, sigma_j * np.sqrt(np.maximum(n_jumps, 1))),
            0.0,
        )

        log_s += (mu - lam * k - 0.5 * v_pos) * dt + sq * np.sqrt(dt) * z1 + jump
        v = v + kappa * (theta - v_pos) * dt + xi * sq * np.sqrt(dt) * z2
        out[:, t] = log_s

    return np.exp(out)


# ---------------------------------------------------------------------------
# 3. GJR-GARCH(1,1) con innovaciones t de Student
# ---------------------------------------------------------------------------

def _std_t_logpdf(z, nu):
    """log densidad de una t estandarizada a varianza 1."""
    c = (special.gammaln((nu + 1) / 2) - special.gammaln(nu / 2)
         - 0.5 * np.log(np.pi * (nu - 2)))
    return c - 0.5 * (nu + 1) * np.log1p(z ** 2 / (nu - 2))


def _garch_recursion(r, omega, alpha, gamma, beta):
    T = r.size
    s2 = np.empty(T)
    s2[0] = np.var(r)
    for t in range(1, T):
        e = r[t - 1]
        s2[t] = omega + (alpha + gamma * (e < 0.0)) * e * e + beta * s2[t - 1]
    return s2


def fit_gjr_garch_t(r: np.ndarray) -> dict:
    """
    sigma^2_t = omega + (alpha + gamma*1{eps_{t-1}<0}) eps^2_{t-1} + beta sigma^2_{t-1}
    eps_t = sigma_t * z_t ,  z_t ~ t_nu estandarizada

    gamma > 0  ->  efecto apalancamiento (las caidas generan mas vol que las subidas)
    nu bajo    ->  colas gordas incluso despues de filtrar la vol
    """
    mu_hat = r.mean()
    eps = r - mu_hat

    def nll(p):
        omega, alpha, gamma, beta, nu = p
        if alpha + gamma / 2 + beta >= 0.999:
            return 1e10
        s2 = _garch_recursion(eps, omega, alpha, gamma, beta)
        if not np.all(np.isfinite(s2)) or np.any(s2 <= 0):
            return 1e10
        z = eps / np.sqrt(s2)
        return -np.sum(_std_t_logpdf(z, nu) - 0.5 * np.log(s2))

    v = np.var(eps)
    x0 = [v * 0.02, 0.03, 0.06, 0.90, 6.0]
    bounds = [(1e-12, v), (0.0, 0.3), (0.0, 0.5), (0.4, 0.999), (2.1, 40.0)]
    res = optimize.minimize(nll, x0, method="L-BFGS-B", bounds=bounds)

    omega, alpha, gamma, beta, nu = res.x
    s2 = _garch_recursion(eps, omega, alpha, gamma, beta)
    return {
        "mu": mu_hat, "omega": omega, "alpha": alpha, "gamma": gamma,
        "beta": beta, "nu": nu,
        "sigma2": s2,
        "z": eps / np.sqrt(s2),               # residuos estandarizados
        "persistence": alpha + gamma / 2 + beta,
        "loglik": -res.fun,
    }


# ---------------------------------------------------------------------------
# 4. EVT: cola de Pareto generalizada (Peaks Over Threshold)
# ---------------------------------------------------------------------------

def fit_gpd_tail(x: np.ndarray, q: float = 0.95) -> dict:
    """
    Pickands-Balkema-de Haan: los excesos sobre un umbral alto u convergen a

        P(X - u > y | X > u) = (1 + xi*y/beta)^(-1/xi)

    xi > 0  ->  cola pesada de tipo potencia. Para perdidas diarias de renta
    variable suele salir xi ~ 0.2-0.35, o sea momentos de orden > 1/xi infinitos.
    """
    u = np.quantile(x, q)
    exc = x[x > u] - u
    xi, _, beta = stats.genpareto.fit(exc, floc=0.0)
    return {"u": u, "xi": xi, "beta": beta, "p": 1.0 - q, "n_exc": exc.size}


def make_spliced_sampler(z: np.ndarray, q: float = 0.95):
    """Cuerpo empirico + dos colas GPD. Permite generar shocks PEOR que
    cualquiera observado, que es justo lo que el bootstrap puro no puede hacer."""
    right = fit_gpd_tail(z, q)
    left = fit_gpd_tail(-z, q)
    body = z[(z <= right["u"]) & (-z <= left["u"])]

    def sample(size, rng=RNG):
        out = np.empty(size)
        u01 = rng.random(size)
        p = right["p"]
        m_r, m_l = u01 < p, u01 > 1 - p
        m_b = ~(m_r | m_l)
        out[m_b] = rng.choice(body, m_b.sum(), replace=True)
        if m_r.any():
            out[m_r] = right["u"] + stats.genpareto.rvs(
                right["xi"], scale=right["beta"], size=m_r.sum(),
                random_state=rng.integers(1 << 31))
        if m_l.any():
            out[m_l] = -(left["u"] + stats.genpareto.rvs(
                left["xi"], scale=left["beta"], size=m_l.sum(),
                random_state=rng.integers(1 << 31)))
        return out

    return sample, {"xi_izq": left["xi"], "xi_der": right["xi"]}


# ---------------------------------------------------------------------------
# 5. Filtered Historical Simulation
# ---------------------------------------------------------------------------

def simulate_fhs(s0, fit, horizon, n_paths, mu_annual=None,
                 use_evt=True, mu_sd=0.0, rng=RNG):
    """
    Barone-Adesi et al. (1999). Se filtra la serie con el GARCH, se guardan los
    residuos estandarizados z, y se simula re-muestreandolos. La distribucion de
    los shocks es la empirica: no se asume normal, ni t, ni nada.

    mu_sd > 0 -> cada trayectoria usa su propio mu sacado de la distribucion de
    incertidumbre del estimador. Esto es lo que casi nadie hace y lo que mas
    ensancha el cono (con razon).
    """
    if use_evt:
        sampler, tail_info = make_spliced_sampler(fit["z"])
    else:
        zs = fit["z"]
        sampler = lambda size, rng=rng: rng.choice(zs, size, replace=True)
        tail_info = {}

    mu_d = fit["mu"] if mu_annual is None else mu_annual / TRADING_DAYS
    mu_path = mu_d + (rng.normal(0, mu_sd / TRADING_DAYS, n_paths)
                      if mu_sd > 0 else 0.0)
    mu_path = np.broadcast_to(np.atleast_1d(mu_path), (n_paths,))

    omega, alpha, gamma, beta = (fit[k] for k in ("omega", "alpha", "gamma", "beta"))
    s2 = np.full(n_paths, fit["sigma2"][-1])
    eps_prev = np.full(n_paths, fit["z"][-1] * np.sqrt(fit["sigma2"][-1]))
    log_s = np.full(n_paths, np.log(s0))
    out = np.empty((n_paths, horizon))

    for t in range(horizon):
        s2 = omega + (alpha + gamma * (eps_prev < 0)) * eps_prev ** 2 + beta * s2
        eps_prev = np.sqrt(s2) * sampler(n_paths, rng)
        log_s += mu_path + eps_prev
        out[:, t] = log_s

    return np.exp(out), tail_info


# ---------------------------------------------------------------------------
# 6. Metricas de riesgo (dejar de mirar la banda del 90%)
# ---------------------------------------------------------------------------

def max_drawdown(paths: np.ndarray) -> np.ndarray:
    peak = np.maximum.accumulate(paths, axis=1)
    return (paths / peak - 1.0).min(axis=1)


def risk_report(paths: np.ndarray, s0: float, label: str) -> dict:
    final = paths[:, -1]
    ret = final / s0 - 1.0
    dd = max_drawdown(paths)
    q01 = np.quantile(ret, 0.01)
    return {
        "modelo": label,
        "mediana": np.median(ret),
        "media": ret.mean(),
        "p_perdida": (ret < 0).mean(),
        "VaR_99": -q01,
        "ES_99": -ret[ret <= q01].mean(),          # CVaR: la media DE la cola
        "p1_banda98": np.quantile(final, 0.01),
        "p99_banda98": np.quantile(final, 0.99),
        "DD_mediano": np.median(dd),
        "DD_p95": np.quantile(dd, 0.05),
        "p_ruina_50": (dd < -0.50).mean(),
    }


def print_table(rows):
    hdr = (f"{'modelo':<26}{'mediana':>9}{'P(perd)':>9}{'VaR99':>8}"
           f"{'ES99':>8}{'DD p95':>9}{'P(DD>50%)':>11}")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['modelo']:<26}{r['mediana']:>8.1%}{r['p_perdida']:>9.1%}"
              f"{r['VaR_99']:>8.1%}{r['ES_99']:>8.1%}"
              f"{r['DD_p95']:>9.1%}{r['p_ruina_50']:>11.2%}")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def main(path=None, horizon=TRADING_DAYS, n_paths=40_000, s0=100.0):
    r = load_returns(path)
    print(f"\nObservaciones: {r.size}   "
          f"vol anual: {r.std() * np.sqrt(TRADING_DAYS):.1%}   "
          f"asimetria: {stats.skew(r):+.2f}   "
          f"curtosis exc.: {stats.kurtosis(r):.2f}   (normal = 0)\n")

    fit = fit_gjr_garch_t(r)
    print(f"GJR-GARCH-t:  alpha={fit['alpha']:.3f}  gamma={fit['gamma']:.3f}"
          f"  beta={fit['beta']:.3f}  nu={fit['nu']:.1f}"
          f"  persistencia={fit['persistence']:.3f}")
    print(f"  gamma>0 => efecto apalancamiento | nu<10 => colas gordas tras filtrar")

    mu = fit["mu"] * TRADING_DAYS
    sigma = r.std() * np.sqrt(TRADING_DAYS)
    # error estandar del estimador de mu: sigma/sqrt(T_años). El problema real.
    mu_se = sigma / np.sqrt(r.size / TRADING_DAYS)
    print(f"\nmu estimado = {mu:+.1%} anual  con error estandar {mu_se:.1%}"
          f"  -> IC95% = [{mu - 1.96 * mu_se:+.1%}, {mu + 1.96 * mu_se:+.1%}]")
    print("  Ese intervalo es el verdadero limite del metodo, no el modelo.\n")

    rows = [
        risk_report(simulate_gbm(s0, mu, sigma, horizon, n_paths),
                    s0, "1. GBM (el del video)"),
        risk_report(simulate_bates(s0, mu, sigma ** 2, 3.0, sigma ** 2,
                                   0.45, -0.75, 1.2, -0.05, 0.08,
                                   horizon, n_paths),
                    s0, "2. Bates (Heston+saltos)"),
    ]
    p_fhs, tail = simulate_fhs(s0, fit, horizon, n_paths, mu_annual=mu, use_evt=True)
    rows.append(risk_report(p_fhs, s0, "3. GARCH-FHS + EVT"))
    p_unc, _ = simulate_fhs(s0, fit, horizon, n_paths, mu_annual=mu,
                            use_evt=True, mu_sd=mu_se)
    rows.append(risk_report(p_unc, s0, "4. 3 + incert. de mu"))

    print_table(rows)
    print(f"\nIndice de cola GPD:  xi_izq={tail['xi_izq']:+.3f}"
          f"  xi_der={tail['xi_der']:+.3f}   (xi>0 = cola de potencia)")
    print("\nLee ES99 y DD, no la banda del 90%.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
```

## 8. Skill creada

Se generó también una skill reutilizable `analisis-video-social` (formato `.skill`) para analizar videos de redes sociales + comentarios en futuras conversaciones: obtiene o reconstruye transcrito, extrae afirmaciones, las verifica, clasifica comentarios (aporte real / media verdad / conspiración / error técnico / ruido) y cierra con veredicto. Entregada aparte como archivo descargable.
