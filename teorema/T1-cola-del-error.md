# T1 — Teorema de la cola del error

*Borrador. Derivado por el orquestador para cumplir el encargo N31 de la auditoría de
novedad, que dictaminó que N28 era la única de cinco afirmaciones sin precedente
encontrado, y que para ser teorema necesitaba una derivación analítica del índice de cola.*

---

## Enunciado

> Sea `Ψ_H` el Expected Shortfall a horizonte H estimado con un modelo GARCH de
> persistencia φ, y sea `φ̂` un estimador con error aproximadamente normal de desviación
> típica `s`. Entonces el error relativo `Y = Ψ̂_H/Ψ_H` tiene **cola de potencia de índice
> 2**:
>
> ```
> P(Y > y)  ~  C · y⁻²        cuando y → ∞
> ```
>
> con `C = φ_N(ρ) / (ρ · Φ_N(ρ))` y `ρ = (1−φ)/s`, donde φ_N y Φ_N son la densidad y la
> distribución normal estándar.
>
> **El índice es 2 para todo s > 0**: no depende del tamaño muestral, del horizonte ni del
> nivel de cola. Acumular datos reduce la constante C —exponencialmente en ρ— pero **no
> cambia la forma de la cola**.
>
> **Corolario.** La varianza del estimador de ES está en la frontera de la existencia
> (índice 2) y el tercer momento no existe. Un modelo de riesgo de cola tiene, él mismo,
> error de cola pesada.

## Demostración

A horizonte largo, la varianza integrada de un GARCH converge a su valor incondicional:

```
IV_H  =  H·σ̄² + (σ²_{t+1|t} − σ̄²)·(1−φ^H)/(1−φ)  →  H·σ̄²  con  σ̄² = ω/(1−φ)
```

y el Expected Shortfall escala como `Ψ_H ≈ c_p·√IV_H ∝ (1−φ)^(−1/2)`.

Sea `X = 1 − φ̂`. Bajo normalidad asintótica del estimador, `X ~ N(m, s²)` con `m = 1−φ`.
El error relativo es

```
Y = (X/m)^(−1/2)
```

Para `y` grande, `Y > y` equivale a `0 < X < m·y⁻²`, y como la densidad de X es continua y
positiva en 0,

```
P(Y > y | X > 0) = (1/P(X>0)) ∫₀^{m y⁻²} f_X(x) dx  ≈  f_X(0)·m·y⁻² / Φ_N(ρ)
```

Con `f_X(0) = φ_N(m/s)/s = φ_N(ρ)/s` y `m/s = ρ`:

```
P(Y > y) ≈ [φ_N(ρ)/(ρ·Φ_N(ρ))] · y⁻²    ∎
```

La densidad correspondiente es `f_Y(y) ~ 2C·y⁻³`, de donde `E[Y²] = ∞` en el borde y
`E[Y³] = ∞`.

**El mecanismo es elemental y por eso robusto**: un error normal en una cantidad que
aparece en un *denominador* produce cola de potencia. Lo que no es elemental es que la
cantidad en el denominador sea `1−φ`, y que en los mercados reales φ esté a un par de
errores estándar de 1.

## Verificación numérica

`Y = (X/m)^(−1/2)` con `X ~ N(m, s²)`, 400.000 réplicas, índice por estimador de Hill:

| φ | s | ρ=(1−φ)/s | Hill α | P(error > 2×) | RMSE/mediana |
|---|---|---|---|---|---|
| 0,990 | 0,0050 | **2,00** | **2,28** | **4,49%** | 1,53 |
| 0,990 | 0,0025 | 4,00 | 8,50 | 0,13% | 1,04 |
| 0,990 | 0,0015 | 6,67 | 23,3 | 0,00% | 1,01 |
| 0,980 | 0,0050 | 4,00 | 8,30 | 0,14% | 1,04 |
| 0,950 | 0,0050 | 10,0 | 41,4 | 0,00% | 1,01 |

## El matiz, que importa

La tabla **no** muestra un índice de 2 en todas las filas, y hay que decir por qué en vez
de esconderlo.

El índice asintótico es 2 para todo s>0 — la demostración no tiene grietas. Pero el
estimador de Hill sobre el 2% superior de la muestra mide la cola *en la región que la
muestra realmente puebla*, y para ρ grande esa región está aún en el régimen
pre-asintótico, donde domina el decaimiento gaussiano. La cola de potencia está ahí, pero
empieza más allá de donde hay datos.

Es decir:

> **La cola de potencia existe siempre. Solo es observable cuando ρ = O(1).**

Y esa es la afirmación falsable, porque ρ es medible.

## La cantidad que unifica

`ρ = (1−φ)/SE(φ̂)` —la distancia del parámetro a la singularidad del funcional de riesgo,
medida en errores estándar— es la misma estructura que aparece en los otros dos resultados
de no identificabilidad del grafo:

| resultado | parámetro | singularidad | distancia medida |
|---|---|---|---|
| N24 | M2 | M2 = 1 (cuarto momento) | 0,0114 / 0,0097 ≈ **1,2 σ** |
| T1 | φ | φ = 1 (raíz unitaria) | 0,010 / 0,005 ≈ **2,0 σ** |
| N44 | d | d = 3/8 (rango de Hermite 4) | 0,03 / 0,054 ≈ **0,6 σ** |

