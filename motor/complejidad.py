"""
El experimento de la complejidad optima frente al horizonte.

Hipotesis (propia del orquestador, ciclo 2): la complejidad de modelo que
minimiza el error en una medida de riesgo a horizonte H es DECRECIENTE en H.

Razon: el error de especificacion (sesgo) baja al anadir parametros, pero el
error de estimacion se amplifica con el horizonte, porque la sensibilidad de la
medida de riesgo a cada parametro crece con H (dPsi_H/dtheta_k ~ H^a_k), mientras
que la precision de cada parametro esta fija por T. Mas parametros = mas canales
por los que el horizonte amplifica ruido.

Si es cierto, hay un optimo interior d*(H,T) decreciente, y usar el modelo mas
sofisticado para el estres a 10 anos es exactamente lo contrario de lo correcto.

Se contrasta con cuatro modelos de complejidad creciente ajustados al MISMO dato
y evaluados contra la verdad conocida (el DGP se conoce porque lo generamos).
"""
from __future__ import annotations
import numpy as np
from scipy import optimize, special, stats

DIAS = 252

# --------------------------------------------------------------------------
# DGP verdadero: GJR-GARCH-t con saltos. Rico a proposito.
# --------------------------------------------------------------------------
DGP = dict(omega=1.6e-6, alpha=.03, gamma=.09, beta=.90, nu=7.0,
           mu=2.5e-4, lam=.004, mj=-.03, sj=.05)

def _sim_dgp(n_paths, n_steps, rng, p=DGP, s2_0=None, eps_0=None, devolver_estado=False):
    """Simulacion vectorizada sobre trayectorias. Devuelve log-retornos (n_paths,n_steps)."""
    o,a,g,b,nu,mu,lam,mj,sj = (p[k] for k in
        ("omega","alpha","gamma","beta","nu","mu","lam","mj","sj"))
    s2 = np.full(n_paths, s2_0 if s2_0 is not None else o/max(1e-12,1-a-g/2-b))
    eps_prev = np.zeros(n_paths) if eps_0 is None else np.full(n_paths, eps_0)
    out = np.empty((n_paths, n_steps))
    sc = np.sqrt(nu/(nu-2))
    for t in range(n_steps):
        s2 = o + (a + g*(eps_prev < 0))*eps_prev**2 + b*s2
        z = rng.standard_t(nu, n_paths)/sc
        eps = np.sqrt(s2)*z
        nj = rng.poisson(lam, n_paths)
        eps = eps + np.where(nj > 0, rng.normal(mj*nj, sj*np.sqrt(np.maximum(nj,1))), 0.)
        out[:, t] = mu + eps
        eps_prev = eps
    return (out, s2, eps_prev) if devolver_estado else out

# --------------------------------------------------------------------------
# Ajuste: cuatro modelos de complejidad creciente
# --------------------------------------------------------------------------
def _std_t_logpdf(z, nu):
    c = (special.gammaln((nu+1)/2)-special.gammaln(nu/2)-.5*np.log(np.pi*(nu-2)))
    return c - .5*(nu+1)*np.log1p(z**2/(nu-2))

def _rec(e, o, a, g, b):
    T = e.size; s2 = np.empty(T); s2[0] = np.var(e)
    for t in range(1, T):
        x = e[t-1]; s2[t] = o + (a + g*(x < 0))*x*x + b*s2[t-1]
    return s2

