# Ciclo 7 — El teorema que no era

**Pregunta:** auditar T3 antes de construir encima, localizar el punto de cruce
especificación/estimación, y romper T3 por donde se rompa.

**Agentes:** H1 auditoría · H2 el punto de cruce · H3 adversarial.

| métrica | valor |
|---|---|
| κ | **0,7189** (idéntico al ciclo 5) |
| κ_forma | **−0,2604** |
| grieta | **eje E**, σ=0,286 — tercer ciclo consecutivo |
| única convergencia | «hereda el supuesto iid», 0,88 |

---

## 1. T3 cae, por dos motivos y el segundo es peor

**El cruce por cero está publicado literal.** Dowd, Blake & Cairns, *«Long-Term Value at
Risk»*, Pensions Institute DP468 / *J. Risk Finance* 5(2):52–57 (2004), §2, verificado por
extracción íntegra:

> *«As the time horizon increases, the VaR rises initially but then peaks and turns down;
> after that it keeps falling, becomes negative at some point, and thereafter remains
> negative.»*

Con tabla (VaR₉₉ = 0,244 a 5 años → −0,552 a 20), con el **pico**, con la **sensibilidad
creciente al μ supuesto**, y con la recomendación de **declarar μ** que presentábamos como
nuestra. Aportación nuestra en esa pieza: **cero**.

**Y el error de método.** Enchufé el intervalo de confianza de μ̂ en la fórmula del ES. **Eso
no es propagar incertidumbre.** El tratamiento coherente integra la incertidumbre en la
varianza predictiva, `σ²H(1+H/T)`, que es el componente de *estimation risk* de
Pástor–Stambaugh 2012, y entonces

```
ES_pred = −μ̂H + k_α·σ·√(H(1+H/T))  >  0   para todo H,   cuando  Ŝ√T < k_α
```

Verificado: el Sharpe ajustado por incertidumbre crece 0,358 → 0,839 → 1,131 (H=1/10/100) y
**satura en Ŝ√T = 1,186. Nunca alcanza k₉₉ = 2,665.**

> **T3 declaraba indeterminado lo que el tratamiento coherente determina.** Y la dirección
> del efecto que anuncié era la contraria a la correcta: propagar bien la incertidumbre
> **aumenta** el ES.

Y el mapa regulatorio no sobrevivía ni a nuestro propio grafo: con el d≈0,40 que el ciclo 3
midió, H\* cae de 7,18 a **1,90 años**.

**N96: 0,90 → 0,50.**

## 2. Lo que sobrevive es más simple — T4

```
sup_H [ Ŝ·√H / √(1+H/T) ] = Ŝ·√T
```

luego el ES₉₉ es **estrictamente positivo a todo horizonte mientras T < (k_α/Ŝ)² = 50,5
años**, con dualidad exacta: *el horizonte al que el ES cruzaría cero si μ se conociera es
la longitud de muestra mínima para que el cruce pueda existir.*

> **El horizonte no compra signo. Solo la muestra lo compra.**

Y la reparación mueve más que lo refutado: **1,746× a 10 años, 12,2× a 40.**

## 3. La caja de convenios de mi propio teorema

H3 encontró el análogo de N74 aplicado a T3, **y es mayor**: H\* ∈ [4,54a; 38,63a], rango
**8,52×**, sin que ningún dato lo fije. Ejes: ventana 2,33× · **numerario 1,52×** · deriva de
μ 1,22× · cola verdadera 1,10× · k₉₉ medido 1,06×.

**Yo reporté la esquina baja.**

Y el eje del numerario es elegante: **el cero no es un dato, lo pone el instrumento de
referencia.** Si el capital devenga r —que es la definición de Artzner et al. 1999— entonces
Ŝ es el Sharpe *en exceso* y H\* pasa a **10,90 años**: el borde inferior de IFRS-9 entra en
la región determinada.

**Y encontró un error en mi propio encargo:** escribí que las colas gordas bajan H\*. Es al
revés — la fórmula es creciente en k_α. Y el efecto es ruido de todos modos: el agregado a
diez años vuelve a ser casi gaussiano (k₉₉ medido 2,744 con memoria larga y t₇, 2,873 con
crashes, frente a 2,665).

## 4. El signo no mueve capital

El frente que mató dos líneas anteriores se resuelve también contra T3:

| tratamiento | multiplicador a 10 años |
|---|---|
| **truncar en cero** | **1,021×** — ruido |
| ES con μ:=0 (la desviación) | 1,802× |
| ES al p90 del error de μ | 1,866× |
| **ES predictivo, integrando μ** | **1,746×** (5,360× a 30a) |

