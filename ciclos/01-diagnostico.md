# Ciclo 1 — Diagnóstico

**Pregunta:** ¿Cuál es el defecto estructural más profundo del Monte Carlo para riesgo a
largo plazo — el que persiste después de subir toda la escalera de modelos?

**Agentes:** A1 procesos estocásticos · A2 estadística e inferencia · A3 epistemología
e información.

| métrica | valor |
|---|---|
| κ (coherencia) | **0,9085** |
| κ_forma (Pearson medio) | 0,9803 |
| centroide | A=.83 E=.18 F=.12 P=.26 H=.95 O=.72 |
| grieta | **eje P** (parametricidad), σ=0,114 |
| modo del ciclo siguiente | GRIETA |

Los tres agentes coinciden casi por completo salvo en un eje. Coinciden en que la
incertidumbre dominante es epistémica (A=.83), en que el proceso no es estacionario
(E=.18), en que las afirmaciones a largo plazo son prácticamente infalsificables
(F=.12) y —de forma unánime, σ=0— en que el problema crece con el horizonte (H=.95).

Discrepan solo en **qué forma debe tener la salida**: A2 admite una salida paramétrica
con barras de error honestas (P=.40), A3 exige libre de modelo (P=.12), A1 queda en
medio con Γ-minimax sobre un conjunto de confianza (P=.25). Esa es la grieta, y es la
pregunta del ciclo 2.

---

## Convergencias

Tres anclas fueron alcanzadas por más de un agente desde matemáticas distintas.

**`n_eff = T/H` gobierna toda falsabilidad** — los tres, confianza agregada 0,92.
El número de observaciones independientes a horizonte H en una serie de T años es T/H,
no T·252. Muestrear más fino no crea bloques. A2 lo deriva de la potencia de un test de
cobertura (T_req ≈ 11,4·H/p), A3 de contenido empírico (N = α·T_s/H), A1 de la varianza
del estimador del propio exponente de escalamiento. **Verificado numéricamente**: el n
para poder 80% sale 1070 medido contra 1140 predicho.

**El Monte Carlo oculta el error de inferencia** — A2 y A3, 0,93. Reporta el error de
integración (1/√N, que elige el analista) y no el de inferencia (√(H/T), heredado de la
historia disponible). A2 cuantifica el subreporte en ≈√(N·H/T) y observa que es
**creciente en N**: el remedio universal del practicante —añadir trayectorias— empeora
la honestidad epistémica monótonamente.

**El invariante R(H) = √(H/T_eff)** — A1 y A2, 0,89. La razón entre incertidumbre
epistémica y aleatoria no contiene ni σ ni μ. Es adimensional y depende solo de la razón
entre horizonte y span. A1 lo agrava: con memoria larga, T_eff = T^(1−2d) y con d≈0,4
cien años de datos valen como dos años y medio.

## Convergencia independiente sobre la pregunta

Lo más importante del ciclo no es una coincidencia numérica sino que los tres agentes
cerraron con variantes de la misma pregunta, desde herramientas que no se tocan:

- A2 llega vía **Girsanov**: cambiar μ produce medidas equivalentes (indistinguibles en
  tiempo finito), cambiar σ las produce singulares (distinguibles al instante). Por eso
  I(μ) = T/σ² no depende de la frecuencia de muestreo.
- A3 llega vía **Dambis–Dubins–Schwarz**: la ley de todo funcional de trayectoria
  —drawdown, tiempo bajo el agua, ruina— depende solo de la ley de ⟨M⟩_H más los saltos.
  Toda la escalera es una reparametrización de lo mismo. Solo el drift queda fuera.
- A1 llega vía **agregación temporal**: el exponente que decidiría si el tiempo
  diversifica se estima con n_eff = T/H bloques, y su intervalo al 95% deja un factor 3
  de indeterminación en el riesgo a 30 años.

Las tres rutas señalan el mismo punto: **el drift es el único canal irreducible, y es
exactamente la dirección en la que las medidas son equivalentes** (N13). De ahí la
pregunta del ciclo 2.

## La tensión N05 ⊥ N08

A1 demuestra por simulación que la escalera **no** colapsa a GBM: el coeficiente de
variación de la varianza integrada decae como H^−0,24 en vez de H^−0,5, y el cociente
ES99(GJR)/ES99(GBM) sigue siendo 1,62 a veinte años. A3 argumenta lo contrario desde
teoría de la información: a horizontes largos toda la información pasa por θ, con
capacidad ~(d/2)log₂T ≈ 50 bits, así que subir peldaños no añade nada.

No se contradicen. La resolución es **N14**: la escalera añade *estructura*, no
*información*. Cambia la respuesta sin cambiar lo que puede saberse. Subir peldaños
mueve el número y deja intacto el conocimiento — que es exactamente la forma más
peligrosa de progreso aparente, porque se siente como mejora.

## Falsación interna

A1 partió de la hipótesis "toda la escalera colapsa a GBM por TCL funcional" y **la
falsó con su propia simulación**. La razón del no-colapso resultó más profunda que la
hipótesis: no es memoria larga, es violación de la condición de cuarto momento. Queda
registrado como N05 y como advertencia para los ciclos siguientes.

## Aportaciones marcadas como candidatas a novedad

Los tres agentes recibieron instrucción de ser brutalmente honestos sobre qué ya existe.
Lo que quedó tras ese filtro:

| candidato | de | por qué podría ser nuevo |
|---|---|---|
| **Frontera de fase M2=1 no identificable** (N06) | A1 | El estadístico discriminante (curtosis muestral) tiene varianza infinita exactamente donde hace falta: poblacional 13,5→∞ contra muestral 3,6→5,5. Semilla de un teorema de no identificación en una singularidad |
| **Subreporte √(N·H/T) creciente en N** (N04) | A2 | La fórmula explícita y, sobre todo, su monotonía en N: la práctica estándar degrada la honestidad a tasa √N, con signo opuesto al de T |
| **N\* ≈ T_eff/(H(1−q))** (N11) | A1 | Criterio de "deja de simular". No aparece formulado |
| **Colapso de canal** (N08) | A3 | La capacidad ~(d/2)log₂T como razón formal de por qué la escalera es irrelevante a largo plazo, con corolario falsable de cruce de log-score en H≈12–24 meses |
| **Demarcación N = α·T_s/H** (N03) | A3 | Un solo número que separa régimen científico (VaR diario, N=378) de metafísico (ES a 10 años, N=0,03) |

Lo demás quedó explícitamente atribuido: Merton 1980, Pástor–Stambaugh 2012, Drost–Nijman,
He–Teräsvirta, Lo–MacKinlay, Gneiting 2011, Fissler–Ziegel 2016, Shafer–Vovk,
Danielsson–Shin, Hansen–Sargent, Gordy–Juneja.

## Verificación

En `c01-raw/verificacion.md`. Dos claims confirmados, uno acotado: la predicción de que
la sensibilidad a la ventana de estimación supera a la sensibilidad al número de
trayectorias en >200× se midió en **51×** — dirección correcta, magnitud no.

## Salida hacia el ciclo 2

> ¿Existe un funcional de riesgo Ψ a horizonte H que sea simultáneamente
> **(a)** decisión-relevante, **(b)** invariante al drift —y por tanto estimable in-fill,
> sin depender del span T— y **(c)** refutable sobre una única trayectoria?

Tres agentes lo atacan desde los dos extremos del eje P y desde la imposibilidad:
construcción libre de modelo, construcción paramétrica con identificación parcial, y un
intento de teorema no-go.
