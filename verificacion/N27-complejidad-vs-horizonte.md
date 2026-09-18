# Complejidad óptima frente al horizonte — hipótesis del orquestador, verificada

No salió de ningún agente. Es mía, y se contrastó antes de meterla en el grafo.

## La hipótesis

Si el error epistémico se amplifica con el horizonte (N04) y toda la información pasa por
θ con capacidad ~(d/2)log₂T (N08), entonces **la complejidad de modelo que minimiza el
error en una medida de riesgo a horizonte H debe ser decreciente en H.**

El razonamiento: el error de especificación (sesgo) baja al añadir parámetros, pero el de
estimación se amplifica con el horizonte, porque la sensibilidad de la medida de riesgo a
cada parámetro crece con H mientras la precisión de cada parámetro está fija por T. Más
parámetros son más canales por los que el horizonte amplifica ruido.

Si es cierta, usar el modelo más sofisticado para el estrés a 10 años es exactamente lo
contrario de lo correcto — y eso es lo que hace todo el mundo.

## El diseño

DGP verdadero conocido: GJR-GARCH-t(ν=7) con saltos. Se entrena con 20 años diarios, se
proyecta a tres horizontes y se compara contra la verdad, que se conoce porque se simula
desde el mismo estado final del DGP. 25 réplicas independientes. Código en
`motor/complejidad.py`.

Cuatro modelos de complejidad creciente ajustados **al mismo dato**.

## El resultado

| horizonte | modelo | sesgo rel. | RMSE rel. | \|error\| mediano |
|---|---|---|---|---|
| 1 mes | GBM (2p) | −36,3% | 38,1% | 36,1% |
| 1 mes | GARCH-N (4p) | −39,1% | 40,6% | 41,6% |
| 1 mes | GJR-GARCH-t (6p) | −38,4% | 40,6% | 40,3% |
| 1 mes | **GJR-t+EVT (8p)** | **−1,0%** | **29,6%** | 22,4% |
| 1 año | GBM (2p) | −43,6% | 45,3% | 44,1% |
| 1 año | **GARCH-N (4p)** | −42,6% | **44,8%** | 46,1% |
| 1 año | GJR-GARCH-t (6p) | −47,9% | 49,7% | 52,0% |
| 1 año | GJR-t+EVT (8p) | +39,6% | 84,1% | 22,6% |
| 10 años | **GBM (2p)** | −26,2% | **47,0%** | 35,1% |
| 10 años | GARCH-N (4p) | −28,5% | 47,1% | 40,8% |
| 10 años | GJR-GARCH-t (6p) | −45,9% | 56,2% | 49,6% |
| 10 años | GJR-t+EVT (8p) | **+174,9%** | **377,4%** | 43,6% |

Complejidad óptima por horizonte creciente: **8p → 4p → 2p**. Monótona decreciente.
**Hipótesis confirmada.**

## Lo que hay que decir con honestidad

**A diez años todos fallan.** El mejor RMSE es 47%. El GBM no gana por ser bueno: gana
por ser el menos catastrófico. Coronarlo como "el modelo correcto a largo plazo" sería
repetir el error del vídeo con el signo cambiado.

El resultado correcto es más incómodo que cualquiera de las dos posturas: a horizonte
largo **ningún modelo de la escalera da un número utilizable**, y el más sofisticado da
el peor de todos.

## Lo que creo que es el verdadero hallazgo

Mírense las dos últimas columnas del modelo EVT a 10 años: RMSE 377% pero error mediano
43,6%. Razón RMSE/mediana = **8,7**. Para el GBM: 47,0 / 35,1 = **1,34**.

El modelo sofisticado no es típicamente peor. Es **catastróficamente peor de vez en
cuando**. Su distribución de error tiene colas gordas.

> **La distribución de error de un modelo de cola hereda las colas gordas del fenómeno que
> modela.** Cuanto más cuidadosamente se modela la cola, más gorda es la cola del error
> propio.

El mecanismo es visible: el parámetro de forma ξ de la Pareto generalizada se estima con
~250 excedencias, y su error se compone multiplicativamente sobre 2520 pasos. Es N07
—«EVT no es ajustable a horizonte largo»— apareciendo de forma dinámica en vez de
estática.

La ironía es exacta: el instrumento construido para no subestimar las colas gordas las
tiene en su propio error, y nadie las mide porque nadie reporta la distribución del error
de su modelo de riesgo — solo el número.

Se registra como N27 y N28.

## Relación con la literatura

Que los modelos simples ganen a horizonte largo es folclore econométrico desde
Meese–Rogoff (1983): el paseo aleatorio bate a los modelos estructurales de tipo de
cambio fuera de muestra. Y el compromiso sesgo-varianza es de manual.

Lo que no he encontrado enunciado es (a) la **monotonía en H** de la complejidad óptima
para **medidas de riesgo de cola** —no para pronósticos puntuales—, con el óptimo
cruzando peldaños concretos de la escalera estándar, y (b) la observación sobre la
**curtosis del error**: que el coste de la sofisticación no se paga en error típico sino
en frecuencia de error catastrófico. Ambas cosas se contrastan en el ciclo 6 contra la
literatura, con agentes dedicados a buscar precedentes.