Los tres son O(1). La conjetura que se sigue, y que va al ciclo 5:

> **Los parámetros empíricamente relevantes de la volatilidad financiera viven a uno o dos
> errores estándar de singularidades del funcional de riesgo, y esa proximidad convierte
> error de estimación normal en error de riesgo de ley de potencia.**

No es que los modelos estén mal ajustados. Es que el punto donde caen los mercados reales
está pegado a los puntos donde las fórmulas explotan, y a una distancia que ningún span de
datos disponible resuelve.

## Qué falta

1. **Medir ρ empíricamente** sobre GARCH ajustados de verdad, no supuestos. En curso.
2. Comprobar que la razón RMSE/mediana medida en el experimento de complejidad (**8,7**
   para el modelo EVT a 10 años) es compatible: aquí sale 1,53 a ρ=2, así que este canal
   explica parte y no todo. El resto vendría del segundo canal —la composición del error
   del parámetro de forma ξ de la Pareto generalizada sobre 2.520 pasos— que habría que
   derivar igual.
3. Auditar novedad. La mecánica «normal en un denominador ⇒ cola de potencia» es
   elemental y seguro que está en algún sitio; lo que hay que buscar es si alguien la ha
   aplicado al error de un modelo de riesgo y ha observado que el índice es universal.

---

## Medición de ρ sobre ajustes reales — y una retractación

**RETRACTACIÓN (ver abajo).** La primera versión de esta sección afirmaba que el
diagnóstico ρ̂ está sesgado hacia la calma. Era falso, y el error era mío.

En el script de medición escribí «DGP con persistencia verdadera 0,99». El DGP de
`motor/complejidad.py` tiene α=0,03, γ=0,09, β=0,90, luego su persistencia es

```
φ = α + γ/2 + β = 0,03 + 0,045 + 0,90 = 0,975
```

no 0,99. Comparé los ajustes contra un valor verdadero equivocado.

Con el valor correcto:

| T | φ̂ medio | SE(φ̂) | ρ̂ medido | **ρ verdadero (φ=0,975)** | error de φ̂ |
|---|---|---|---|---|---|
| 10 años | 0,9767 | 0,0067 | 3,49 | 3,73 | **−0,4%** |
| 20 años | 0,9762 | 0,0046 | 5,10 | 5,43 | **−0,5%** |
| 40 años | 0,9773 | 0,0030 | 7,34 | 8,33 | **−0,0%** |

El estimador de la persistencia está **prácticamente insesgado**, y ρ̂ sigue de cerca al ρ
verdadero. **No hay ningún sesgo hacia la calma. N53 queda retractado por completo.**

## Lo que eso le hace a T1

La demostración sigue en pie: es matemática elemental y no depende de ninguna medición. Pero
su **activación** sí depende de ρ, y aquí ρ ≈ 5,4, donde la cola de potencia existe pero es
inobservable (Hill α ≈ 14, P(error>2×) ≈ 0,01%).

Es decir: **T1 no está activo en el DGP con el que hemos trabajado, y por tanto no explica
la razón RMSE/mediana de 8,7 que se midió para el modelo EVT a 10 años.** Esa sigue sin
explicación, y el candidato que queda es el otro canal —la composición del error del
parámetro de forma ξ de la Pareto generalizada sobre 2.520 pasos—, que hay que derivar
aparte.

Para que T1 esté activo hace falta φ cerca de 1. La renta variable real suele ajustar
persistencias de 0,98–0,995; con φ=0,99 y SE≈0,005 sale ρ≈2 y la cola sí sería observable.
**Pero eso no lo hemos medido**: solo lo hemos supuesto. Medir ρ sobre series reales es
trabajo pendiente y es la única vía para saber si T1 importa o es una curiosidad.

## Estado honesto de T1

| pieza | estado |
|---|---|
| La derivación del índice 2 | **correcta**, verificada numéricamente |
| «El índice no depende de s, H ni p» | **correcta** |
| «Solo es observable cuando ρ = O(1)» | **correcta**, verificada |
| «ρ ≈ 2 en la práctica» | **no medido** — supuesto, y falso en nuestro DGP (ρ≈5,4) |
| «Explica la razón RMSE/mediana de 8,7» | **refutado** — el canal no está activo aquí |
| «El diagnóstico está sesgado hacia la calma» | **retractado** — error factual mío |

T1 baja de w=0,85 a **w=0,55**: teorema correcto, relevancia empírica no establecida.

## Nota de método

Es la segunda vez en este ciclo que una afirmación mía se cae al comprobarla, y la primera
en que el error es puramente factual: escribí un número equivocado en la cabecera de un
script y construí encima. Queda escrito con el mismo detalle que la afirmación original,
igual que la anterior.

Lo que sí sostiene esta serie de tests: φ̂ y ω̂ **no** se compensan tan limpiamente como
sugiere el folclore (el error de σ̄² es 5–10%, comparable al de ω̂), pero φ̂ está muy bien
estimado, así que el denominador 1−φ no es la fuente de incertidumbre que yo suponía.
