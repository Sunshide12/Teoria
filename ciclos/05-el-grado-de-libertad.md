# Ciclo 5 — El grado de libertad

**Encargo (grieta del C04, eje E):** la línea M2 es irrelevante —mueve 1,011×—. Lo que
mueve la decisión es el error de estimación amplificado por el horizonte. Cuantificarlo y
acotarlo.

**Agentes:** F1 (la cota inferior), F2 (la ventana), F3 (el invariante).
`κ = 0,71` · centroide `[.88, .66, .78, .58, .94, .90]` · grieta **E** (σ=0,34).

*Informe reconstruido en el ciclo 10 desde el grafo y los informes verbatim de
`c05-raw/`, para cerrar un hueco en el registro.*

---

## F3 — el invariante que cancela todo

```
var(ÊS_H) = H²σ²/T  +  H·k²σ²/(2fT)
```

Los dos términos —deriva y cola— se igualan en **3,55 observaciones**, y al igualarlos
**se cancelan T, σ y la unidad de muestreo**. La cuota de la deriva: 22,0% a 1 día, 85,5%
a 1 mes, 98,6% a 1 año, **99,86% a 10 años**.

Con una consecuencia perversa: **muestrear más rápido adelanta el cruce**. A cinco
minutos, 3,55 barras son **17,8 minutos**. Más datos hacen el problema *más* puramente de
media, nunca menos.

Y el cierre lógico del ciclo 4 (N72): la región donde el ES es falsable está **contenida**
en la región donde domina el sesgo de especificación. Donde es falsable está sucio; donde
está limpio ya no es falsable. **Falsabilidad y especificidad-de-cola se apagan juntas.**

## F1 — la cota, y que se alcanza

```
RMSE_rel(ÊS) ≥ √[ (s_μ/c_q)²(H/n) + (λ_H/2)²g'Σ̂g + (∂log c_q/∂ν)²SE(ν̂)² ]
```

Vale 5,4% / 12,4% / **30,8%** a 1 mes / 1 año / 10 años con T=10a. **Y se alcanza:** 800
ajustes MLE dan 5,5% / 12,0% / 32,6%, ratio 1,01 / 0,97 / 1,06.

De ahí dos cosas que sobrevivieron:

- **El tope de saturación del canal volatilidad** es `(1−β)/(1−π)`: medido 4,50 frente a
  4,51 analítico. **La persistencia no puede explicar un crecimiento de 12,5×.**
- **El multiplicador de capital por error de estimación**: fijar capital en el p90 del
  error en vez del punto estimado multiplica por **1,45× a 10 años**, frente a 1,073× a un
  mes. Con T=10a: FRTB 10d → 1,02× · Solvencia II 1a → 1,17× · **ECL vitalicia 10a →
  1,45×** · con 5 años de datos **1,63×** · con 3 años **1,89×**.

> La frontera M2 del ciclo 4 movía **1,011×**. Esto mueve cuarenta veces más.

## F2 — la ventana no es continua

`T*(H)` **salta**. La prima de recencia decae con el horizonte mientras el coste de ser
corto no depende de él; al cruzarse, el mínimo global brinca de la rama corta a «toda la
muestra». Locus `H_c = 1,4·τ`, **factor de salto 57–459×**. Es una transición de primer
orden en el argmin.

Y la condición exacta de **«más datos perjudican»**: `L(T_max) > L(T) ⟺ T·T_max > T*²`.
Con `T = T*`, todo exceso de muestra es estrictamente dañino y el daño crece sin cota.

## El resultado del ciclo: N74

**Capital libre de dato.** Las dos cuotas son **ortogonales** (rango total 3,39× frente al
producto de medios 3,28×, 3% de discrepancia).

> A un año, un factor de **3,4** en el capital regulatorio no está fijado por ningún dato:
> sólo por dos convenciones no declaradas — la ventana de estimación (2,13–2,79×) y la
> deriva declarada (1,21–1,59×).
>
> A diez años **ni el signo está determinado**: el ES₉₉ va de **−0,120** (μ=8%, ventana
> 2a) a **+1,444** (μ=0%, ventana 50a). De esperar una ganancia en el 1% peor a perder el
> 76% del valor, con los mismos datos.

Comparado con la frontera M2 del ciclo anterior: **1,011×**.

N74 acabó siendo el nodo de mayor peso del grafo (0,96) y el único superviviente del
núcleo tras las auditorías de los ciclos 8 y 9.

## Lo que el ciclo se equivocó, y se corrigió después

- **N73** («√t es exactamente μ=0, y μ no es estimable») se presentó como núcleo. Está
  publicado: Danielsson–Zigrand 2006. Bajó de 0,80 a 0,30. Y sus «400 años» suponían
  σ=10%; con σ=16% son **983**.
- **N81**, la cota de bolsillo `0,27·√(H/T)`, **se rompe bajo no estacionariedad**:
  cobertura medida 35% a un año y 43,3% a diez, de un 90% nominal. Bajó a 0,45.
- **N88** decía que el sesgo bajista era *de la ventana*. El ciclo 6 lo corrigió: es **del
  horizonte**. A un año no existe (1,032/1,019); a diez años los procedimientos
  convencionales dan 0,945/0,892 e infraestiman el 50–63% de las veces.
- **N89**, el aviso más útil contra nosotros mismos: el «risk ratio» entre modelos de
  Danielsson–James–Valenzuela–Zer (media ≈4, hasta 55 en crisis) es **mayor** que el
  nuestro entre ventanas (mediana 2,28×). **La elección de modelo domina a la elección de
  ventana.** Y S mide la anchura, no el error: entre terciles de S el error mediano sólo
  pasa de 0,263 a 0,296. **Es una declaración, no un diagnóstico.**

## Pregunta para el ciclo 6

La aportación es la **cuantificación** —Danielsson 2002 ya tiene la tesis—. Construir el
algoritmo completo y volver irrefutable el factor 3,4×–8,3× de capital libre de dato.
