# T2 — Teorema de la autoviolación del modelo de cola

*Mecanismo para N28, encontrado tras retractar el de T1. Medido, no supuesto.*

---

## Enunciado

> Un modelo de Simulación Histórica Filtrada con colas de Pareto generalizada (GJR-GARCH-t
> + FHS + EVT) ajustado a datos financieros produce, con probabilidad ≈95%, innovaciones
> estandarizadas con `ξ̂ > 1/4` en la cola de pérdidas — es decir, **sin cuarto momento**.
>
> Al simular esas innovaciones a través de la recursión GARCH, el proceso resultante tiene
> `M2 = E[((α+γ1{z<0})z² + β)²] = ∞ > 1`: cae automáticamente del lado no identificable de
> la frontera de fase que el ciclo 1 identificó (N06).
>
> **En consecuencia el Expected Shortfall que el modelo produce no tiene varianza finita**, y
> su error es de cola pesada.

## La ironía, ahora precisa

El modelo construido para **no subestimar las colas gordas** se coloca, por construcción, del
lado de la frontera donde el cuarto momento no existe — la misma frontera que ya sabíamos no
identificable con ningún span de datos. Su propia salida hereda la patología que el modelo
fue diseñado para describir.

No es un defecto de implementación. Es lo que hace el método cuando funciona como está
previsto: ajustar una Pareto generalizada a las excedencias y remuestrear de ella.

## Medición

Veinte ajustes independientes del pipeline completo sobre series de 20 años del DGP.

| medida | resultado |
|---|---|
| ξ̂ cola derecha (ganancias) | media **+0,136**, p5–p95 [+0,029 · +0,246] |
| ξ̂ cola izquierda (pérdidas) | media **+0,372**, p5–p95 [+0,269 · +0,500] |
| ajustes con ξ̂ > 1/4 → **E[z⁴] = ∞** | derecha 5%, **izquierda 95%** |
| ajustes con ξ̂ > 1/2 → **Var[z] = ∞** | 5% |
| cuarto momento muestral de la empalmada (200k draws) | mediana **117**, p95 **10.224**, máx **57.708** |
| dispersión entre ajustes | **CV = 3,32** |

Referencias: una normal da 3, una t de Student con 7 grados estandarizada da 5.

**El cuarto momento muestral varía tres órdenes de magnitud entre ajustes del mismo proceso
generador.** Ese es exactamente el ingrediente que produce un error de cola pesada en el ES:
no la aleatoriedad del mercado, sino la dispersión del propio estimador de la cola.

La asimetría entre las dos colas es coherente con el efecto apalancamiento: la cola de
pérdidas es la pesada, y es la que determina el ES.

## Por qué se amplifica con el horizonte

Dos canales, y el segundo es el que importa:

1. **Aditivo.** Sumar H variables de índice de cola α = 1/ξ preserva el índice; la escala
   crece como H^(1/α) = H^ξ si α < 2. Con ξ ≈ 0,37 y H = 2.520, el factor es
   e^(ξ·ln H) = e^(2,9) ≈ 18 frente al √H = 50 del caso ligero. Por sí solo no explica nada
   dramático.
2. **Multiplicativo, vía la realimentación GARCH.** Cada innovación grande entra al cuadrado
   en la recursión de la varianza y **eleva la varianza futura**, que a su vez escala la
   siguiente innovación. Con `E[z⁴] = ∞`, la condición de estabilidad del segundo momento de
   σ² —M2 < 1— falla, y la varianza del proceso simulado no converge. Sobre 2.520 pasos eso
   no es un error grande: es un error sin varianza.

El segundo canal es el que convierte una cola moderada de la innovación en una explosión de
la salida.

## Qué explica, y qué no

**Explica** la razón RMSE/mediana de 8,7 medida para el modelo EVT a 10 años frente a 1,34
del GBM (N28), y el sesgo de +174,9%: una distribución sin varianza finita produce
exactamente ese patrón —mediana razonable, media y RMSE dominados por una minoría de casos
catastróficos.

**No está confirmado directamente todavía.** La prueba decisiva es medir el índice de cola
de la distribución del error de ES a través de muchos ajustes y comprobar que está cerca de
2 o por debajo. Requiere del orden de doscientos ajustes con proyección a 2.520 pasos, y
queda para el ciclo 9.

## Relación con T1

T1 (la cola del error vía la persistencia φ) quedó **inactivo** en nuestro DGP: ρ ≈ 5,4 y la
cola de potencia, aunque existe, es inobservable. T2 es un canal **distinto y activo**: no
pasa por la persistencia sino por el parámetro de forma de la cola de la innovación.

Los dos comparten la estructura de N52 —un parámetro pegado a una singularidad— pero solo
T2 está encendido aquí. T1 se conserva como teorema correcto cuya activación depende de un ρ
que no hemos medido en datos reales.

## Una coincidencia numérica que NO reclamo

ξ̂ izquierda ≈ 0,372 y el umbral de rango de Hermite d*_4 = 3/8 = 0,375 (N44) son
numéricamente casi iguales. Son parámetros distintos de objetos distintos —el índice de cola
de la innovación y el exponente de memoria larga— y no tengo ninguna razón para creer que la
coincidencia signifique algo. Se registra para que nadie la reclame después como hallazgo,
incluido yo.

## Novedad — pendiente de auditar

Que el FHS+EVT pueda generar procesos sin cuarto momento es probablemente conocido en la
literatura de EVT aplicada (la condición ξ<1/4 para el cuarto momento de una Pareto
generalizada es de manual). Lo que hay que buscar es si alguien ha señalado que **esto
convierte la salida del modelo de riesgo en una variable sin varianza finita**, y con qué
consecuencia práctica. Va a la segunda auditoría de novedad.
