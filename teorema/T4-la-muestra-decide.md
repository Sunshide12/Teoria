# T4 — La muestra decide, no el horizonte

*Lo que sobrevivió a la refutación de T3, y es más simple y más fuerte que lo que cayó.
Derivado por el agente auditor del ciclo 7 y verificado de forma independiente.*

---

## Enunciado

Con el tratamiento coherente de la incertidumbre de parámetros —varianza predictiva
`σ²H(1+H/T)`, el componente de *estimation risk* de Pástor–Stambaugh (2012)—:

```
ES_{α,H} = −μ̂H + k_α·σ·√( H·(1 + H/T) )
```

Como `sup_H [ √H / √(1+H/T) ] = √T`, se sigue inmediatamente:

> **Teorema.** El Expected Shortfall al nivel α es estrictamente positivo **a todo horizonte**
> si y solo si
>
> ```
> Ŝ·√T  <  k_α        equivalentemente        T  <  (k_α/Ŝ)²  ≡  T_min
> ```
>
> Con el Sharpe típico de renta variable (Ŝ=0,375) y k₉₉=2,6652: **T_min = 50,5 años.**

## La dualidad

`T_min = (k_α/Ŝ)²` es **la misma fórmula** que el horizonte de cruce con μ conocido,
`H*_∞ = (k_α/Ŝ)²`. No es coincidencia:

> **El horizonte al que el ES cruzaría cero si μ se conociera es exactamente la longitud de
> muestra mínima para que el cruce pueda existir.**

Misma expresión, dos lecturas. Y la lectura correcta invierte la de T3:

| T3 (refutado) | T4 |
|---|---|
| a partir de H\* el signo está indeterminado | con T < T_min el signo está **determinado a todo H** |
| el horizonte destruye la información | **el horizonte no compra signo; solo la muestra lo compra** |

## Verificación

| T (años) | Ŝ·√T | k₉₉ | ¿signo determinado a todo H? |
|---|---|---|---|
| 3 | 0,650 | 2,665 | sí, siempre pérdida |
| 5 | 0,839 | 2,665 | sí, siempre pérdida |
| 10 | 1,186 | 2,665 | sí, siempre pérdida |
| 20 | 1,677 | 2,665 | sí, siempre pérdida |
| 50 | 2,652 | 2,665 | sí, siempre pérdida |
| **50,5** | **2,665** | 2,665 | **frontera** |
| 60 | 2,905 | 2,665 | no, cruza en algún H |
| 100 | 3,750 | 2,665 | no, cruza en algún H |

Y el Sharpe ajustado por incertidumbre, con T=10 años:

| H | Ŝ√H/√(1+H/T) |
|---|---|
| 1 a | 0,358 |
| 10 a | 0,839 |
| 100 a | 1,131 |
| 1.000 a | 1,180 |
| 10.000 a | 1,185 |
| ∞ | **1,186 = Ŝ√T** |

Nunca alcanza 2,665. **Alargar el horizonte no cambia el signo, por mucho que se alargue.**

## Lo que mueve, medido

Sustituir el ES enchufado por el predictivo multiplica el capital:

| H \ T | 3 años | 5 años | 10 años | 20 años |
|---|---|---|---|---|
| 1 año | 1,180× | 1,111× | 1,057× | 1,029× |
| 5 años | 1,924× | 1,604× | 1,328× | 1,172× |
| **10 años** | **2,949×** | **2,319×** | **1,746×** | 1,405× |
| 20 años | 5,771× | 4,334× | 2,974× | 2,117× |
| 40 años | 26,3× | 19,2× | **12,2×** | 7,65× |

Es **mayor que el 1,45× de N84** —que recogía solo el error de estimación sin integrar μ— y
lo contiene. A un año da 1,057×, subumbral, coherente con N100: el efecto es del horizonte,
no de la ventana.

## Alcance honesto

**La maquinaria no es nuestra.** La varianza predictiva con componente de riesgo de
estimación es Pástor–Stambaugh (2012, JF 67(2):431–478), ya registrado como rival desde la
primera auditoría. Lo nuestro es:

1. **El enunciado del umbral en forma cerrada** `T_min = (k_α/Ŝ)²`, y la dualidad exacta con
   el horizonte de cruce. El auditor lo buscó y no lo encontró publicado.
2. **La medición sobre el ES** en vez de sobre la varianza predictiva, con la tabla de
   multiplicadores por (H, T).
3. **La lectura**: no es que el riesgo a largo plazo sea indeterminado; es que **con la
   cantidad de datos que existe, está determinado, y decirlo requiere integrar la
   incertidumbre en vez de enchufarla.**

## Rivales que hay que citar, y no se habían citado

- **Dowd, Blake & Cairns (2004)**, *J. Risk Finance* 5(2):52–57 — el cruce, el pico, la
  sensibilidad a μ y la recomendación de declararlo.
- **Welch, «Long-Term Risk-Reward Tradeoffs and Sharpe Ratios»**, SSRN 5709087 (nov-2025) —
  mismo rango de horizontes, mismo mensaje, otro objeto: *«the central concern for long-term
  investors is not the sampling of draws but the uncertainty about the distribution»*.
- **Kritzman (1994/2015, FAJ)** — la forma adimensional en sustancia.
- **Bodie (1995, FAJ 51(3))** — √t ≡ μ=0 en lenguaje de opciones.

## La grieta

`T_min` se deriva en el mundo iid-gaussiano de σ constante que N45, N60 y N99 declaran
inverificable. Sustituyendo T por n_eff, T_min se alcanza aún más tarde — el resultado va en
la dirección conservadora, pero hay que medirlo.
