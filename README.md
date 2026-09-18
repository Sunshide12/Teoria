# Teoria — límites del Monte Carlo en riesgo a largo plazo

Investigación en bucle: **10 ciclos × 3 agentes**, cada ciclo correlacionado con
el anterior por un algoritmo explícito, buscando un resultado que no esté en la
literatura.

## De dónde sale

De un reel divulgativo sobre simulación de Monte Carlo aplicada a fondos de
inversión (`fuentes/00-analisis-montecarlo-origen.md`). El análisis de ese vídeo
subió toda la escalera de modelos —GBM → Merton → Heston → Bates →
GJR-GARCH-t+FHS → EVT— y se topó con algo que **ninguno** de esos modelos
arregla:

```
SE(μ) ≈ σ / √T
```

El error de estimación del drift depende del *span* de la serie, no de su
frecuencia. Muestrear cada minuto durante 20 años no estima μ mejor que muestrear
cada día durante 20 años. A horizonte de 1 año eso es irrelevante; a 10 años
domina todo lo demás.

Esa es la grieta por la que entra esta investigación.

## Estructura

| ruta | qué hay |
|---|---|
| `fuentes/` | el material de partida |
| `motor/` | el algoritmo de correlación que cierra el bucle entre ciclos |
| `ciclos/` | un informe por ciclo — el registro auditable |
| `memoria/` | **el estado comprimido**: recarga la investigación entera en ~1.5k tokens |
| `teorema/` | el resultado final |

## El bucle

Cada ciclo despliega 3 agentes con ángulos distintos sobre una misma pregunta.
Cada agente devuelve su análisis **y** una posición en 6 ejes. El motor
(`motor/correlacion.py`) convierte esas 3 posiciones en:

- un **centroide** — la conclusión del ciclo,
- una **coherencia κ** — cuánto coinciden,
- una **grieta** — el eje donde más discrepan,
- una **decisión de control** para el ciclo siguiente.

La última es lo que hace que esto sea un bucle y no una lista. La grieta del
ciclo *n* es la pregunta del ciclo *n+1*. Y si κ sube demasiado, el motor fuerza
un agente adversarial: diez ciclos de tres agentes que se dan la razón no son
diez ciclos de investigación, son un eco.

## Para retomarlo

Lee `memoria/GRAFO.md` y `memoria/MEM.ndx`. Nada más.