**La dramatización del signo no estaba donde está el dinero.** Aunque truncar sigue sin ser
válido, y por una razón que no es de nivel: rompe la equivarianza de caja, y en la región
truncada —7,0% de probabilidad a 10 años— **el alivio marginal de capital por cubrirse es
exactamente cero**. No quita el fallo: lo vuelve invisible.

Y dónde está el P&L de verdad: **el vaivén anual de la provisión de IFRS-9 por reestimar μ
con un año más de datos es el 21,4% del nivel del ES a 10 años y el 89,6% a 30.**

## 5. El punto de cruce, en forma cerrada

H2 cumplió el encargo que la auditoría del ciclo 6 había señalado como el de mayor valor:

```
ε*(H) = √(H/T) / (k_α − Ŝ√H) · √(1 + h₀/H)
```

**La especificación domina si y solo si el modelo yerra más del ε\* del número que reporta.**
Verificado exacto —predicho igual a medido a tres decimales— en 7 generadores × 7 horizontes.
Con T=10 años: **2,4% a 10 días, 37,5% a 10 años.**

Y el cruce medido por tipo: t₅ **19 días** · saltos **38d** · memoria larga **76d** · saltos
asimétricos **100d** · vol estocástica **0,83a** · vol apalancada **3,15a** · **nivel de vol a
la deriva: NUNCA**. Mediana 0,30 años. **A diez años la especificación domina en 0 de 7.**

**Cruce de capital en 34 días.** A diez años, arreglar por completo la especificación mueve
**1,142× —ruido por nuestra propia regla— frente al 2,111× del error de estimación.** La
relación de palancas pasa de 1,05 a favor de especificar a **7,9 a favor de estimar**.

> En el libro de negociación el presupuesto de modelización va a especificar. En ECL vitalicia
> y pensiones, **todo gasto en especificar la cola es sofisticación asignada a un efecto del
> 14%**.

**Y cerró el flanco declarado del ciclo 6**: extrajo las 58 páginas de Kerkhof et al. y su
aplicación es literal «T = 1/252 (one day)», con la única aplicación plurianual
**delta-cubierta** —neutral a la deriva por construcción—. **El canal de la deriva está
ausente de su diseño: su ordenación no es un hallazgo, es forzada.**

## 6. La escalera de tres horizontes

Un solo funcional con tres umbrales:

| umbral | qué ocurre | T=10a |
|---|---|---|
| **H_×** | se invierte el orden especificación/estimación | **0,30 años** |
| **H\*** | se disuelve el signo | **6,4 años** |
| **H\*_∞** | el número se anula | **37,1 años** |

El polo de ε\* es exactamente H\*_∞. Misma ley, tres umbrales.

## 7. Y la síntesis — T5

De cruzar N19 (ciclo 2, tumbado por publicado), N91 (ciclo 6, la ausencia verificada) y N113
(ciclo 7, μ≡0 es la desviación de Rockafellar) sale la tesis final:

> Una medida usada como **capital** debe ser aditiva en efectivo (Artzner 1999). Una de
> **desviación** es invariante a traslación (RUZ 2006). Difieren **exactamente en E[X]**. La
> regla √t reporta `k_α·σ·√H`, que no contiene μ ⇒ **es una desviación, usada como capital**.
>
> **La brecha es exactamente μH** — el parámetro ausente de las 64 páginas.
>
> Adimensional: `Ŝ√H/k_α` = **2,8% a 10 días · 44,5% a 10 años · 77,1% a 30**.
> En capital: **1,029× · 1,802× · 4,360×**.

Con la ironía que conviene dejar escrita: **el teorema que el ciclo 2 presentó como su
resultado más limpio, y que la primera auditoría tumbó por estar publicado, es exactamente el
instrumento que explica el hallazgo del ciclo 6.** No era nuestro resultado. Es nuestra
herramienta.

## Salida hacia el ciclo 8

La grieta lleva tres ciclos en el eje E y hay que cerrarla. Todo el aparato cuantitativo se
deriva en un mundo iid-gaussiano que el propio grafo declara no disponible.

1. **Auditar T5** antes de escribirlo, como se auditó T3 — y T3 se cayó.
2. **Cerrar la grieta del eje E**: qué sobrevive sin estacionariedad, y cuantificarlo.
3. **El protocolo de falsación**: especificar exactamente qué observación futura refutaría
   cada afirmación, con fecha y criterio, para que alguien pueda resolverlo en 2036 sin
   hablar con nosotros.
