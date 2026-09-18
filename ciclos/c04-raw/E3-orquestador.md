# E3 — demolición adversarial (ejecutada por el orquestador)

El agente adversarial del ciclo 4 cayó por límite de sesión. Asumo su papel, con su encargo
intacto y sin suavizarlo.

## FRENTE 3 — ¿Importa?

El encargo decía: *«Si la frontera M2=1 no es identificable pero su efecto sobre la decisión
es pequeño, el resultado es una curiosidad técnica y no un límite fundamental. Cuantifica el
efecto decisional de estar del lado equivocado. Si es pequeño, esta investigación tiene un
problema.»*

Lo cuantifiqué. Barrido con persistencia fija en 0,99, ν=8 y **ω fijo**, de modo que la
varianza incondicional es idéntica en los cuatro procesos y lo único que cambia es el cuarto
momento. 60.000 trayectorias por celda.

| proceso | curtosis poblacional | ES99 1 mes | ES99 1 año | ES99 10 años |
|---|---|---|---|---|
| M2 = 0,9960 | 22,7 | 0,209 | 0,880 | 2,453 |
| M2 = 0,9994 | **149** | 0,221 | 0,906 | 2,487 |
| M2 = 1,0016 | **∞** | 0,221 | 0,933 | 2,514 |
| M2 = 1,0114 | ∞ | 0,232 | 0,954 | 2,758 |

**Cruzar la frontera** (0,9994 → 1,0016, de curtosis 149 a curtosis infinita):

| horizonte | factor |
|---|---|
| 1 mes | **1,002×** |
| 1 año | **1,030×** |
| 10 años | **1,011×** |

**Los extremos del barrido entero**: 1,11× / 1,08× / 1,12×.

## Veredicto

**La investigación tiene el problema que el encargo anticipaba.**

La frontera que el ciclo 1 identificó como «la que decide el ritmo al que el riesgo agrega
con el horizonte» mueve el Expected Shortfall al 99% **un uno por ciento**. La curtosis
poblacional pasa de 149 a infinito y el número que se reporta no se entera.

La razón es obvia en retrospectiva y debería haberla visto antes de cuatro ciclos: **el ES99
es un cuantil al 1%, y el cuarto momento gobierna la cola mucho más lejana.** Que E[z⁴] sea
infinito afecta a probabilidades ≪ 1%. El percentil 1 vive en el cuerpo de la distribución,
no en la región donde el cuarto momento manda.

Toda la línea M2 —N06, N24, N24a, N24b, N44, N66, N67, N68— es **técnicamente correcta y
decisionalmente irrelevante para el ES**. El trabajo del ciclo 4 (la regularidad en θ, el
a=0 en f, la brecha de octava, los tres días que voltean la fase) es bueno y es cierto. Y no
importa.

## FRENTE 1 — ¿Está publicado?

E1 ya lo cerró en su propio informe, contra sí mismo: **Bahadur–Savage (1956)** para la
inexistencia de tests no triviales sobre clases ricas, **Donoho–Liu (1991)** para el riesgo
minimax como módulo de continuidad de Hellinger —y E[z⁴] tiene módulo infinito—, y
**Francq–Zakoïan (2022)** como el test exacto que construimos. El auditor de novedad había
señalado además Blough, Faust, Pötscher y Dufour, que no llegamos a revisar.

No hace falta otro agente para concluir: el frente 1 también va en contra.

## FRENTE 2 — ¿Confundimos difícil con imposible?

Sí, y E1 lo demostró: dentro del modelo la frontera **es** identificable, a tasa √T, con 5%
de error en 158 años. Mi enunciado «no identificable a ningún T» era falso. Lo indecidible
está en la ley de innovación, no en los parámetros, y ese resultado es correcto — pero por el
frente 3, tampoco importa.

## Lo que esto redirige

El ciclo 4 no destruye la investigación: la **reorienta**, y con datos propios. Puestos uno
al lado de otro, los efectos medidos en este mismo trabajo:

| fuente de error | efecto medido sobre el ES |
|---|---|
| cruzar la frontera M2=1 | **1,01×** |
| barrido M2 completo | 1,12× |
| elegir la ventana de estimación T* (N61) | **1,34× mediana, 2,16× p99** |
| oráculo vs estimado a 10 años (N57) | **24,0% → 56,6% de RMSE** |
| coste de estimar, 1 mes → 10 años (N48) | **+4 → +50 puntos** |
| el modelo EVT a 10 años (N28) | **sesgo +175%, RMSE 377%** |

**La frontera de fase es el efecto más pequeño de la tabla, por un orden de magnitud.**

Perseguimos la frontera equivocada durante cuatro ciclos. Lo que mueve la decisión no es
dónde está M2 respecto a 1: es **cuánto error de estimación entra en el ES y cómo se
amplifica con el horizonte** — que es precisamente N48, N57 y N61, los tres resultados que
salieron del trabajo propio y no de la línea principal.

Los ciclos 5 a 10 van por ahí.
