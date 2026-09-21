# T5 — La incoherencia axiomática

*Síntesis de siete ciclos. No es un teorema nuevo: es una composición de piezas conocidas
que produce una afirmación que no he encontrado hecha, y un número.*

---

## La cadena

**1.** Una medida de riesgo que se usa como **capital** debe ser aditiva en efectivo
(Artzner–Delbaen–Eber–Heath 1999):

```
ρ(X + c) = ρ(X) − c
```

**2.** Una medida de **desviación** es invariante a traslación
(Rockafellar–Uryasev–Zabarankin 2006):

```
D(X + c) = D(X)
```

**3.** Y las dos clases están en correspondencia biunívoca, **difiriendo exactamente en la
media**:

```
D(X) = R(X − E[X])
```

**4.** La regla de la raíz del tiempo reporta `k_α·σ·√H`, que **no contiene μ**. Por el punto
2, eso es una **desviación**.

**5.** Y ese número se usa como capital, donde el punto 1 exige una medida **aditiva en
efectivo**.

> **La brecha entre lo que se reporta y lo que se necesita es exactamente μH: el parámetro
> que la auditoría del ciclo 6 verificó ausente de las 64 páginas de la literatura de riesgo
> de modelo.**

## El número

La brecha relativa es adimensional y la volatilidad se cancela:

```
brecha = μH / (k_α·σ·√H) = Ŝ·√H / k_α
```

| horizonte | Ŝ=0,20 | Ŝ=0,375 | Ŝ=0,50 | Ŝ=0,80 |
|---|---|---|---|---|
| 10 días | 1,5% | **2,8%** | 3,7% | 6,0% |
| 1 año | 7,5% | 14,1% | 18,8% | 30,0% |
| 5 años | 16,8% | 31,5% | 41,9% | 67,1% |
| **10 años** | 23,7% | **44,5%** | 59,3% | 94,9% |
| 20 años | 33,6% | 62,9% | 83,9% | 134,2% |
| **30 años** | 41,1% | **77,1%** | 102,8% | 164,4% |

Y en multiplicador de capital, con Ŝ=0,375 y σ=16%:

| horizonte | ES correcto | `k·σ·√H` reportado | ratio |
|---|---|---|---|
| 10 días | 0,0826 | 0,0849 | **1,029×** |
| 1 año | 0,3664 | 0,4264 | 1,164× |
| 10 años | 0,7485 | 1,3485 | **1,802×** |
| 20 años | 0,7071 | 1,9071 | 2,697× |
| 30 años | 0,5357 | 2,3357 | **4,360×** |

> **A diez días la convención es correcta: la brecha es del 2,8% y Basilea la validó ahí.
> A diez años es casi la mitad del número. A treinta, tres cuartas partes.**

## Lo que esto dice, que es más preciso que «el riesgo a largo plazo es incognoscible»

El número reportado **no es una estimación sesgada del capital**. Es un objeto de otra clase
axiomática con el nombre de la primera. Y el cambio de clase no está declarado en ninguna
parte: se produce al adoptar una convención de escalado que nadie presenta como un supuesto
sobre la prima de riesgo.

La consecuencia no es que haga falta más precisión. Es que **la cantidad que se está
midiendo no es la cantidad que se necesita**, y la diferencia entre ambas es exactamente el
parámetro que no se menciona.

## La ironía, que conviene dejar escrita

El ciclo 2 presentó como su resultado más limpio que «la frontera Artzner/Rockafellar es la
frontera de Girsanov». La primera auditoría de novedad lo tumbó sin contemplaciones: es el
teorema de Rockafellar–Uryasev–Zabarankin 2006 con vocabulario nuevo encima. Bajó de w=0,93
a w=0,25 y se reclasificó como reformulación pedagógica.

**Cinco ciclos después, ese mismo teorema resulta ser el instrumento que explica el hallazgo
central.** No era nuestro resultado. Es nuestra herramienta.

El auditor tenía razón en tumbarlo como aportación, y el trabajo tenía razón en haberlo
buscado.

## Alcance honesto

Nada de la matemática es nuestro:

- La axiomática de medidas coherentes: **Artzner–Delbaen–Eber–Heath 1999**.
- La correspondencia desviación/coherente: **Rockafellar–Uryasev–Zabarankin 2006**.
- Que √t equivale a suponer deriva cero: folclore de mesa, y en forma de opción en
  **Bodie 1995** (FAJ 51(3):18–22).
- Que la incertidumbre de μ domina el riesgo a largo plazo: **Pástor–Stambaugh 2012**.
- Que el VaR de horizonte largo cruza cero: **Dowd–Blake–Cairns 2004**.

**Lo que queda como aportación son tres cosas, y son modestas:**

1. **La ausencia verificada** (N91): cero ocurrencias de «mean / expected return / drift» en
   el texto íntegro de Danielsson (2002), 30 páginas, y de Danielsson–James–Valenzuela–Zer
   (2016), 34 páginas. Verificado por extracción, no por cita.
2. **La composición**: que esa ausencia no es un olvido sino un cambio de clase axiomática no
   declarado, y que la brecha es exactamente `Ŝ√H/k_α`.
3. **La medición**: 2,8% a diez días, 44,5% a diez años, 77,1% a treinta; y en capital,
   1,029× / 1,802× / 4,360×.

## Lo que hay que auditar antes de reclamarlo

La composición parece demasiado simple para no estar hecha. Hay que buscar específicamente:
si alguien ha señalado que la regla de escalado temporal convierte la medida de capital en
una medida de desviación, y si alguien ha cuantificado la brecha. El ciclo 8 lo audita.

## Por qué solo se puede corroborar con los años

La brecha es `μH`, y μ no es estimable a la precisión necesaria en menos de **983 años** con
σ=16% (N73). Saber cuánto vale exactamente la brecha exige saber μ; saber μ exige esperar.

Lo que **sí** se puede hacer hoy —y es lo que el algoritmo propone— es **declarar μ como
convenio publicado** en vez de fijarlo a cero en silencio. Eso no reduce el error: lo
convierte de ruido invisible en sesgo auditable (N98). Y el sesgo auditable es el que, con
los años, alguien podrá comprobar.
