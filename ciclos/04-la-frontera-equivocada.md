# Ciclo 4 — La frontera equivocada

**Pregunta:** ¿Se puede decidir, con T años de datos, de qué lado de una frontera de fase
está el proceso — y puede demostrarse que no, como cota inferior minimax en vez de como
meseta empírica?

**Agentes:** E1 Le Cam y cotas minimax · E2 presupuesto de estacionariedad · E3 adversarial
(cayó por límite de sesión; asumí su papel).

**Respuesta corta:** sí se puede decidir, tarda 158 años, y da igual porque la frontera no
mueve el número que se reporta.

---

## 1. Mi enunciado era falso

Escribí, tras medir una meseta de RMSE en cuatro tamaños muestrales, que la frontera M2=1
«no es identificable a ningún T».

E1 lo refutó con la cuenta correcta. El problema es **regular** en θ: la información de
Fisher no es singular en la frontera (autovalores de 4,6·10⁻⁴ a 464), ∇M2 ≠ 0, y
`T·KL(P⁺,P⁻) → 2c²/s² = 1,88`, medido 1,74 / 1,90 / 1,93 para el exponente a=1/2 y
divergente como T^(1−2a) para a=0,4 y 0,3 — que es exactamente el comportamiento de un
problema regular.

Luego **a_crítico = 1/2** y el error minimax es `Φ(−δ√T/s)` con s=1,031:

| T | error de clasificación de fase |
|---|---|
| 10 años | 34% |
| 80 años | 12% |
| **158 años** | **5%** |

Es identificable. Solo tarda siglo y medio.

## 2. La meseta tenía mecanismo, y no era ninguno de los que supuse

Las dos explicaciones candidatas quedan refutadas **numéricamente**, no por argumento:

- **No es ν̂.** Ajustando con ν fijado al valor verdadero sale el mismo sesgo hasta la cuarta
  cifra: −0,00233 frente a −0,00235 a 10 años. El polo en ν=4 infla el error estándar un 23%
  y nada más.
- **No es Hall–Yao 2003.** Su irregularidad exige E[z⁴]=∞, o sea ν≤4. Aquí ν≈7 y el QMLE es
  regular. El flanco que la auditoría de novedad había señalado queda cerrado.

El mecanismo real, que E1 llama **brecha de octava**:

> Una condición de **cuarto** momento se sondea con un estadístico de **octavo** momento.

`κ̂ = T⁻¹Σẑ⁴` es una media muestral de sumandos con índice de cola ν/4. Con 4 < ν < 8 ese
índice cae en (1,2): la media existe, la varianza no, el límite es estable sesgado a la
derecha, y el sesgo mediano decae como T^−(1−4/ν). Medido: IQR ~ T^−0,36 con ν=7, T^−0,29
con ν=6, T^−0,42 con ν=8.

**Sesgo y error estándar decaen al mismo orden. Su razón es constante. De ahí la meseta.**

La medición era correcta; la interpretación no; y el mecanismo correcto es mejor que el que
propuse.

## 3. Lo indecidible está en otro sitio

E1 encontró la cota que el encargo pedía, pero perturbando otro objeto.

**Lema exacto** (no asintótico): para todo modelo de escala condicional, con el mismo θ y la
misma σ₁, la afinidad de Hellinger entre las leyes de T observaciones bajo dos densidades de
innovación distintas es **exactamente ρ(f₀,f₁)^T** — porque σ_t es la misma función del
pasado bajo ambas leyes, de modo que la afinidad condicional vale ρ en cada paso
independientemente del pasado.

Con un contaminante `f₁ = (1−ε)f₀ + ε·bump(±M)`, eligiendo ε = c/T y M = (Δκ·T/c)^¼, la
afinidad no colapsa mientras Δκ **no depende de T**:

> Para toda brecha fija D>0 existen dos leyes con M2 = 1∓D/2 cuyo error minimax es
> **≥ 0,246, invariante de 10 a 32.000 años.** Exponente a = 0.

El encargo pedía un argumento de dos puntos **en θ**. Ese argumento nunca podía funcionar,
porque en θ el modelo es regular. La irregularidad está en **f**, la ley de la innovación.

Y el estadístico que lo hace tangible: **borrar los tres mayores residuos voltea la
clasificación de fase en el 18,3% / 15,0% / 15,8% de las muestras a 10 / 40 / 80 años.** No
decrece con T. A diez años, tres días mueven M̂2 más que la distancia entera a la frontera.

## 4. La frontera de falsabilidad

E2 produjo el resultado más operativo de toda la investigación: una desigualdad que clasifica
cada medida de riesgo en falsable o no.

> **H/p < T*/11,4**

acoplando el muro `T_req ≈ 11,4·H/p` (N03, verificado numéricamente: n=1070 medido contra
1140 predicho) con el presupuesto de estacionariedad T*.

