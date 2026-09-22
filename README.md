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
| `motor/` | el algoritmo de correlación que cierra el bucle, y el algoritmo del resultado |
| `ciclos/` | un informe por ciclo, más los informes verbatim de cada agente en `cNN-raw/` |
| `memoria/` | **el estado comprimido**: recarga la investigación entera en ~1.5k tokens |
| `verificacion/` | los números, reproducibles |
| `auditoria/` | los dictámenes de novedad |
| `teorema/` | los intentos — **la mayoría retractados, y se dice cuál y por qué** |
| `protocolo/` | **el preregistro sellado y su resolutor ejecutable** |

```
python3 protocolo/resolve.py
```

Imprime `PASS / FAIL / VOID / MOOT / ESPERA` para cada predicción fechada. Hoy: P-2
pasa, el resto espera a 2031, 2036, 2046, 2060 y 2082.

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

## El resultado

**T6 — la banda ciega** (`teorema/T6-la-banda-ciega.md`), **recortado por el ciclo 10
antes de publicarse.** Lo que aguantan los datos:

> Para el mercado total estadounidense, la Sharpe realizada sobre cualquier ventana de 10
> a 95 años es indistinguible de `k_α/√10 = 0,8428` (**Ŝ = 0,8247, t = 0,167, p = 0,87**).
> El signo del `ES₉₉` a diez años corregido por media no está determinado por la muestra, y
> el intervalo de horizontes indeterminados es **(6,6 , 19,0) años**, que cubre la ECL y el
> ALM de pensiones.

```
H^∓ = [ k_α / (Ŝ ± z/√T) ]²
```

**Y lo primero que hay que saber es que esa banda es una identidad**: bajo H ↦ k_α/√H, es
el intervalo de confianza de Ŝ con el eje reetiquetado (coincidencia a `0,00e+00`). Es
Merton 1980 leído en el eje del horizonte. No se reproduce en **12 de 16 mercados**, y cuál
de los cinco Ŝ defendibles se use cambia qué horizontes entran — el regulador usa 0,489 y
con ese valor la banda es (14,4 , 92,8).

Lo que queda, y es el resultado más honesto del proyecto: `SE(Ŝ) = 0,126`, luego
`H⁻ ∈ [4,31 , 11,35]` y `H⁺ ∈ [9,64 , 53,02]`, de modo que para **H = 5, 7, 10, 15, 20 y
30 la pertenencia a la banda es indecidible**. No se puede determinar qué horizontes están
en la región donde nada se determina.

## Lo que no es

Este repositorio contiene **once resultados propios retractados**, seis de ellos escritos
con confianza ≥ 0,90 — el último, por el agente al que se le encargó matarlo. Están todos, con el mismo detalle con que se escribieron, en
`ESTADO.md` y `verificacion/M01-funciono-el-bucle.md`. El registro de lo que no funcionó
es la parte del método que no se puede reconstruir después.

T6 **todavía no es admisible como aportación**: la regla del proyecto prohíbe declarar
novedad mientras quede literatura sin ver por encima del 20%, y un estrato bibliográfico
sigue abierto.
