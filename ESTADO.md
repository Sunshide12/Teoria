# Estado tras ocho ciclos

Balance honesto. Veinticuatro agentes desplegados, tres auditorías de novedad independientes,
**seis resultados propios retractados**.

---

## Lo que se retractó, y por qué

| resultado | ciclo | motivo |
|---|---|---|
| La frontera Artzner/Rockafellar es la de Girsanov | C2 | Publicado: Rockafellar–Uryasev–Zabarankin 2006 |
| El mecanismo de la complejidad óptima | C4 | El test que propuse para defenderlo lo refutó |
| El diagnóstico sesgado hacia la calma | C4 | Error factual mío sobre el parámetro del generador |
| La autoviolación del modelo de cola | C5 | Publicado (premisa de Ma–Wei 2025) **y** non sequitur medido |
| T3, el horizonte de determinación del signo | C7 | Publicado (Dowd–Blake–Cairns 2004) **y** enchufar un IC no es propagar incertidumbre |
| T5, la incoherencia axiomática | C8 | Publicado (Danielsson–Zigrand 2006) **y matemáticamente falso** |

Y un nodo que no era nuestro y sostuvo cinco ciclos: **`n_eff = T/H` está literal en
Danielsson 2002 §3.5**, con ejemplo numérico.

Todo queda en el repositorio con el mismo detalle con que se escribió. El registro de lo que
no funcionó es la parte del método que no se puede reconstruir después.

## Lo que queda en pie

### 1. El punto de cruce especificación/estimación — lo más sólido

La auditoría del ciclo 6 lo señaló como el nodo de mayor valor del grafo, y el ciclo 7 lo
cerró:

```
ε*(H) = √(H/T) / (k_α − Ŝ√H) · √(1 + h₀/H)
```

**La especificación domina si y solo si el modelo yerra más del ε\* del número que reporta.**
Verificado exacto —predicho igual a medido a tres decimales— en 7 generadores × 7 horizontes.

El cruce, medido por tipo de error de modelo (T=10a): colas gordas **19 días** · saltos
**38d** · memoria larga **76d** · saltos asimétricos **100d** · vol estocástica **0,83a** ·
vol apalancada **3,15a** · **nivel de volatilidad a la deriva: nunca cruza**.

**Cruce de capital en 34 días.** A diez años, arreglar por completo la especificación mueve
**1,142×** —ruido por nuestra propia regla— frente al **2,111×** del error de estimación. La
relación de palancas pasa de 1,05 a favor de especificar a **7,9 a favor de estimar**.

> En el libro de negociación, el presupuesto de modelización va a especificar mejor. En ECL
> vitalicia y pensiones, **todo gasto en especificar la cola es sofisticación asignada a un
> efecto del 14%**.

**Y el rival, auditado por texto íntegro:** Kerkhof–Melenberg–Schumacher 2010 concluyen lo
contrario, pero su aplicación es literal *«T = 1/252 (one day)»* y su única aplicación
plurianual es **delta-cubierta**, neutral a la deriva por construcción. **El canal de la
deriva está ausente de su diseño: su ordenación no es un hallazgo, es forzada.**

### 2. La banda de capital libre de dato

| | valor |
|---|---|
| rango del ES₉₉ a 1 año sobre convenios defendibles | **3,39×** — y los dos ejes son ortogonales |
| a 10 años | **el signo cruza cero** (de −0,120 a +1,444) |
| banda de estimación sobre el número reportado a 10 años | **147%** (frente al 0,79% a 10 días) |

**Lo que nadie cierra**: que como la brecha es μH y μ no es estimable a la precisión necesaria
—983 años con σ=16%—, **la brecha no es un error corregible sino una banda irreducible**.
Dowd–Blake–Cairns dicen «toma una postura»; Danielsson–Zigrand lo mencionan y lo sueltan.

### 3. La cota que se rompe, y por qué importa

