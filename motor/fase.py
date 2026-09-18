"""
Verificacion independiente de N06: la frontera de fase M2=1 del GJR-GARCH y su
no identificabilidad empirica.

Para GJR-GARCH(1,1):  sigma2_t = w + [(a + g*1{z<0}) z^2 + b] sigma2_{t-1}
El coeficiente aleatorio es  A_t = (a + g*1{z<0}) z^2 + b.

  E[A]  = a + g/2 + b                        (persistencia; <1 => estacionariedad debil)
  E[A2] = (a^2 + a g + g^2/2) k_z + 2b(a+g/2) + b^2

M2 := E[A2]. La curtosis poblacional del retorno es finita si y solo si M2 < 1:

  E[s2]  = w/(1-E[A])
  E[s4]  = (w^2 + 2w E[A] E[s2])/(1-M2)
  kurt_r = k_z * E[s4]/E[s2]^2

M2=1 es una frontera de FASE, no de estacionariedad: a ambos lados el proceso es
estacionario y de aspecto identico, pero de un lado la curtosis es finita y del otro
infinita, y con ella el ritmo al que el riesgo agrega con el horizonte.

La pregunta de N06 es si esa frontera se puede localizar con datos.
"""
from __future__ import annotations
import numpy as np

def kappa_z(nu):
    """Curtosis de una t de Student estandarizada a varianza 1."""
    return 3.0 * (nu - 2) / (nu - 4) if nu > 4 else np.inf

def M2(a, g, b, nu):
    kz = kappa_z(nu)
    return (a * a + a * g + g * g / 2) * kz + 2 * b * (a + g / 2) + b * b

def persistencia(a, g, b):
    return a + g / 2 + b

def kurt_poblacional(a, g, b, nu, w=2e-6):
    m2 = M2(a, g, b, nu)
    if m2 >= 1:
        return np.inf
    EA = persistencia(a, g, b)
    Es2 = w / (1 - EA)
    Es4 = (w * w + 2 * w * EA * Es2) / (1 - m2)
    return kappa_z(nu) * Es4 / (Es2 ** 2)

def simular(a, g, b, nu, n, w=2e-6, rng=None, burn=2000):
    rng = rng or np.random.default_rng()
    EA = persistencia(a, g, b)
    s2 = w / max(1e-12, 1 - EA)
    out = np.empty(n)
    for t in range(-burn, n):
        z = rng.standard_t(nu) / np.sqrt(nu / (nu - 2))
        e = np.sqrt(s2) * z
        if t >= 0:
            out[t] = e
        s2 = w + (a + g * (e < 0)) * e * e + b * s2
    return out

def kurt_muestral(x):
    d = x - x.mean()
    m2 = (d * d).mean()
    return (d ** 4).mean() / (m2 * m2)
