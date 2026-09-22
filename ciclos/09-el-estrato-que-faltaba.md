# Ciclo 9 — El estrato que faltaba

**Encargo (literal de I3):** *«La acción correcta para el ciclo 9 no es simular: es
gastar el presupuesto entero en un segundo buscador con consultas disjuntas.»*

**Agentes:** J1 (econométrico), J2 (finanzas de inversión), J3 (regulatorio/actuarial).
Los tres reportaron. **54 consultas preregistradas, 27 textos íntegros extraídos.**

`κ = 0,756` · centroide `[A .88 · E .58 · F .67 · P .86 · H .49 · O .82]` · modo GRIETA ·
**eje E por cuarto ciclo consecutivo** (σ=0,205).

---

## El ciclo salió al revés de como se planeó, y eso es el resultado

Se desplegaron tres buscadores para **bajar** la masa no vista por debajo del 20%. La
subieron.

| | masa no vista |
|---|---|
| ciclo 8 (Chapman único) | 47% |
| J1 (econométrico) | 30% |
| J2 (inversión) | **54%** |
| J3 (regulatorio) | **78%** |

Y por el camino mataron tres de las cinco afirmaciones que el ciclo 8 celebraba.

### Lo que murió

**`T_req = 55,8 años` — muerto.** Noguer i Alonso (2026, arXiv:2606.08209, ec. 21):
*«To test a drift with two-sided size α and power 1−β, the approximate required horizon
is T ≳ ((z₁₋α/₂+z₁₋β)/|θ|)²»*, con *«For an annual Sharpe ratio θ = 0.33… a horizon on
the order of decades»*. Evaluada en Ŝ=0,375 da **55,81 años**. El número exacto.

Lo encontraron **J1 y J2 por separado**, con consultas disjuntas. Es la convergencia
independiente más fuerte que ha producido el motor de correlación (confianza agregada
0,948), y lo que señala es una retractación.

**El techo `T_eff ≤ T/ρ̄` — muerto.** Giller (2024, ecs. 17–18): *«0 ≤ N\* ≤ 1/ρ»*. Con
ρ̄=0,6: 16,67 años efectivos. El número exacto.

**La tesis cualitativa — muerta.** Spadafora, Dubrovich & Terraneo (2014, UniCredit):
*«such a scaling of the mean would be difficult to justify in statistical terms, since
the sample uncertainty of the empirical estimation of the short-term mean is typically
comparable to the value itself. Therefore we deem reasonable to set the long-term mean to
zero»*. Es nuestra tesis entera, escrita por practicantes de capital económico bancario.

**La firma de revisión — el mecanismo, muerto.** Richards, Currie & Ritchie (2012):
simular un año extra de datos, reajustar el modelo, y usar la dispersión de la revisión —
descompuesta en **σ_drift** y σ_ε. Publicado en longevidad desde 2012, y usado como
criterio de modelo interno bajo Solvencia II.

**Y el 48× — falso, por nuestra propia medición.** El ciclo 8 predijo que un número con
μ̂ se revisa 48 veces más que uno con μ≡0. Medido sobre **90 reestimaciones anuales
reales**: **3,04×**. El 48× suponía σ constante; σ̂ también se revisa, un 6,42% del nivel.

### Lo que la contradicción explícita reveló

El motor marcó `revision-variance-diagnostic` como **contradictorio**: J1 conf 0,78 («sin
precedente»), J2 conf 0,62 («sin precedente»), **J3 conf 0,15 («publicado en 2012»)**.

Dos buscadores no encontraron nada porque buscaron en la literatura equivocada. El
tercero lo encontró en la primera consulta derivada. **Eso es exactamente para lo que se
diseñaron las consultas disjuntas**, y es la primera vez en nueve ciclos que el eje de
contradicción del motor señala un hecho verificable en lugar de una diferencia de énfasis.

---

## La corrección metodológica, que es de J3

> Chapman exige **captura homogénea**. El ciclo 9 la refuta.

| pareja | solapamiento |
|---|---|
| J1 × J2 (econométrico × inversión) | 7/23 = **0,304** |
| J2 × J3 (inversión × regulatorio) | 1/17 = 0,059 |
| J1 × J3 (econométrico × regulatorio) | 0/17 = **0,000** |

Factor superior a 5 entre tasas. **Un Chapman único sobre la unión no estima N: estima la
heterogeneidad y la llama N.** El 78% de J3 lee como falta de cobertura lo que es
ausencia de segunda muestra.