| norma | T* que exigiría |
|---|---|
| VaR diario 99% | ~2,5 años |
| FRTB (ES 10d 97,5%) | **18,1 años** |
| Basilea II (VaR 10d 99%) | **45,2 años** |
| Solvencia II (1a 99,5%) | **2.280 años** |
| ECL vitalicia 10a | **11.400 años** |

Solo el VaR diario sobrevive.

Y el presupuesto de estacionariedad no solo es difícil de medir. **Certificar T* con precisión
relativa ε exige observar 1/ε² regímenes, o sea T ≥ T*/ε²; y ese presupuesto mayor exige otro
ε⁻² mayor. La sucesión no tiene punto fijo finito.** Es estrictamente más fuerte que el muro
autosellado del ciclo 3: allí la cota se volvía verificable una vez superada; aquí **nunca**.

Con dos hechos que lo cierran: la segmentación binaria encuentra **3,97 rupturas en una serie
estacionaria que no tiene ninguna** —el mismo número que en una que tiene cuatro de verdad—
y 50 años de datos no detectan al 80% ningún cambio de volatilidad menor que **×1,55**.

## 5. Y entonces el adversarial mató la línea entera

El frente decisivo del encargo adversarial era: *si la frontera no es identificable pero su
efecto sobre la decisión es pequeño, el resultado es una curiosidad técnica.*

Lo medí con ω y persistencia fijos, de modo que la varianza incondicional es idéntica en
todos los procesos y lo único que cambia es el cuarto momento:

| proceso | curtosis poblacional | ES99 a 10 años |
|---|---|---|
| M2 = 0,9994 | 149 | 2,487 |
| M2 = 1,0016 | **∞** | 2,514 |

**1,011×.**

La razón es obvia en retrospectiva y debería haberla visto antes de cuatro ciclos: el ES99 es
un cuantil al **1%**, y el cuarto momento gobierna la cola mucho más lejana. El percentil 1
vive en el cuerpo de la distribución.

**Toda la línea M2 —N06, N24a, N24b, N44, N66, N67, N68— es técnicamente correcta y
decisionalmente irrelevante.** Degradada en bloque a w≈0,50.

## 6. La tabla que reorienta la investigación

Puestos uno al lado de otro los efectos medidos en este mismo trabajo:

| fuente | efecto sobre el ES |
|---|---|
| cruzar la frontera M2=1 | **1,01×** |
| barrido M2 completo | 1,12× |
| elegir la ventana T* (N61) | **1,34× mediana, 2,16× p99** |
| oráculo vs estimado a 10a (N57) | 24,0% → **56,6%** de RMSE |
| coste de estimar, 1 mes → 10 años (N48) | **+4 → +50 puntos** |
| el modelo EVT a 10 años (N28) | sesgo **+175%**, RMSE **377%** |

La frontera de fase es el efecto **más pequeño de la tabla, por un orden de magnitud**.

Lo que mueve la decisión no es dónde está M2 respecto a 1. Es **cuánto error de estimación
entra en el ES y cómo se amplifica con el horizonte** — N48, N57 y N61, los tres resultados
que salieron del trabajo propio y no de la línea principal.

## 7. Rivales que no habíamos citado

Los propios agentes los encontraron y los reportaron contra sí mismos:

- **Francq–Zakoïan (2022, J. Econometrics 227(1):47–64)** — es exactamente nuestro test.
  N24 estaba pre-empted desde 2019. Flanco: su TLC exige E[z⁸]<∞ y la calibración que pone
  M2≈1 pone ν≈5–7, así que su test es √T-válido justo donde no hace falta. **Sin verificar:
  solo se leyó el abstract.**
- **Donoho–Liu (1991)** — riesgo minimax ≍ módulo de continuidad de Hellinger, y E[z⁴] tiene
  módulo infinito. El principio general está publicado desde 1991.
- **Bahadur–Savage (1956)** — inexistencia de tests no triviales sobre clases ricas. Nuestro
  a=0 es un Bahadur–Savage para la fase de cuarto momento de un GARCH.
- **Francq–Zakoïan (2004, Bernoulli)** — √T-CAN bajo E[z⁴]<∞. Es lo que hace de M2=1 un punto
  regular. Solo lo redescubrimos.
- **Müller–Watson (NBER w21564)** — T años solo informan sobre frecuencias > 1/T.

## 8. Lo que queda escrito

Cuatro ciclos persiguiendo la frontera equivocada. El trabajo es correcto y el resultado es
cierto, y la conclusión operativa es que no sirve. Queda en el repositorio con el mismo
detalle que si hubiera funcionado, porque el registro de lo que no funcionó es la parte del
método que no se puede reconstruir después.

Los ciclos 5 a 10 van por la tabla del punto 6.
