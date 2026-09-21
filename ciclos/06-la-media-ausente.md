# Ciclo 6 — La media ausente

**Pregunta:** integrar y medir el algoritmo completo, y confrontar la investigación con
Danielsson (2002) para determinar qué añade la cuantificación.

**Agentes:** G1 el algoritmo · G2 la confrontación · G3 adversarial. **G1 y G3 cayeron por
límite de sesión; asumí sus dos papeles**, como en el ciclo 4.

**Respuesta corta:** lo único que esta investigación añade a veinticuatro años de literatura
es un parámetro que nadie menciona. Y con él sale una fórmula cerrada.

---

## 1. El hallazgo, verificado por extracción íntegra

G2 leyó los PDF completos en vez de citarlos de segunda mano:

> **Cero ocurrencias de «mean / expected return / drift» en las 30 páginas de Danielsson
> (2002) y en las 34 de Danielsson–James–Valenzuela–Zer (2016).**

Toda la literatura de riesgo de modelo cuantifica dispersión de cola con **μ ≡ 0 por
convención, y nunca lo dice**. Con μ≡0 el ES nunca cruza cero y el criterio de T3 no puede
aparecer.

**El resultado estaba escondido detrás de una convención que nadie declara como tal.**

## 2. Lo que se cae, y duele

| nodo | estaba en | nuevo peso |
|---|---|---|
| **N03** — `n_eff = T/H` | **Danielsson 2002 §3.5, literal**, con ejemplo numérico | 0,96 → **0,55** |
| N59 — frontera de falsabilidad | endurecimiento ×3,80 de sus «3.000 días» | 0,92 → 0,75 |
| N61 — componente sistemático de ventana | recuperable de su Tabla 2 (1,38–1,44×) | 0,90 → 0,75 |
| N80 — «la aportación es N74» | incorrecto: el eje ventana está prefigurado | 0,90 → 0,70 |

`n_eff = T/H` fue el nodo más sólido durante cinco ciclos, el único que salía reforzado de
cada uno. Nunca fue nuestro. Sobrevive la verificación numérica —n=1.070 medido contra 1.140
predicho— no el concepto.

Y **una recomendación publicada que sí contradecimos**: Danielsson 2002 §3.4 concluye que
«longer estimation horizons are preferred». N86/N87 miden lo contrario. Un desacuerdo medido
con una recomendación en JBF vale más que cien glosas.

## 3. Tres errores numéricos nuestros, corregidos

- **N71**: «5-min → 1,6 horas» es falso. 3,55 barras de cinco minutos son **17,8 minutos**.
  Factor 5,4 de discrepancia.
- **N81**: el bolsillo solo ajusta a horizonte largo — predice 0,025 frente a 0,054 a un mes.
  Dominio declarado: H ≥ 1 año.
- **N84**: p95 y p99 analíticos exceden los medidos en 6–13%. **La cola del error es más
  delgada que lognormal.** Solo el p90 es robusto.
- **N73**: «400 años para fijar μ a ±1%» suponía σ=10%. Con σ=16% son **983 años**. El nodo
  subestimaba su propio hallazgo 2,5×.

## 4. T3 — el resultado principal

Salió de tirar del hilo que G1 dejó antes de caer: *«la cota sobreestima el error una vez μ
se declara»*.

Es cierto, y medido: a diez años declarar μ reduce la desviación del ES de 0,5063 a 0,0190
—**factor 26,7**— pero introduce un sesgo (μ_dec − μ_real)·H de 0,40 si el convenio yerra
cuatro puntos. **El error total no baja: cambia de ruido invisible a sesgo declarado.** Y eso
importa porque el sesgo es auditable y el ruido no.

Tirando de ahí:

```
ES_{α,H} = −μH + k_α·σ·√H     cruza cero en    μ* = k_α·σ/√H
```

y el signo está indeterminado cuando μ* cae en el IC de μ̂. **Dividiendo por σ, la volatilidad
desaparece:**

> ```
> | Ŝ − k_α/√H | < z_{γ/2}/√T        ⟹        H* = [ k_α / (Ŝ + z/√T) ]²
> ```

Verificado con 200.000 réplicas: `P(ES<0)` pasa de 0,5% a H=5 años, a 2,5% justo en H\*=7,18,
a 6,9% a H=10 y a 24,4% a H=20.

Con Sharpe típico de renta variable y diez años de datos, **el signo del ES₉₉ está determinado
hasta 7,2 años y no más allá**. Con cien años, hasta 21,8. IFRS-9 y las proyecciones de
pensiones quedan fuera, y ninguna serie histórica disponible las mete dentro.

