# Verificación independiente de N06 — la frontera de fase no identificable

N06 salió del agente estocástico en el ciclo 1 con w=0,78. Es el candidato a novedad
más fuerte del ciclo, así que lo verifiqué por mi cuenta antes de construir nada encima.

Código: `motor/fase.py`.

## Qué es la frontera

Para un GJR-GARCH(1,1), `σ²_t = ω + [(α + γ·1{z<0})z² + β]·σ²_{t−1}`. El coeficiente
aleatorio es `A_t = (α + γ·1{z<0})z² + β`, y

```
E[A]  = α + γ/2 + β                                 persistencia
M2    = E[A²] = (α² + αγ + γ²/2)·κ_z + 2β(α+γ/2) + β²
```

La curtosis poblacional del retorno es finita **si y solo si M2 < 1**:

```
E[σ²] = ω/(1−E[A])
E[σ⁴] = (ω² + 2ω·E[A]·E[σ²])/(1−M2)
κ_r   = κ_z · E[σ⁴]/E[σ²]²
```

`M2 = 1` no es la frontera de estacionariedad. A ambos lados el proceso es estacionario
y de aspecto idéntico. Lo que cambia es si el cuarto momento existe — y con él, el ritmo
al que el riesgo agrega con el horizonte.

Comprobación de consistencia: con los parámetros que el agente dio para acciones
calibradas (α=0,02 γ=0,10 β=0,92 ν=8) la fórmula da **M2 = 1,0085**, exactamente el
valor que reportó. La matemática del agente es correcta.

## Primer test: ¿lo ve la curtosis muestral?

Barrido con persistencia fija en 0,99, ν=8, ventanas de 20 años, 120 réplicas:

| s | M2 | fase | κ poblacional | κ muestral 20a (p5 / mediana / p95) |
|---|---|---|---|---|
| 0,050 | 0,9960 | finita | 22,7 | 5,12 / 6,64 / 16,21 |
| 0,055 | 0,9994 | finita | 149,1 | 5,29 / 7,59 / 26,77 |
| 0,058 | 1,0016 | **infinita** | ∞ | 5,30 / 8,04 / 19,97 |
| 0,060 | 1,0031 | **infinita** | ∞ | 5,41 / 7,57 / 15,86 |
| 0,065 | 1,0071 | **infinita** | ∞ | 5,51 / 8,35 / 27,56 |
| 0,070 | 1,0114 | **infinita** | ∞ | 5,67 / 8,70 / 26,88 |

La curtosis poblacional cruza de 22,7 a infinito. La muestral pasa de 6,64 a 8,70, con
rangos p5–p95 que se solapan en [5,67 · 16,21]. **Confirmado.**

## Segundo test: ¿lo ve la máxima verosimilitud?

La curtosis muestral es un estimador pobre, así que el test decisivo es el MLE. Se
ajusta GJR-GARCH-t completo por máxima verosimilitud sobre 20 años de datos diarios y se
clasifica según `M̂2 ≷ 1`. 35 réplicas por proceso.

| proceso real | M̂2 mediana | p5–p95 | sesgo | clasifica "infinito" |
|---|---|---|---|---|
| M2 = 0,9960 (finito) | 0,9902 | 0,9759 – 1,0022 | −0,0058 | 14% |
| M2 = 1,0114 (**infinito**) | 0,9935 | 0,9768 – 1,0149 | −0,0179 | **20%** |

**Precisión de clasificación: 52,9%.** El azar es 50%.

Separación entre medianas 0,0033, dispersión típica del estimador 0,0097: la señal es un
tercio del ruido.

## Lo que el agente no vio: el sesgo tiene dirección

Las dos medianas de `M̂2` caen **por debajo de 1**, incluido el caso en que la verdad es
1,0114. El estimador no solo falla: falla sistemáticamente hacia el mismo lado.

Con 20 años de datos diarios, la máxima verosimilitud informa "cuarto momento finito,
riesgo de cola acotado a largo plazo" el 80% de las veces en que la verdad es lo
contrario. El error no es simétrico ni inocente — apunta hacia la respuesta tranquilizadora.

Esto refuerza N06 y lo convierte en algo más fuerte que "no se puede estimar": **se
estima mal en una dirección predecible**. Se registra como N15.

## Estado

N06 sube de w=0,78 a **w=0,90** (verificado de forma independiente, dos estadísticos
distintos, incluido el eficiente).

Queda pendiente el estudio de escalamiento: cuántos años de datos estacionarios harían
falta para que la frontera fuese identificable. Si ese número supera el presupuesto de
estacionariedad del sistema (N10), N06 deja de ser una limitación práctica y pasa a ser
una imposibilidad estructural — que es exactamente lo que busca esta investigación.
