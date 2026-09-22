# Estado tras diez ciclos

Balance final. **Treinta agentes desplegados** (tres murieron por límite de tasa y asumí
su papel), cuatro auditorías de novedad independientes, **once resultados propios
retractados** — el último por el agente al que le encargué matarlo.

---

## Lo que se retractó, y por qué

| # | resultado | ciclo | peso que llevaba | motivo |
|---|---|---|---|---|
| 1 | la frontera Artzner/Rockafellar es la de Girsanov | C02 | **0,93** | publicado: Rockafellar–Uryasev–Zabarankin 2006 |
| 2 | el mecanismo de la complejidad óptima | C04 | 0,85 | el test que propuse para defenderlo lo refutó |
| 3 | el diagnóstico sesgado hacia la calma | C04 | — | error factual mío sobre el parámetro del generador |
| 4 | T2, la autoviolación del modelo de cola | C05 | 0,88 | publicado (premisa de Ma–Wei 2025) **y** non sequitur medido |
| 5 | N91, «cero ocurrencias de drift en 64 páginas» | C06 | **0,92** | error de muestreo **nuestro**: extrajo los dos artículos donde no está |
| 6 | T3, el horizonte de determinación del signo | C07 | **0,90** | publicado (Dowd–Blake–Cairns 2004) **y** enchufar un IC no es propagar incertidumbre |
| 7 | T5, la incoherencia axiomática | C08 | 0,85 | publicado (Danielsson–Zigrand 2006) **y matemáticamente falso** |
| 8 | T_req = 55,8 años | C08 | **0,92** | publicado: Noguer i Alonso 2026, ec. (21) |
| 9 | el techo T_eff ≤ T/ρ̄ | C08 | **0,93** | publicado: Giller 2024, ecs. (17)–(18) |
| 10 | la firma de revisión, ratio 48× | C08 | **0,90** | publicado (Richards et al. 2012) **y el 48× era falso: medido 3,04×** |
| 11 | **el aparato entero de T6** | C09 | **0,94** | **el agente adversarial del C10**: la banda es una identidad, T_det sale de un barrido con nivel efectivo del 15–25%, los 11.707 años tienen IC (49 , 181.757), y T_est no era portante |

**Seis de las once se escribieron con `w ≥ 0,90`.** La etiqueta está bien calibrada —tasa
de fallo empírica 8,8%— y no protegió ninguna. Lo que las mató fue, en siete casos, una
búsqueda bibliográfica que no se había hecho; en los otros cuatro, un error aritmético o
metodológico propio que sólo apareció al intentar defenderlo.

Y un nodo que no era nuestro y sostuvo cinco ciclos: **`n_eff = T/H` está literal en
Danielsson 2002 §3.5**, con ejemplo numérico.

---

## Lo que queda en pie

### 1. El punto de cruce especificación/estimación — lo más sólido del repositorio

```
ε*(H) = √(H/T) / (k_α − Ŝ√H) · √(1 + h₀/H)
```

**La especificación domina si y solo si el modelo yerra más del ε\* del número que
reporta.** Verificado exacto —predicho igual a medido a tres decimales— en 7 generadores ×
7 horizontes.

El cruce, medido por tipo de error de modelo (T=10a): colas gordas **19 días** · saltos
**38d** · memoria larga **76d** · saltos asimétricos **100d** · vol estocástica **0,83a** ·
vol apalancada **3,15a** · **nivel de volatilidad a la deriva: nunca cruza**.

**Cruce de capital en 34 días.** A diez años, arreglar por completo la especificación mueve
**1,142×** —ruido por nuestra propia regla— frente al **2,111×** del error de estimación.

> En el libro de negociación, el presupuesto de modelización va a especificar mejor. En ECL
> vitalicia y pensiones, **todo gasto en especificar la cola es sofisticación asignada a un
> efecto del 14%**.

**Y el rival, auditado por texto íntegro:** Kerkhof–Melenberg–Schumacher 2010 concluyen lo
contrario, pero su aplicación es literal *«T = 1/252 (one day)»* y su única aplicación
plurianual es **delta-cubierta**. **Su ordenación no es un hallazgo: es forzada.**

