# Corrección a N27 — el test del oráculo refuta mi propio mecanismo

## Lo que afirmé

Respondiendo a la auditoría de novedad, que objetaba que N27 podía ser un artefacto de
evaluar contra un DGP simulado por nosotros mismos, escribí:

> «El DGP verdadero pertenece a la familia del modelo 3, que por tanto está **bien
> especificado**. Si un modelo bien especificado pierde contra uno mal especificado, la
> derrota es **puramente error de estimación**, que es exactamente la tesis.»

Y propuse el test del oráculo como decisivo.

## Lo que salió

| horizonte | ORÁCULO-3 (params verdaderos) | MODELO-3 estimado | GBM estimado | ORÁCULO-GBM |
|---|---|---|---|---|
| 1 mes | 37,0% | 40,2% | 38,2% | **35,4%** |
| 1 año | 45,5% | 48,5% | 44,3% | **41,5%** |
| 10 años | **65,5%** | 56,4% | 47,3% | **28,8%** |

A diez años el oráculo del modelo complejo es **el peor de los cuatro**, y su versión
estimada le gana por nueve puntos.

## Por qué mi afirmación era falsa

El DGP incluye saltos de Poisson. El modelo 3 (GJR-GARCH-t) **no los tiene**. Por tanto el
«oráculo-3» no estaba bien especificado: le faltaba un componente del generador. A un mes
esa omisión importa poco; a diez años los saltos aportan una parte grande de la cola, y el
oráculo la ignora sistemáticamente.

La afirmación de que el modelo 3 pertenecía a la familia del DGP es sencillamente
incorrecta, y con ella se cae el argumento con el que respondí al auditor.

Y hay un segundo hecho que tampoco encaja con mi mecanismo: a diez años el error de
estimación **redujo** el error del modelo 3 (de 65,5% a 56,4%). El ruido del estimador
compensó parcialmente el sesgo de especificación. Eso es lo contrario de «el error de
estimación se amplifica con el horizonte».

## Lo que sí sostiene el test

**ORÁCULO-GBM a 10 años: sesgo −28,8%, RMSE 28,8%.** Sesgo y RMSE idénticos, es decir
varianza prácticamente nula. Frente a los 47,3% del GBM estimado.

Esos 18,5 puntos de diferencia entre el GBM con parámetros verdaderos y el GBM estimado
**sí son error de estimación puro**, sobre el modelo más simple posible y a horizonte
largo. Esa parte del mecanismo aguanta.

## Qué queda de N27

El fenómeno original es real —el modelo EVT pasa de un sesgo del −1,0% a un mes a +174,9%
a diez años, con un RMSE de 377%— pero **el mecanismo que le atribuí no está demostrado**.
La explicación honesta ahora mismo es una interacción entre especificación y composición
de colas, no un puro compromiso sesgo-varianza amplificado por el horizonte.

**N27 baja de w=0,85 a w=0,60** y se reformula: *observado, mecanismo no establecido*.

**N28 (la cola del error) no se ve afectado** y sigue siendo la pieza más limpia: la razón
RMSE/mediana de 8,7 del modelo EVT frente a 1,34 del GBM es un hecho medido que no depende
de por qué ocurre. El encargo de derivarlo analíticamente (N31) sigue en pie y es más
importante ahora, porque es lo que convertiría la observación en mecanismo.

## El test que sí decide

Se lanza la versión limpia: **DGP sin saltos**, de modo que el modelo 3 es exactamente la
familia del generador. Entonces el oráculo-3 tiene error cero por construcción y toda la
degradación del modelo 3 estimado es error de estimación, sin mezcla posible.

Si en esa versión el GBM estimado sigue ganando al modelo 3 estimado a diez años, el
mecanismo queda establecido. Si no, N27 se queda en observación y hay que buscar otra
explicación.

## Nota de método

Esto es exactamente para lo que sirve el bucle. La afirmación no la hizo un agente: la hice
yo, al responder a una crítica, y era conveniente para mi posición. El test que propuse
para defenderla la refutó. Queda escrito con el mismo detalle con el que se escribió la
afirmación original.