Detalle completo en `teorema/T3-horizonte-de-determinacion.md`.

## 5. La cota se rompe, y el círculo se cierra

Asumiendo el papel de G3, medí la cota de bolsillo bajo el régimen **no estacionario**:

| | cobertura nominal | medida |
|---|---|---|
| `0,27·√(H/T)` a 1 año | 90% | **35,0%** |
| `0,27·√(H/T)` a 10 años | 90% | **43,3%** |

La pieza constructiva del ciclo 5, verificada allí con ratio 1,01–1,06, **cubre menos de la
mitad de lo que promete** en cuanto el nivel de volatilidad deja de ser estacionario.

Y aquí se cierra el círculo del trabajo entero:

> La cota solo vale si el proceso es estacionario. Y saber si lo es es precisamente lo que
> N60 demuestra que no se puede saber — la segmentación encuentra 3,97 rupturas en una serie
> estacionaria que no tiene ninguna, el mismo número que en una que tiene cuatro reales.

**Una cota cuyo dominio de validez no es verificable no es utilizable. Y una que no cubre es
peor que no reportar nada, porque da falsa confianza con aspecto de rigor.**

## 6. El sesgo bajista: confirmado, y mal atribuido

| H = 10 años | capital/verdad | déficit p95 | P(infraestimar) |
|---|---|---|---|
| práctica vigente (ventana 2a) | 0,945 | 1,595 | 50,0% |
| muestra completa | **0,892** | 0,561 | **63,3%** |
| escalera + 2º mayor | 1,322 | 0,420 | 31,7% |
| algoritmo completo | 1,480 | **0,000** | **3,3%** |

A un año no hay sesgo (1,032 y 1,019). A diez años lo hay y es grande. **El sesgo bajista es
del horizonte, no de la ventana** — N88 lo atribuyó mal. El mecanismo es el de T3: a horizonte
largo el término −μH domina, el ruido de μ̂ entra **restando**, y el ES sale sistemáticamente
pequeño. Crece como H mientras la cola crece como √H.

**Consecuencia:** acotar la dispersión de la ventana no corrige nada. El frente que se
planteaba como el ataque más peligroso al entregable acierta en la conclusión y se equivoca
en la causa.

## 7. El algoritmo: funciona, y cuesta

La escalera con regla del segundo mayor reduce el déficit p95 de 1,595 a 0,420 —**factor
3,8**— por un 32% más de capital. Eso **recupera** el resultado que la medición del ciclo 5
había descartado por debajo del umbral (1,27×), porque aquella medía en régimen estacionario
y esta en el que de verdad no se puede descartar.

El algoritmo completo lleva el déficit a **cero** con probabilidad de infraestimar del 3,3%
frente al 50–63% de lo vigente, **a cambio de un 48% más de capital**. No es gratis, y decir
lo contrario sería el mismo error cometido ya tres veces en este trabajo.

## 8. El párrafo que G2 escribió, y que el entregable tiene que llevar

> Daníelsson (2002) demostró que los modelos de riesgo no son robustos, que las propiedades
> del dato cambian al ser observadas y que el análisis en calma no informa sobre la crisis.
> Su evidencia, y la de toda la literatura que le siguió, se sitúa en horizontes de uno a
> diez días y mantiene la media de los retornos fijada en cero por convención: **ninguno de
> esos trabajos menciona el parámetro de deriva**. Este trabajo muestra que esa convención,
> correcta donde fue validada (sesgo del +3,9% a diez días), induce un sesgo del +146% a diez
> años y deja el ES₉₉ **con el signo indeterminado**. La consecuencia no es que el riesgo de
> modelo sea mayor de lo medido en 2016, sino que en los horizontes que IFRS-9 y Solvencia II
> exigen **la métrica de aquel trabajo deja de estar definida**, y el orden entre riesgo de
> especificación y riesgo de estimación se invierte.

## Salida hacia el ciclo 7

Tres frentes, y el primero es el que decide si hay trabajo o no:

1. **Auditar la novedad de T3.** La polémica de «time diversification» (Samuelson, Bodie 1995)
   lleva décadas discutiendo si el riesgo baja o sube con el horizonte. Si T3 es esa polémica
   con vocabulario nuevo, se cae.
2. **El punto de cruce exacto de N57**, que la auditoría señaló como el nodo con más valor.
3. **Romper T3**: μ constante, normalidad del cuantil, si truncar a cero salva el problema, y
   si la circularidad declarada es profunda o vacía.
