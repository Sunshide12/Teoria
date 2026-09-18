# Auditoría de novedad #1 — dictamen

Sistema independiente, en paralelo al bucle. Único trabajo: encontrar precedentes y
destruir lo que no se sostenga.

| candidato | veredicto | cita decisiva |
|---|---|---|
| **B.** Artzner/Rockafellar = Girsanov (N19) | **PUBLICADO** | Rockafellar–Uryasev–Zabarankin 2006, *Finance and Stochastics* 10(1):51–74 |
| **A.** Anticorrelación relevancia/refutabilidad (N25) | **CASI** | Merton 1980 + Chopra–Ziemba 1993 + DeMiguel–Garlappi–Uppal 2009 |
| **E.** Torre del drift (N16) | **CASI** | Phillips–Yu 2005; Tang–Chen 2009; Yu 2012; Pástor–Stambaugh 2012 |
| **C.** M2=1 no identificable (N24) | **ADYACENTE**, con flanco | Francq–Zakoïan 2022; **Hall–Yao 2003**, *Econometrica* 71(1):285–317 |
| **D.** Complejidad decreciente (N27) | **ADYACENTE**, signo disputado | Christoffersen–Diebold 2000; Danielsson–Zigrand 2006; Wang–Yeh–Cheng 2011 |
| **D'.** Cola del error (N28) | **NO ENCONTRADO** | — |

## Lo que hay que abandonar

**N19 cae.** Rockafellar–Uryasev–Zabarankin 2006 demuestran la correspondencia biunívoca
D(X)=R(X−E[X]) entre medidas de desviación (invariantes por traslación) y coherentes
aditivas en efectivo. La capa de Girsanov no añade matemática: para un proceso de Itô el
cambio de medida deja invariante la difusión y solo desplaza E[X]. Nuestro «teorema» es
ese teorema con vocabulario nuevo encima. **Se degrada de w=0,93 a w=0,25 y se reclasifica
como reformulación pedagógica, no como hallazgo.**

Era el resultado que el ciclo 2 dio por más limpio. No lo era.

**N25 baja a marco expositivo.** La anticorrelación cualitativa es folclore desde
Chopra–Ziemba 1993 (errores en medias cuestan ~11× los errores en varianzas) y
DeMiguel–Garlappi–Uppal 2009 ya calculan las ventanas de siglos. Lo único salvable es Φ,
y **solo si deja de ser una medición y pasa a ser una desigualdad**:

> (información de Fisher sobre θᵢ) × (peso decisional de θᵢ) ≤ C, uniformemente sobre una
> clase de modelos.

En palabras del auditor: *si no pueden demostrar esa desigualdad, A no es un principio,
es una anécdota con dos decimales.* w=0,90 → 0,55, reclasificado como objetivo pendiente.

**N16 baja a corolario.** Phillips–Yu 2005 y Tang–Chen 2009 / Yu 2012 ya publicaron que
el sesgo de κ̂ es O(1/T) en el *span* y no se reduce con la frecuencia — eso es literalmente
el piso de nuestra torre, un nivel por encima del precio. Pástor–Stambaugh 2012 publicó su
consecuencia. Lo único no publicado es **la recursión como recursión**, y para ser un
resultado hay que demostrar que SE/θ ∝ 1/√T es *invariante de nivel* en una jerarquía de k
niveles, con constante explícita. No basta hacerlo en el nivel 2 de Heston y afirmar que
sigue. w=0,93 → 0,60.

## El trabajo a superar

**Pástor & Stambaugh (2012), «Are stocks really less volatile in the long run?»,
*Journal of Finance* 67(2):431–478.**

Es el mismo programa, ejecutado en 2012: toma el riesgo a horizonte largo, se niega a
tratar los parámetros como conocidos, descompone la incertidumbre en componentes
epistémicos y concluye con un número que invierte la sabiduría convencional. La
diferencia: ellos bayesianos sobre varianza predictiva, nosotros frecuentistas sobre
medidas de cola.

Hay que tratarlo como rival, no como cita de contexto.

## Lo que queda vivo

**N28 — la cola del error del modelo de riesgo. NO ENCONTRADO.** Es la pieza más limpia
de las cinco. La literatura de *model risk of risk models* (Danielsson–James–Valenzuela–Zer
2016) mide dispersión **entre** modelos, no la forma de la cola de la distribución del
error **de un modelo dado**.

Encargo del auditor: no reportar una razón RMSE/mediana de 8,7, sino **derivar el índice
de cola de la distribución del error de ES**, ligándolo analíticamente al error de
estimación del parámetro de persistencia. El error de ES es aproximadamente exponencial en
el error de persistencia por el horizonte, lo que produce lognormalidad o cola de potencia
de forma mecánica. Eso es enunciable en una frase y es falsable.

**N24 — la frontera M2=1.** Vivo pero mal protegido, con un flanco serio: **Hall & Yao
2003** demuestran que en GARCH con errores de cola pesada el QMLE tiene límites no
normales y tasas más lentas que √T precisamente cuando fallan los momentos relevantes. Si
nuestro sesgo plano de 10 a 80 años es la no regularidad de Hall–Yao heredada por el
estimador plug-in de M2, entonces está publicado desde 2003 y solo lo hemos redescubierto.

Encargo: reconciliar el sesgo plano con la tasa O(1/T) de Francq–Zakoïan 2004 y con las
tasas no-√T de Hall–Yao 2003, y después **demostrar una cota inferior minimax de Le Cam**
sobre un entorno de M2=1 que se encoge con T — dos puntos M2 = 1 ∓ cT^(−a), y probar que
ninguna sucesión de tests los separa con probabilidad → 1.

> Una meseta de RMSE es una observación; una cota de Le Cam es un teorema. Es la
> diferencia entre «no lo conseguimos» y «no se puede».

## Donde discrepo del auditor

El auditor advierte que N27 contradice a Danielsson–Zigrand 2006 y Wang–Yeh–Cheng 2011,
que encuentran que el modelo simple se equivoca **más** al alargar el horizonte.

**No hay contradicción, y creo que el auditor confundió los horizontes.** Esos dos
trabajos evalúan la regla de la raíz del tiempo a **10–30 días**. Nuestro cruce ocurre
entre 1 mes y 1 año. Y en nuestra propia tabla, **a 1 mes el resultado coincide con el
suyo**: el modelo sofisticado gana con sesgo −1,0% frente al −36,3% del GBM. Los dos
resultados son el mismo fenómeno medido a los dos lados del cruce.

Lo que sí acepto es la segunda mitad de la objeción: evaluamos contra un DGP que nosotros
mismos simulamos. Pero eso, bien mirado, **refuerza** el resultado en vez de debilitarlo,
y se puede demostrar: el DGP verdadero pertenece a la familia del modelo 3, que por tanto
está **bien especificado**. Si un modelo bien especificado pierde contra uno mal
especificado, la derrota es **puramente error de estimación**, que es exactamente la tesis.

Test decisivo: dar al modelo 3 los parámetros verdaderos (oráculo) y comparar contra el
mismo modelo 3 estimado. Si el oráculo gana en todos los horizontes y el estimado pierde
contra el GBM a 10 años, N27 queda establecido como fenómeno de estimación y la objeción
del artefacto desaparece. Se ejecuta a continuación.