La cota de bolsillo `0,27·√(H/T)`, verificada en el ciclo 5 con ratio 1,01–1,06 bajo
estacionariedad, **cubre el 35% a un año y el 43% a diez de un 90% nominal** en cuanto el
nivel de volatilidad está a la deriva.

> **Y saber si lo está es precisamente lo indecidible.** La segmentación binaria encuentra
> 3,97 rupturas en una serie estacionaria que no tiene ninguna — el mismo número que en una
> con cuatro reales.
>
> Una cota cuyo dominio de validez no es verificable no es utilizable. Y una que no cubre es
> peor que no reportar nada.

### 4. El algoritmo

Escalera fija de ventanas (1, 2, 5, 10, 20 años y muestra completa) con regla del **segundo
mayor**, medida en el régimen no estacionario:

| | capital | déficit p95 | P(infraestimar) |
|---|---|---|---|
| práctica vigente | 0,945× | 1,595 | 50,0% |
| escalera + 2º mayor | 1,322× | **0,420** | 31,7% |
| algoritmo completo | 1,480× | **0,000** | **3,3%** |

**3,8× menos déficit por un 32% más de capital.** El algoritmo completo elimina el déficit
pero cuesta un 48% más: no es gratis.

Y lo que vale más que el algoritmo: **un parámetro no identificado no se estima. Se fija por
convenio y se declara el convenio.** Lo esencial no es publicar el rango sino **mover la
propiedad del grado de libertad**.

### 5. El sesgo bajista es del horizonte, no de la ventana

A un año no existe (ratios 1,032 y 1,019). A diez años los procedimientos convencionales dan
**0,945 y 0,892** e infraestiman el **50% y 63%** de las veces. Mecanismo: a horizonte largo
el término −μH domina y el ruido de μ̂ entra **restando**.

**Consecuencia: acotar la dispersión de la ventana no corrige nada.**

## Los rivales, todos encontrados por los propios agentes

| trabajo | qué contiene |
|---|---|
| **Danielsson (2002)**, JBF 26(7) | la tesis cualitativa entera; y `n_eff=T/H` literal en §3.5 |
| **Danielsson–Zigrand (2006)**, JBF 30(10) | que √t falla **por la deriva**, «well-known», con §4 dedicada |
| **Dowd–Blake–Cairns (2004)**, JRF 5(2) | el cruce por cero, el pico, la sensibilidad a μ, y «toma una postura» |
| **Pástor–Stambaugh (2012)**, JF 67(2) | el mismo programa, bayesiano, con la maquinaria correcta |
| **Kerkhof et al. (2010)**, JBF 34 | la ordenación contraria — forzada por su diseño a un día |
| **DJVZ (2016)**, JFS 23 | el risk ratio entre modelos, mayor que el nuestro entre ventanas |
| **Welch (2025)**, SSRN 5709087 | mismo rango de horizontes, mismo mensaje |

## Lo que la investigación aprendió sobre sí misma

**El umbral de impacto.** La regla de que por debajo de 1,3× es ruido mató dos líneas enteras
—la frontera de cuarto momento movía 1,011×— y se aplicó luego a resultados propios sin
excepción, incluido el algoritmo.

**Auditar antes de construir.** La frontera de cuarto momento sobrevivió cuatro ciclos porque
la auditoría llegó tarde. T3 y T5 murieron en el mismo ciclo en que se propusieron, porque
se lanzó un agente a auditarlos antes de escribir encima.

**Las retractaciones valen más que los resultados.** De seis, cuatro fueron por precedente
publicado y dos por error propio. Las dos de error propio —el mecanismo refutado por su
propio test, y la biyección aplicada sin comprobar su condición— son las que enseñan algo.

## Lo que falta

- **Cerrar la grieta del eje E**, abierta tres ciclos: qué sobrevive sin estacionariedad.
- **El protocolo de falsación**: qué observación concreta, con qué fecha y qué criterio,
  refutaría cada afirmación viva.
- **La síntesis final**, construida sobre lo que quede y confrontando a los siete rivales en
  el primer párrafo.
