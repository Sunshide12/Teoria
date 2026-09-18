# El coste de estimar crece con el horizonte — versión limpia y decisiva

Tercer intento del experimento, con el bug corregido (el parche anterior rebindeaba el
atributo del módulo mientras el argumento por defecto `p=DGP` seguía apuntando al
diccionario original, así que era un no-op y devolvía los mismos números).

**Diseño limpio:** DGP sin saltos, de modo que el modelo 3 (GJR-GARCH-t) es **exactamente**
la familia del generador. El oráculo tiene error cero por construcción, y toda la
diferencia entre oráculo y estimado es error de estimación, sin mezcla posible con
especificación.

## Resultado

| horizonte | ORÁCULO-3 | MODELO-3 estimado | ORÁCULO-GBM | GBM estimado |
|---|---|---|---|---|
| 1 mes | **3,1%** | 7,1% | 26,3% | 29,5% |
| 1 año | **5,2%** | 16,5% | 31,0% | 33,5% |
| 10 años | **6,6%** | 56,6% | 24,0% | 60,8% |

**Coste de estimar** (RMSE estimado − RMSE oráculo, mismo modelo):

| horizonte | coste |
|---|---|
| 1 mes | **+4,0 puntos** |
| 1 año | **+11,2 puntos** |
| 10 años | **+50,0 puntos** |

El oráculo del modelo correcto es casi perfecto a los tres horizontes: 3,1%, 5,2%, 6,6%.
La especificación no es el problema. **El coste de estimar se multiplica por doce entre un
mes y diez años.**

Esto confirma la hipótesis original con la que entré al ciclo 2: el error epistémico se
amplifica con el horizonte. Ahora medido sin contaminación.

## Lo que obliga a reformular

El ranking se invierte respecto al experimento con saltos. Aquí **el modelo bien
especificado gana en los tres horizontes** (56,6% frente a 60,8% del GBM a 10 años).

Así que **N27 —«la complejidad óptima decrece con el horizonte»— NO es cierto como ley
general.** Cuando la complejidad extra es *correcta*, sigue pagando a todos los horizontes.

El enunciado correcto es otro, y es más preciso:

> El horizonte no penaliza la complejidad. Penaliza la **estimación**. Un modelo más
> complejo tiene más parámetros que estimar, así que paga más peaje — pero solo pierde si
> esa complejidad extra es equivocada o superflua.

En el experimento con saltos el modelo 3 era complejo **y equivocado** (le faltaban los
saltos), y el modelo EVT era complejo **y superfluo** (añadía colas que se autoviolaban,
T2). Por eso perdían. Aquí, complejo y correcto, gana.

## El dato que sí es limpio y sorprendente

> **A diez años, un modelo mal especificado con parámetros conocidos (ORÁCULO-GBM, RMSE
> 24,0%) bate a un modelo correctamente especificado con parámetros estimados (MODELO-3,
> RMSE 56,6%).**

A un mes ocurre lo contrario, y por mucho: 3,1% frente a 26,3%.

Es el compromiso sesgo-varianza, pero con el punto de cruce medido y en un sitio incómodo:
**entre un año y diez años, saber los parámetros de un modelo malo pasa a valer más que
tener el modelo bueno y estimarlo.**

## Estado de los nodos

- **N48 sube a w=0,92.** El coste de estimar crece con el horizonte: +4,0 → +11,2 → +50,0
  puntos. Medido tres veces, la última sin contaminación.
- **N27 baja a w=0,40 y se reformula** como caso particular: la complejidad solo penaliza a
  horizonte largo si es incorrecta o superflua. En nuestro primer experimento lo era por
  las dos vías (saltos ausentes en el modelo 3, colas autoviolatorias en el modelo 4).
- **Nodo nuevo N57**: a diez años, modelo malo con parámetros conocidos bate a modelo bueno
  con parámetros estimados; a un mes, al revés por un factor de ocho.

## Nota de método

Es el tercer intento de este experimento. El primero mezclaba especificación con estimación
y me llevó a una conclusión equivocada que defendí ante el auditor. El segundo tenía un bug
de Python que lo convertía en una repetición del primero. Este es el que decide, y decide
en contra de la mitad de lo que afirmé.

Lo que sobrevive —la amplificación del coste de estimar con el horizonte— es lo que más me
importaba, y ahora está medido en condiciones donde no admite otra lectura.