def _fit_garch(r, leverage, student):
    """GARCH(1,1) o GJR, con innovacion normal o t. Devuelve dict de parametros."""
    mu = r.mean(); e = r - mu; v = np.var(e)
    def nll(p):
        o, a, g, b, nu = p
        if not leverage: g = 0.0
        if a + g/2 + b >= .9995 or o <= 0: return 1e10
        s2 = _rec(e, o, a, g, b)
        if not np.all(np.isfinite(s2)) or np.any(s2 <= 0): return 1e10
        z = e/np.sqrt(s2)
        ll = (_std_t_logpdf(z, nu) if student else -.5*(np.log(2*np.pi)+z*z))
        return -np.sum(ll - .5*np.log(s2))
    bnd = [(1e-12, v), (0, .3), (0, .5) if leverage else (0, 1e-9),
           (.4, .9994), (4.2, 40.) if student else (1e6, 1e6+1)]
    x0 = [v*.03, .03, .06 if leverage else 0., .90, 8. if student else 1e6]
    res = optimize.minimize(nll, x0, method="L-BFGS-B", bounds=bnd)
    o, a, g, b, nu = res.x
    s2 = _rec(e, o, a, g, b)
    return dict(mu=mu, omega=o, alpha=a, gamma=g, beta=b, nu=nu,
                s2_last=s2[-1], e_last=e[-1], z=e/np.sqrt(s2), student=student)

def _gpd_sampler(z, q=.95, rng=None):
    """Cuerpo empirico + colas GPD (EVT). Permite shocks peores que los observados."""
    def tail(x):
        u = np.quantile(x, q); exc = x[x > u] - u
        xi, _, be = stats.genpareto.fit(exc, floc=0.)
        return u, xi, be
    ur, xr, br = tail(z); ul, xl, bl = tail(-z)
    body = z[(z <= ur) & (-z <= ul)]
    p = 1 - q
    def sample(size, rng):
        out = np.empty(size); u01 = rng.random(size)
        mr, ml = u01 < p, u01 > 1-p; mb = ~(mr | ml)
        out[mb] = rng.choice(body, mb.sum(), replace=True)
        if mr.any(): out[mr] = ur + stats.genpareto.rvs(xr, scale=br, size=mr.sum(),
                                                        random_state=rng.integers(1<<31))
        if ml.any(): out[ml] = -(ul + stats.genpareto.rvs(xl, scale=bl, size=ml.sum(),
                                                          random_state=rng.integers(1<<31)))
        return out
    return sample

# --------------------------------------------------------------------------
# Proyeccion de cada modelo a horizonte H
# --------------------------------------------------------------------------
def _proj_gbm(r, H, n, rng):
    mu = r.mean(); sg = r.std()
    return mu*H + sg*np.sqrt(H)*rng.standard_normal(n)

def _proj_garch(f, H, n, rng, sampler=None):
    o,a,g,b,nu = (f[k] for k in ("omega","alpha","gamma","beta","nu"))
    s2 = np.full(n, f["s2_last"]); ep = np.full(n, f["e_last"])
    acc = np.zeros(n); sc = np.sqrt(nu/(nu-2)) if f["student"] else 1.
    for t in range(H):
        s2 = o + (a + g*(ep < 0))*ep**2 + b*s2
        z = (sampler(n, rng) if sampler is not None else
             (rng.standard_t(nu, n)/sc if f["student"] else rng.standard_normal(n)))
        ep = np.sqrt(s2)*z
        acc += f["mu"] + ep
    return acc

def es99(x, q=.01):
    c = np.quantile(x, q)
    return float(-x[x <= c].mean())

MODELOS = ["1. GBM (2p)", "2. GARCH-N (4p)", "3. GJR-GARCH-t (6p)", "4. GJR-t+EVT (8p)"]

def estimar_todos(r, H, n_paths, rng):
    out = {}
    out[MODELOS[0]] = es99(_proj_gbm(r, H, n_paths, rng))
    f2 = _fit_garch(r, leverage=False, student=False)
    out[MODELOS[1]] = es99(_proj_garch(f2, H, n_paths, rng))
    f3 = _fit_garch(r, leverage=True, student=True)
    out[MODELOS[2]] = es99(_proj_garch(f3, H, n_paths, rng))
    out[MODELOS[3]] = es99(_proj_garch(f3, H, n_paths, rng, sampler=_gpd_sampler(f3["z"])))
    return out