### 2. La ley exacta del exceso de revisión

```
Var(ΔÊS | μ̂) − Var(ΔÊS | μ≡0) = H² · 2σ²/T²
```

Es una **igualdad**, no una desigualdad. Medido/teórico sobre reestimaciones anuales
reales: **1,054 · 1,165 · 1,110** (registro entero) y **1,100 · 1,029 · 1,076** (sólo el
tramo estacionario). Es la única pieza del protocolo ya verificada, y por eso es el
control: si falla, ningún otro veredicto significa nada.

Corroboración externa que no nos buscaba: la Fed publica revisiones interanuales del
*stress capital buffer* que implican σ ≈ **21,0%** del nivel, frente al **20,4%** que
predice la aritmética. Con dos advertencias que la propia fuente obliga a poner.

### 3. T6, recortado hasta donde aguantan los datos

> Para el mercado total estadounidense, la Sharpe realizada sobre cualquier ventana de 10 a
> 95 años es indistinguible de `k_α/√10 = 0,8428` (**Ŝ=0,8247, t=0,167, p=0,87**). El signo
> del `ES₉₉` a diez años corregido por media no está determinado por la muestra, y el
> intervalo de horizontes indeterminados —**imagen exacta del IC de Ŝ**— es (6,6 , 19,0)
> años, que cubre la ECL y el ALM de pensiones.

Robusto a la ventana, al test de ruptura, al estimador predictivo (que lo **ensancha un
40%**) y al `k_α` empírico (2,54–3,04, ruido). **No se reproduce en 12 de 16 mercados.** Y
**cuál de los cinco Ŝ defendibles se use cambia qué horizontes entran**: sólo H=15 cae
dentro bajo los cinco.

### 4. Y el resultado de segundo orden, que es el más honesto

`SE(Ŝ) = 0,126` ⇒ `H⁻ ∈ [4,31 , 11,35]`, `H⁺ ∈ [9,64 , 53,02]`.

**Para H = 5, 7, 10, 15, 20 y 30 la pertenencia a la banda es indecidible.** No se puede
determinar qué horizontes están en la región donde nada se determina. Es el teorema
aplicado a sí mismo.

### 5. El algoritmo

`motor/banda.py` — 1.097 líneas, 21/21 pruebas. Su virtud no es calcular: es **negarse a
calcular**. Si el paso 0 detecta ruptura en la media, devuelve `None` en los pasos 1–6. Si
H cae dentro de la banda, `ES_punto = None`.

### 6. El protocolo

`protocolo/` — seis predicciones fechadas hasta 2082, selladas con SHA-256, con puerta
bibliográfica que corre **antes** que el test empírico. `python3 protocolo/resolve.py`
imprime PASS/FAIL/VOID/MOOT/ESPERA. P-2 pasa hoy.

---

## Lo que no se consiguió

- **El estrato regulatorio/actuarial sigue abierto**, y el ciclo 10 demostró que no se
  cierra con muestras disjuntas: eso rompe la homogeneidad de captura que Chapman exige.
  Hace falta una tercera muestra con las **mismas** consultas, o sorteadas del mismo
  universo. Es una tarea acotada, y está sin hacer.
- **Ninguna afirmación de novedad es admisible** mientras eso siga así. T6 queda en el
  repositorio como lo que es: una conjetura fechada, sellada y falsable, con su propia
  demolición escrita al lado.
- **T6 es en la práctica infalsificable por la ruta que él mismo ofrece.** Casi toda
  corrección de robustez añade incertidumbre y por tanto lo refuerza. Queda escrito, porque
  si no, cada réplica que «lo confirma» no aporta información.
- **Tres agentes murieron sin informar** (ciclos 4, 6 y 8). Un ciclo de tres que corre con
  dos no es el diseño.

---

## Para retomarlo

`memoria/GRAFO.md` (159 nodos) y `memoria/MEM.ndx` (10 líneas). Nada más.
