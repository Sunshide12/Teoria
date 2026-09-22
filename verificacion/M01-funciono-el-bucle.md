# M01 — ¿Funcionó el bucle?

Meta-análisis del método, no del tema. Medido sobre `memoria/GRAFO.md` (146 nodos con
peso) y `memoria/MEM.ndx` (9 ciclos registrados).

---

## 1. No convergió a un eco

El riesgo de diez ciclos de tres agentes es que se den la razón entre ellos. El motor
tiene un umbral explícito: `κ > 0,92` significa que los tres dicen lo mismo con distinto
vocabulario, y dispara un agente adversarial.

| ciclo | κ | modo |
|---|---|---|
| C01 | **0,91** | GRIETA |
| C02 | 0,62 | GRIETA |
| C03 | 0,69 | GRIETA |
| C04 | — | **ADVERSARIAL** |
| C05 | 0,71 | GRIETA |
| C06 | — | **ADVERSARIAL** |
| C07 | 0,72 | GRIETA |
| C08 | — | **ADVERSARIAL** |
| C09 | 0,76 | GRIETA |

El primer ciclo llegó a **0,91**, a un punto del umbral: los tres agentes iniciales
estaban efectivamente repitiéndose. Cayó a 0,62 y volvió a subir despacio hasta 0,76,
sin volver a acercarse. **Media 0,735, máximo 0,91.** El eco no se produjo.

## 2. La grieta sí arrastró el bucle

```
P → P → E → E → E → E → E
```

El eje E —estacionariedad— fue el de máxima divergencia en **cinco ciclos consecutivos**.
El controlador no lo soltó, y eso es probablemente lo más valioso que hizo: **impidió
pasar página**. El ciclo 9 lo cerró con una medición, no con un argumento: sobre la serie
estadounidense el sup-Wald HAC da **16,8–40,7 sobre la volatilidad** (ruptura al 1%) y
**1,67 sobre la media** (crítico 12,35).

La grieta de cuatro ciclos no era conceptual. Era esa asimetría sin medir.

## 3. Lo que costó: diez retractaciones

| # | resultado | ciclo | peso que llevaba | por qué cayó |
|---|---|---|---|---|
| 1 | frontera Artzner/Rockafellar ≡ Girsanov | C02 | **0,93** | publicado (RUZ 2006) |
| 2 | mecanismo de la complejidad óptima | C04 | 0,85 | el test que propuse lo refutó |
| 3 | diagnóstico sesgado hacia la calma | C04 | — | error factual mío sobre el generador |
| 4 | T2, la autoviolación | C05 | 0,88 | publicado **y** non sequitur medido |
| 5 | T3, horizonte de determinación | C07 | **0,90** | publicado **y** error de método |
| 6 | N91, «cero ocurrencias de drift» | C06 | **0,92** | error de muestreo **nuestro** |
| 7 | T5, la incoherencia axiomática | C08 | 0,85 | publicado **y matemáticamente falsa** |
| 8 | T_req = 55,8 años | C08 | **0,92** | publicado (Noguer i Alonso 2026) |
| 9 | techo T_eff ≤ T/ρ̄ | C08 | **0,93** | publicado (Giller 2024) |
| 10 | la firma de revisión, 48× | C08 | **0,90** | publicado (Richards 2012) **y el 48× era falso** |

## 4. La etiqueta de confianza está bien calibrada — y eso no salvó nada

De los 68 nodos que en algún momento llevaron `w ≥ 0,90`, **6 murieron**: tasa de fallo
**8,8%**. La etiqueta significa en la práctica ~0,91. Está calibrada.

**Y es irrelevante.** Seis de las diez retractaciones se escribieron con `w ≥ 0,90`. La
confianza alta no protegió ninguna. Lo que las mató fue, en siete de diez casos, **una
búsqueda bibliográfica que no se había hecho** — y en los tres restantes, un error
aritmético o metodológico propio que sólo apareció al intentar defenderlo.

> La lección operativa del proyecto entero: **la precedencia se busca antes, no después.**
> Seis consultas resolvieron en un día lo que el test empírico habría tardado 56 años.

## 5. La advertencia sobre el trabajo más reciente

Peso medio de los nodos, por ciclo de origen:

| C01 | C02 | C03 | C04 | C05 | C06 | C07 | C08 | C09 |
|---|---|---|---|---|---|---|---|---|
| 0,759 | 0,705 | 0,839 | 0,673 | 0,779 | 0,749 | 0,851 | **0,922** | **0,938** |

Sube de forma monótona desde C06. Parte está justificada —los nodos del C09 son en buena
medida **precedentes verificados por cita textual extraída**, que merecen peso alto— pero
las afirmaciones **propias** del ciclo 9 (N133–N138) promedian **0,94**, más que las de
cualquier ciclo anterior.

Esa es exactamente la condición en la que se escribieron las diez retractaciones de
arriba. **Queda dicho aquí, en el mismo archivo donde se dice que el bucle funcionó.**

## 6. Lo que el bucle no hizo

- **No produjo el resultado que buscaba.** El encargo era «un algoritmo no contemplado
  hasta ahora». Lo que produjo fue una máquina de tumbar los suyos propios, y un teorema
  superviviente que **aún no es admisible** porque un estrato bibliográfico sigue sin
  cerrar.
- **Tres agentes murieron sin informar** (límites de tasa, ciclos 4, 6 y 8). Asumí su
  papel cada vez. Un ciclo de tres agentes que corre con dos no es el diseño, y está
  anotado en cada informe afectado.
- **El registro de retractaciones vive en dos sitios** —este archivo y `ESTADO.md`— y el
  grafo sólo marca cuatro en línea. Es una inconsistencia de contabilidad, no de fondo,
  pero está.
