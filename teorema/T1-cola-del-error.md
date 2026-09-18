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

## Medición de ρ sobre ajustes reales — y el fallo del propio diagnóstico

`ρ` se midió ajustando GJR-GARCH-t por máxima verosimilitud a series simuladas de un DGP
con persistencia verdadera φ=0,99, con el error estándar de φ̂=α̂+γ̂/2+β̂ obtenido del
hessiano numérico.

| T | φ̂ medio | SE(φ̂) medio | **ρ̂ medido** | ρ p5–p95 | **ρ verdadero** |
|---|---|---|---|---|---|
| 10 años | 0,9767 | 0,0067 | **3,49** | [2,33 · 4,41] | 1,49 |
| 20 años | 0,9762 | 0,0046 | **5,10** | [3,82 · 8,04] | 2,17 |

Dos hechos, y el segundo invalida el uso ingenuo del diagnóstico.

**Primero:** φ̂ sale 0,976 frente a 0,990. El estimador sitúa la persistencia **más lejos de
la singularidad de lo que está**. Es el mismo sesgo direccional hacia el lado tranquilizador
que se midió para M2 en N15 y N24, ahora en otro parámetro y con otro estimador.

**Segundo, y es el problema:** `ρ̂ = 5,10` mientras el ρ verdadero es 2,17. Y la brecha
**crece con T** —de 3,49 a 5,10 al pasar de 10 a 20 años— porque el error estándar del
denominador encoge mientras el sesgo del numerador persiste.

Las consecuencias operativas son opuestas:

| | ρ̂ = 5,1 (lo que uno mediría) | ρ = 2,2 (la verdad) |
|---|---|---|
| Hill α | ≈ 14 | ≈ 2,3 |
| P(error de ES > 2×) | ≈ 0,01% | **≈ 3–4%** |
| lectura | «cola de potencia inobservable» | «uno de cada treinta estimados está mal por más del doble» |

> **El diagnóstico que determina si la cola de potencia está activa está sesgado hacia decir
> que no lo está, y cuantos más datos se acumulan, más seguro está de su error.**

Esto pone a T1 en la misma familia que N33 (el muro autosellado) y N15 (el sesgo con
dirección): no es solo que la cantidad relevante sea difícil de medir, es que **el
instrumento falla sistemáticamente hacia la conclusión tranquilizadora**, y la acumulación
de datos refuerza la falsa tranquilidad en vez de corregirla.

Queda registrado como N53, y es lo que hay que atacar en el ciclo 5: si ρ̂ no sirve, ¿hay
algún diagnóstico que sí? Y si no lo hay, la conjetura N52 pasa de interesante a
inverificable — que es exactamente el tipo de resultado que esta investigación busca.

**Caveat honesto:** el sesgo de φ̂ medido (−0,014) es grande y podría deberse en parte a las
cotas del optimizador o al tamaño muestral, no solo a la no regularidad. La subestimación
de la persistencia de GARCH en muestra finita es un hecho conocido; lo que aquí se añade es
que **se propaga al diagnóstico de su propia fiabilidad con el signo equivocado**. Hay que
comprobar con un estimador corregido por sesgo antes de darlo por establecido.
