# N74 — El capital libre de dato, medido

Verificación propia de la conjetura de ortogonalidad que dejó el adversarial del ciclo 5.

**Diseño.** 100 años simulados con el nivel de volatilidad a la deriva (caso no estacionario,
que es el realista según N60/N62). Se calcula el ES99 según `ES = −μH + σ√H·k` con
`k = φ(z_α)/(1−α) = 2,665`, variando dos cosas que **ningún dato fija**:

- la **ventana de estimación** T\* ∈ {2, 5, 10, 20, 30, 50} años — no identificable (N60)
- la **deriva declarada** μ ∈ {0%, 2%, 4%, 6%, 8%} — no estimable en menos de 400 años (N01, N73)

Ambos rangos son conservadores: son las elecciones que un profesional defendería sin
pestañear.

## ES99 a 1 año

| T\* | μ=0% | μ=2% | μ=4% | μ=6% | μ=8% |
|---|---|---|---|---|---|
| 2 a | 0,215 | 0,195 | 0,175 | 0,155 | 0,135 |
| 5 a | 0,245 | 0,225 | 0,205 | 0,185 | 0,165 |
| 10 a | 0,324 | 0,304 | 0,284 | 0,264 | 0,244 |
| 20 a | 0,375 | 0,355 | 0,335 | 0,315 | 0,295 |
| 30 a | 0,396 | 0,376 | 0,356 | 0,336 | 0,316 |
| 50 a | 0,457 | 0,437 | 0,417 | 0,397 | 0,377 |

| | rango |
|---|---|
| por ventana, a μ fijo | **2,13× – 2,79×** |
| por μ, a ventana fija | **1,21× – 1,59×** |
| **total** | **3,39×** |
| producto de los medios | 3,28× |

**Los dos grados de libertad son ortogonales**: el rango total coincide con el producto de
los rangos individuales, con un 3% de discrepancia.

> **Un factor de 3,4 en el capital regulatorio a un año no está fijado por ningún dato.**
> Está fijado por dos elecciones de convención que nadie declara como tales.

Para comparar: la frontera de fase que persiguieron cuatro ciclos mueve **1,011×**.

## ES99 a 10 años: el signo tampoco está determinado

| T\* | μ=0% | μ=4% | μ=8% |
|---|---|---|---|
| 2 a | 0,680 | 0,280 | **−0,120** |
| 10 a | 1,024 | 0,624 | 0,224 |
| 50 a | **1,444** | 1,044 | 0,644 |

El ES99 va de **−0,120 a +1,444**. Los cocientes no significan nada aquí porque el número
cruza el cero, y ese cruce es el resultado:

> A diez años, **no está determinado si existe pérdida en el 1% peor de los casos.** Con una
> ventana corta y una prima de riesgo del 8% declarada, el percentil 1 de la distribución a
> diez años es una **ganancia**. Con ventana larga y deriva cero, es una pérdida del 76% del
> valor.

Las dos configuraciones son defendibles con los mismos datos. Ninguna es refutable en menos
de 400 años (N01: fijar μ a ±1%/año exige ese span **a cualquier frecuencia de muestreo**).

## Lo que esto cierra

Confirma N73 por una ruta independiente. El adversarial lo derivó del intervalo de confianza
de μ̂ con T=10 años; aquí sale de barrer convenciones defendibles sobre una trayectoria
simulada. Mismo resultado: **el signo del ES a horizonte regulatorio no está determinado.**

Y confirma la ortogonalidad, que era la parte conjetural: el capital libre de dato es el
**producto** de las cuotas, no la mayor de ellas.

## Caveat

El rango de μ (0–8%) y el de ventana (2–50 años) los elegí yo. Son defendibles pero no
canónicos: un rango más estrecho daría un factor menor. Lo que **no** depende de esa elección
es la ortogonalidad, ni el hecho de que el signo cambie a diez años — para eso basta con que
μ pueda declararse en 8% y la ventana en 2 años, dos cosas que se hacen todos los días.
