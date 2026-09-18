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

---

# CORRECCIÓN (ciclo 4) — mi enunciado era falso, y el mecanismo era otro

Este documento afirmaba que la frontera M2=1 «no se localiza a ningún T», basándose en la
meseta de RMSE medida. El ciclo 4 lo refuta y lo mejora.

## 1. Dentro del modelo, SÍ es identificable

El problema es **regular** en θ: la información de Fisher no es singular en la frontera
(autovalores 4,6·10⁻⁴ a 464), ∇M2 ≠ 0, y `T·KL(P⁺,P⁻) → 2c²/s² = 1,88` — medido
1,74 / 1,90 / 1,93 para el exponente a=1/2, y divergente como T^(1−2a) para a=0,4 y 0,3.

Luego **a_crítico = 1/2** exactamente, M̂2 es √T-consistente y asintóticamente normal con
`s = √(∇M2' I⁻¹ ∇M2) = 1,031`, y el error minimax es `Φ(−δ√T/s)`:

| T | error de clasificación |
|---|---|
| 10 años | 34% |
| 80 años | 12% |
| **158 años** | **5%** |

con |M2−1| = 0,0085. **Es identificable. Tarda siglo y medio.**

Mi enunciado —«no identificable a ningún T»— era falso. Queda registrado como N24a.

## 2. La meseta tenía un mecanismo real, y no era el que supuse

Las dos explicaciones candidatas quedan **refutadas numéricamente**:

- **No es ν̂.** Ajustando con ν fijado al valor verdadero se obtiene el mismo sesgo hasta
  la cuarta cifra: −0,00233 frente a −0,00235 a 10 años, +0,00024 frente a +0,00021 a 80.
  El polo en ν=4 infla el error estándar un 23% y nada más.
- **No es Hall–Yao 2003.** Su irregularidad exige E[z⁴]=∞, o sea ν≤4. Aquí ν≈7 y el QMLE es
  perfectamente regular. El flanco que la auditoría de novedad señaló queda cerrado.

El mecanismo real es lo que E1 llama **brecha de octava**:

> Una condición de **cuarto** momento se sondea con un estadístico de **octavo** momento.

`κ̂ = T⁻¹ Σ ẑ⁴` es una media muestral de sumandos con índice de cola ν/4. Cuando 4 < ν < 8
ese índice cae en (1,2): la media existe pero la varianza no, el límite es (ν/4)-estable
totalmente sesgado a la derecha, y el sesgo mediano decae como T^−(1−4/ν).

Medido: IQR ~ T^−0,36 con ν=7, T^−0,29 con ν=6, T^−0,42 con ν=8.

**Sesgo y error estándar decaen al mismo orden. Su razón es constante. De ahí la meseta.**

La medición era correcta; la interpretación no. Y el mecanismo correcto es más interesante
que el que propuse.

## 3. Lo que sí es indecidible, y está en otro sitio

La irregularidad no está en θ. Está en **f**, la ley de la innovación.

Lema exacto (no asintótico): con el mismo θ y el mismo σ₁, la afinidad de Hellinger de T
observaciones es **exactamente ρ(f₀,f₁)^T**, porque σ_t es la misma función del pasado bajo
las dos leyes.

Con un contaminante `f₁ = (1−ε)f₀ + ε·bump(±M)`, tomando ε = c/T y M = (Δκ·T/c)^¼ se
consigue que la afinidad no colapse mientras Δκ **no depende de T**. Resultado:

> Para toda brecha fija D>0 existen dos leyes con M2 = 1∓D/2 cuyo error minimax es
> **≥ 0,246, invariante de 10 a 32.000 años.** Exponente a = 0.

El encargo N30 pedía un argumento de dos puntos **en θ**. Ese argumento nunca podía dar el
resultado, porque en θ el modelo es regular. La cota existe, pero perturbando otro objeto.

## 4. El estadístico que lo hace tangible

Borrar los **tres mayores |ẑ|** de la muestra voltea la clasificación de fase en
**18,3% / 15,0% / 15,8%** de las muestras a 10 / 40 / 80 años.

**No decrece con T.** El día mayor carga el 11,5% de Σz⁴ a 10 años. A diez años, borrar
tres días mueve M̂2 más que la distancia entera a la frontera.

Es el único estadístico verdaderamente plano del ciclo, y es el que hay que reportar: no
«el RMSE se estanca» sino «tres días deciden la fase, y eso no mejora con más datos».

## 5. Lo que estaba publicado y no habíamos citado

**Francq & Zakoïan (2022, J. Econometrics 227(1):47–64), «Testing the existence of moments
for GARCH processes».** Es exactamente nuestro test, con la ley asintótica conjunta del
QMLE y los momentos empíricos de los residuos. **N24 como observación empírica estaba
pre-empted desde 2019.**

El flanco que nos queda: su TLC del cuarto momento empírico de residuos exige E[z⁸]<∞, o
sea ν>8 — y la calibración de renta variable que pone M2≈1 pone ν≈5–7. **Su test es
√T-válido justo donde no hace falta.** Eso es la brecha de octava otra vez, y es la entrada
a su resultado. **Pendiente: leer el paper completo antes de reclamarlo.**

Y el principio general está publicado desde antes: **Donoho & Liu (1991)** —riesgo minimax
≍ módulo de continuidad de Hellinger, y E[z⁴] tiene módulo infinito— y
**Bahadur & Savage (1956)** para la inexistencia de tests no triviales sobre clases ricas.
Nuestro resultado de a=0 es un Bahadur–Savage para la fase de cuarto momento de un GARCH.
