# Formato de memoria comprimida

Objetivo: que una sesión futura (tuya o mía) recargue **toda** la investigación
leyendo ~1.5k tokens en vez de releer 10 informes.

Se leen dos archivos, en este orden:

1. **`GRAFO.md`** — los conceptos, con identificador estable. Es la "conexión
   neuronal": cada idea tiene un ID que no cambia nunca, así que cualquier ciclo
   futuro puede referirse a `N14` sin volver a explicar qué es N14.
2. **`MEM.ndx`** — una línea por ciclo. La trayectoria del pensamiento.

Nada más. Los informes de `ciclos/` son el respaldo auditable, no se leen para
continuar.

---

## GRAFO.md — nodos y aristas

```
N07 ≡ <enunciado del concepto en una línea>   [origen] w=<peso>
```

- `N07` — identificador estable. Nunca se reutiliza ni se renumera.
- `≡` — el enunciado, comprimido a una línea. Si necesita dos, es dos nodos.
- `[origen]` — de dónde salió: `C03·A2` = ciclo 3, agente 2. `C05·⊕` = síntesis
  del ciclo 5. `[lit]` = ya existía en la literatura (importante para no
  reclamar como nuestro algo que no lo es).
- `w` — peso en `[0,1]`: cuánta confianza acumulada carga el nodo. Sube cuando
  ciclos posteriores lo corroboran de forma independiente, baja cuando lo atacan.

Aristas, una por línea:

```
N03 → N11   implica
N05 ⊥ N09   tensión (no pueden ser ambos verdad como están enunciados)
N02 ⊕ N07 ⇒ N14   síntesis (dos nodos se funden en uno nuevo)
N08 ⊣ N04   refuta / acota
```

## MEM.ndx — una línea por ciclo

```
C03|k0.78|c[.88,.21,.17,.31,.93,.44]|D=F0.24|GRI|N:12,13,14|>N15|q:<pregunta>
```

| campo | significado |
|---|---|
| `C03` | número de ciclo |
| `k0.78` | κ, coherencia entre los 3 agentes (1 = idénticos, 0 = opuestos) |
| `c[...]` | centroide en los 6 ejes, en orden `A,E,F,P,H,O` |
| `D=F0.24` | eje de máxima divergencia (la grieta) y su σ |
| `GRI` | modo del controlador: `GRI`=atacar grieta, `ADV`=adversarial forzado, `CON`=convergente |
| `N:12,13,14` | nodos nuevos creados en el ciclo |
| `>N15` | nodo de síntesis del ciclo |
| `q:` | pregunta que este ciclo le pasa al siguiente |

### Los 6 ejes

| eje | 0 | 1 |
|---|---|---|
| **A** | la incertidumbre dominante es aleatoria irreducible | es epistémica (no saber el modelo/parámetros) |
| **E** | el proceso generador no es estacionario | es estacionario, el pasado informa |
| **F** | las afirmaciones a largo plazo son infalsificables | son falsables con datos de hoy |
| **P** | la solución debe ser libre de modelo | debe ser paramétrica bien especificada |
| **H** | el problema es invariante al horizonte | crece fuertemente con el horizonte |
| **O** | teórico puro | implementable ya |

---

## Cómo retomar la investigación en una sesión nueva

> Lee `memoria/GRAFO.md` y `memoria/MEM.ndx`. Son el estado completo de la
> investigación "Teoria": 10 ciclos × 3 agentes sobre los límites del Monte
> Carlo en riesgo a largo plazo. El resultado final está en `teorema/`.
> No leas `ciclos/` salvo que necesites auditar un paso concreto.

Eso basta.