**La regla del ciclo 8 queda reformulada por estratos:**

- Estrato econométrico: dos muestras ⇒ estimable ⇒ **47,5% sin ver ⇒ bloquea**.
- Estrato regulatorio/actuarial: **una sola muestra ⇒ no estimable**. No produce una
  fracción: produce **la obligación de una segunda muestra**.

Lo cual convierte el bloqueo en una tarea acotada en vez de un pozo sin fondo.

---

## Y nuestra premisa era falsa

«La convención regulatoria es fijar μ=0» es **específica de la banca de negociación**.

El **C-3 Phase II de la AAA/NAIC (2005)**, prescrito para capital RBC de rentas
variables, **fija la deriva de renta variable en A = 0,055 instantáneo** (Tabla 6). Y su
Tabla 15 publica factores de acumulación a 20 años al percentil 0,5% **por encima de 1**
para los tres activos de renta fija: MONEY 1,230 · ITGVT 1,383 · LTCORP 1,229.
**Requisito de capital negativo, tabulado sin comentario, desde 2005.**

El fenómeno que presentábamos como escándalo latente es rutina en el vecindario actuarial.
Pero el blanco no se encoge: se agranda. **Meten un μ por decreto y sin banda de confianza
publicada.**

J3 además reprodujo independientemente nuestro 44,5%: `ln(0,706/0,158) = 1,495` de 3,338
nats = **44,8% del número**.

---

## La corroboración que no nos buscaba

La Fed publica (17-abr-2025) que los cambios interanuales del *stress capital buffer*
promedian **65 pb** sobre un nivel medio de **3,88 pp**. Si la revisión es centrada y
gaussiana, σ ≈ **21,0% del nivel** — frente al **20,4%** que predice la aritmética para un
número con μ̂ estimada sobre T=10 años, y al 0,42% de uno con μ≡0.

Es la mejor corroboración externa de nueve ciclos. Con las dos advertencias que la propia
fuente obliga a poner: la Fed **promedia dos años precisamente para suprimir esa señal**
(65→54 pb), y Curry (2021 §3.7.4) documenta que las entidades suavizan deliberadamente.

---

## Lo que quedó en pie, y por qué

Con las tres piezas del ciclo 8 muertas, el ciclo 9 no se quedó sin resultado: **fue a
mirar la serie real**, que en nueve ciclos nadie había hecho. Fama–French, 1926-07 a
2026-07, 1.201 meses.

Y ahí apareció **T6 — la banda ciega**. Está en `teorema/T6-la-banda-ciega.md`, verificada
en `verificacion/N133-la-banda-ciega.md` y sellada en `protocolo/`.

Tres cosas de las que salió:

1. **El signo ya está del revés.** Con la ventana de diez años, `ES₉₉` a diez años con μ̂
   es **−0,1842**; con μ≡0 es **+1,3408**.
2. **T_det = 96 años · T_est = 85 años.** El conjunto de ventanas admisibles está **vacío**,
   y el mecanismo es causal: σ̂ salta de 0,157 a 0,182 entre T=94 y T=96, o sea **las
   únicas ventanas que determinan el signo son las que cruzan la ruptura de 1941**.
3. **El eje E, medido por fin.** Sobre la misma serie, el sup-Wald HAC sobre la
   volatilidad da 16,8–40,7 (ruptura al 1%); sobre la media da **1,67** (crítico 12,35).
   La grieta que llevaba cuatro ciclos abierta no era conceptual: era esta asimetría sin
   medir.

Y la objeción más fuerte de J1 —«usa el estimador predictivo»— se comprobó y **no lo
mata**: la banda pasa de (6,60 , 18,96) a (7,16 , 24,40), un **39% más ancha**. La
corrección predictiva añade varianza, no información sobre μ.

---

## Pregunta para el ciclo 10

**Una sola, y acotada:** una segunda muestra independiente del estrato
regulatorio/actuarial, más el cierre del estrato econométrico. Si el 20% se cruza, T6 es
admisible como aportación. Si no, T6 queda en el repositorio como lo que es —una
conjetura fechada, sellada y falsable— y se dice así.

Pendiente heredado que sigue abierto: verificar **Couts et al. (JFE 2025)** (ScienceDirect
403) y **Jorion 1996, *Risk²*** (FAJ 52(6)), que J1 señala como el precedente no detectado
más plausible.
