# Auditoría de novedad #2 — dictamen

Segundo sistema independiente. De seis candidatos: **dos muertos, dos reformulaciones
medibles de resultados conocidos, uno que no es teorema, y uno que es recolocación de
folclore.** En sus palabras: *«Eso no es una investigación con seis contribuciones; es como
mucho una con una.»*

| candidato | veredicto | cita decisiva |
|---|---|---|
| **A.** T2, autoviolación del modelo de cola | **PUBLICADO** | Ma & Wei (2025), *JEDC* 177, art. 105124 |
| **B.** N28, la cola del error | **ADYACENTE** (la auditoría #1 fue generosa) | Bams–Lehnert–Wolff (2005), *JIMF* 24(6):944–958 |
| **C.** N48/N57, coste de estimar vs horizonte | **CASI** | Pástor–Stambaugh 2012 + **DeMiguel–Garlappi–Uppal 2009** |
| **D.** N59, frontera de falsabilidad | **ADYACENTE** — el más sano de los seis | Zumbach (2020), arXiv:2007.12431 |
| **E.** N58, regreso divergente | **ADYACENTE, y no es teorema** | Nobel 1999; Ryabko 2010 |
| **F.** N64, afinidad multiplicativa | **PUBLICADO, y peor: trivial** | Le Cam 1986; Liese–Vajda 1987; Tsybakov 2009 §2.4 |

---

## A — T2 muere, y con un non sequitur mío dentro

Ma & Wei (2025, *Journal of Economic Dynamics and Control* 177) estudian ARMA–GARCH
*«where innovations are assumed to follow a Pareto-type tail distribution and have no finite
fourth moments»*. El régimen que T2 presentaba como hallazgo empírico **es la hipótesis de
trabajo declarada de un artículo publicado**. Y Francq–Zakoïan 2022 ya motiva explícitamente
el problema por el Expected Shortfall, y en su estudio empírico concluye evidencia fuerte de
no existencia del momento de orden 8.

Los ξ̂ ≈ 0,2–0,4 sobre residuos estandarizados están en McNeil–Frey 2000, el artículo
fundacional del método que estábamos criticando.

**Y el agujero lógico, que es mío:** ξ̂ ≈ 0,372 ⇒ α de la innovación ≈ 2,69, es decir
innovaciones **con varianza finita**. De ahí se sigue que falla la condición de cuarto
momento del proceso (correcto), pero **no** que su ES no tenga varianza finita: eso exige
α del proceso < 2, que es la ecuación de Kesten, no ξ̂ > 1/4.

**Lo comprobé en vez de retractarlo a ciegas.** Midiendo el índice de cola por Hill:

| objeto | α medido |
|---|---|
| innovación empalmada | **3,40** |
| proceso GARCH simulado con ella | **2,43** |

La recursión GARCH **sí** engorda la cola sustancialmente —de 3,40 a 2,43— pero **no la cruza
por debajo de 2**. El ES sí tiene varianza finita. **Mi afirmación era un non sequitur, y
está medido que lo era.**

T2 baja de w=0,88 a **w=0,20**: el hecho medido (95% de los ajustes con ξ̂>1/4) se conserva;
la consecuencia que le atribuí, no.

## F — N64 muere por trivial, que es peor que por precedente

Fijados θ y σ₁², el filtro GARCH es una **biyección bimedible** entre innovaciones y
observaciones. Las f-divergencias son invariantes bajo biyecciones bimedibles (Le Cam 1986;
Liese–Vajda 1987) y la afinidad de Hellinger tensoriza sobre medidas producto (Tsybakov 2009,
§2.4). Componiendo: ρ(P₀^T, P₁^T) = ρ(f₀,f₁)^T. **Dos líneas, dos hechos de libro de texto.**

Y es el paso de arranque de toda demostración de LAN/contigüidad para GARCH
(Drost–Klaassen 1997; Drost–Klaassen–Werker 1997). Lo asintótico entra solo cuando σ₁² es
desconocido —que es el caso interesante, y el que la identidad excluye por hipótesis—.

**N64 baja de 0,90 a 0,10 y se retira como aportación.**

## E — N58 no es un teorema

*«El regreso solo diverge si se exige la misma precisión relativa ε en cada nivel; si ε puede
relajarse al subir (que es lo natural: solo necesito T\* con precisión suficiente para decidir
una comparación binaria), la sucesión termina. El candidato asume lo que quiere probar.»*

Correcto. Y la literatura de imposibilidad ya dice algo más fuerte y mejor demostrado:
Nobel (1999, *Ann. Statist.* 27(1):262–273) y Ryabko (2010, arXiv:0809.1053) establecen que
ningún procedimiento es consistente para toda clase ergódica.

**N58 baja de 0,85 a 0,30** y se reduce a observación dentro de N59.

## B — la primera auditoría fue generosa, pero hay un hueco real

Bams–Lehnert–Wolff (2005, *JIMF* 24(6):944–958) dicen literalmente que los modelos de cola
sofisticados *«come at the cost of more uncertainty about the VaR-estimate itself»*.
Figlewski (2003) muestra que el error de estimación multiplica por órdenes de magnitud la
probabilidad de eventos de cola encadenados. Taleb–Cirillo (2019) demuestran el mecanismo
general: la incertidumbre anidada engorda la cola.

**Pero hay una tensión publicada que nadie ha resuelto**, y el auditor la señala:
Hoga (2025, *Econometric Theory*, arXiv:2304.10349) **establece normalidad asintótica** del
error de las previsiones EVT de riesgo extremo sobre residuos desvolatilizados. Y nosotros
medimos RMSE/mediana = 8,7. **Ambas cosas no pueden ser toda la verdad.**

Su recomendación: el ES de una GPD escala como 1/(1−ξ), luego un ξ̂ asintóticamente normal se
transforma en un ES con **polo en ξ̂ = 1**, y la distribución hereda cola de potencia.

**Lo derivé y lo verifiqué.** El índice teórico es **1** —la media del estimador de ES no
existe— y se confirma numéricamente. Pero la constante es a·φ(a) con a = (1−ξ)/SE(ξ̂):

| ξ | N_u | SE(ξ̂) | a | Hill | P(error>2×) | P(ξ̂≥1) |
|---|---|---|---|---|---|---|
| 0,372 | 250 | 0,087 | **7,24** | 12,9 | 0,02% | 2·10⁻¹³ |
| 0,372 | 50 | 0,194 | 3,24 | 2,39 | 5,2% | 6·10⁻⁴ |
| 0,700 | 100 | 0,170 | **1,76** | **1,10** | **15,6%** | 3,9% |
| 0,850 | 60 | 0,239 | **0,63** | **1,03** | 15,2% | 26,5% |

**El polo no está activo a los parámetros que medimos** (a=7,24). Se activa solo con ξ≈0,7–0,85
y pocas excedencias.

Es el **tercer mecanismo** que propongo para explicar la razón de 8,7, y el tercero que no
aguanta:

| mecanismo | estado |
|---|---|
| T1, polo en la persistencia φ | correcto, **inactivo** (ρ≈5,4) |
| T2, cuarto momento infinito | **non sequitur**, α del proceso = 2,43 > 2 |
| polo en ξ de la GPD | correcto, **inactivo** (a=7,24) |

**La medición se sostiene. La explicación no.** Queda registrado así.

## C y D — lo que sobrevive, y a medias

**C** está cubierto por dos literaturas que juntas no dejan sitio: Pástor–Stambaugh 2012 para
«el coste de estimar crece con el horizonte», y **DeMiguel–Garlappi–Uppal 2009** —que no solo
muestran que el mal especificado bate al bien especificado-estimado sino que **calculan el
tamaño muestral del cruce** (≈3.000 meses con 25 activos), estructuralmente idéntico a
nuestro N57—. Solo sobreviviría como **ley de escala**: el exponente γ de
(coste de estimar)/(coste de especificar) ∝ H^γ, y H\* en forma cerrada.

**D es el más limpio de los seis** y está a medio hacer. Zumbach (2020) ya tiene el escalado
—el tamaño muestral efectivo decae como 1/ΔT mientras el tamaño del test crece como √ΔT— y el
«múltiplo de 200 años» para Solvencia II ya es folclore publicado. Lo que falta: derivar
T_req de un backtest de ES **con corrección por riesgo de estimación**, dejar la constante
11,4 como función explícita de (α, potencia) en vez de inventada, y **definir y estimar T\*
operativamente en vez de postularlo**.

---

## El rival que importa

> **Danielsson, J. (2002), «The emperor has no clothes: Limits to risk modelling»,
> *Journal of Banking & Finance* 26(7):1273–1296.**

*«Es la tesis entera de esta investigación publicada hace veinticuatro años en una revista de
primer nivel: que los modelos de riesgo son no robustos y excesivamente volátiles a través de
clases de activos y modelos, que las propiedades de riesgo de los datos cambian al ser
observadas, que el análisis estadístico en calma no informa sobre la crisis, y que el VaR
puede dar información engañosa e incluso aumentar el riesgo. Todo lo que sobrevive de estos
cuatro ciclos son casos particulares cuantificados de ese artículo.»*

Es correcto, y hay que asumirlo de frente.

## La reformulación que queda

Si la tesis cualitativa es de 2002, la aportación posible es **la cuantificación**. Y hay una
sola cifra en todo el trabajo que es cuantitativa, medida, ortogonal y no aparece en
Danielsson:

> **N74: un factor de 3,4 en el capital regulatorio a un año no está fijado por ningún dato**
> —solo por dos convenciones no declaradas, la ventana de estimación y la deriva declarada,
> que son ortogonales y por tanto multiplican— **y a diez años ni el signo del ES está
> determinado** (de −0,120 a +1,444 con los mismos datos).

Eso es lo que los ciclos 6 a 10 tienen que volver irrefutable. Todo lo demás pasa a contexto.
