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

**T6 — la banda ciega** (`teorema/T6-la-banda-ciega.md`). El signo del ES corregido por
media está estadísticamente indeterminado exactamente dentro de

```
H⁻ < H < H⁺        H^∓ = [ k_α / (Ŝ ± z/√T) ]²
```

Sobre el mercado estadounidense (Fama–French, 1926–2026) hacen falta **96 años** de
ventana para determinar el signo a diez años, y sólo hay **85** sin cruzar la ruptura de
volatilidad de 1941. **El conjunto de ventanas admisibles está vacío**, y la banda
—(6,60 , 18,96) años— contiene la ECL vitalicia y el ALM de pensiones.

Sacar H=10 de esa banda exige **11.707 años** de régimen estacionario, porque 10 cae a un
4% del punto `H₀ = (k_α/Ŝ)²` donde el requisito vale cero — y un cero no tiene signo.

## Lo que no es

Este repositorio contiene **diez resultados propios retractados**, seis de ellos escritos
con confianza ≥ 0,90. Están todos, con el mismo detalle con que se escribieron, en
`ESTADO.md` y `verificacion/M01-funciono-el-bucle.md`. El registro de lo que no funcionó
es la parte del método que no se puede reconstruir después.

T6 **todavía no es admisible como aportación**: la regla del proyecto prohíbe declarar
novedad mientras quede literatura sin ver por encima del 20%, y un estrato bibliográfico
sigue abierto.
