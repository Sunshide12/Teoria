# T3 — Horizonte de determinación del signo

*Resultado principal. Derivado por el orquestador al tirar del hilo que dejó el agente G1
antes de caer por límite de sesión: «la cota sobreestima el error una vez μ se declara».*

---

## Enunciado

Sea `ES_{α,H}` el Expected Shortfall al nivel α sobre un horizonte de H años, bajo el modelo
de referencia que usa toda la práctica regulatoria:

```
ES_{α,H} = −μH + k_α·σ·√H        con    k_α = φ(z_α)/(1−α)
```

(k₉₉ = 2,6652; k₉₇,₅ = 2,3378).

El número cruza cero en `μ* = k_α·σ/√H`. Y su **signo está indeterminado** al nivel de
confianza 1−γ cuando `μ*` cae dentro del intervalo de confianza de μ̂ estimado con T años de
datos:

```
| μ̂ − k_α·σ/√H |  <  z_{γ/2}·σ/√T
```

**Dividiendo por σ, la volatilidad desaparece por completo** y queda una desigualdad entre
tres cantidades adimensionales — el ratio de Sharpe, el horizonte y el span:

> ```
> | Ŝ − k_α/√H |  <  z_{γ/2}/√T
> ```

De donde el **horizonte de determinación**:

> ```
> H* = [ k_α / (Ŝ + z_{γ/2}/√T) ]²
> ```
>
> Para H < H\*, el signo del ES está determinado. Para H > H\*, no.

## Los dos límites, y lo que los separa

Con datos infinitos (T → ∞) el criterio no desaparece: queda

```
H*_∞ = (k_α / Ŝ)²
```

que es el horizonte al que el retorno esperado supera genuinamente al cuantil de cola. Eso
**no es ignorancia: es un hecho sobre el activo.**

La zona entre ambos es la indeterminación **epistémica** pura, y su tamaño relativo es
adimensional:

> ```
> H*(T) / H*_∞ = [ Ŝ / (Ŝ + z_{γ/2}/√T) ]²
> ```

> **Con Ŝ = 0,375 y diez años de datos, esa razón vale 0,142: la ignorancia sobre μ quita el
> 85,8% del rango de horizontes en el que el signo estaría determinado si μ se conociera.**

## Tabla

Horizonte de determinación H\*, en años, al 99% de nivel y 95% de confianza:

| Sharpe | T=10 a | T=25 a | T=50 a | T=100 a | T=∞ |
|---|---|---|---|---|---|
| 0,20 | 10,6 | 20,3 | 31,2 | 45,3 | 177,6 |
| **0,375** | **7,2** | 12,1 | 16,7 | 21,8 | 50,5 |
| 0,50 | 5,7 | 8,9 | 11,8 | 14,7 | 28,4 |
| 0,80 | 3,5 | 5,0 | 6,1 | 7,2 | 11,1 |

## Verificación

Muestreando μ̂ de su distribución y calculando el ES resultante, 200.000 réplicas:

| Ŝ | T | H | H\* | criterio | P(ES<0) medido |
|---|---|---|---|---|---|
| 0,375 | 10 | 1 | 7,18 | determinado | 0,000% |
| 0,375 | 10 | 5 | 7,18 | determinado | 0,515% |
| 0,375 | 10 | **7,2** | 7,18 | **umbral** | **2,514%** |
| 0,375 | 10 | 10 | 7,18 | indeterminado | 6,932% |
| 0,375 | 10 | 20 | 7,18 | indeterminado | **24,353%** |
| 0,375 | **50** | 10 | 16,70 | determinado | 0,050% |
| 0,800 | 10 | 10 | 3,52 | indeterminado | **44,635%** |

La probabilidad de que el número reportado salga negativo pasa de prácticamente cero a
sustancial **exactamente al cruzar H\***.

## Lo que dice sobre la práctica vigente

Con el Sharpe típico de renta variable (≈0,375) y diez años de datos, **el signo del ES₉₉
está determinado hasta 7,2 años de horizonte y no más allá.**

| requisito | horizonte | ¿dentro de H\*? |
|---|---|---|
| FRTB (ES 97,5% a 10 días) | 0,04 a | sí, con enorme margen |
| Solvencia II (1 año) | 1 a | sí |
| **IFRS-9 ECL vitalicia** | **10–30 a** | **NO** |
| Proyecciones de pensiones | 20–40 a | **NO** |

Y no se arregla acumulando datos: con **cien años** el horizonte de determinación llega a
21,8 años. Ninguna serie histórica disponible determina el signo a treinta.

## De dónde sale, y por qué no lo vio nadie

De la descomposición que el ciclo 5 dejó medida: `var(ÊS_H) = H²σ²/T + H·k²σ²/(2fT)`. El
primer término es el coste de estimar μ y crece como **H²**; el segundo es el de la cola y
crece como **H**. A 10 años el primero es el 99,86% del total.

Y la auditoría del ciclo 6 verificó, por extracción íntegra de los PDF, que **ni Danielsson
(2002) en sus 30 páginas ni Danielsson–James–Valenzuela–Zer (2016) en sus 34 mencionan la
media ni una sola vez**. Toda la literatura de riesgo de modelo fija μ≡0 por convención y
cuantifica solo la dispersión de cola. Con μ≡0 el ES nunca cruza cero y **el criterio no
puede aparecer**.

Es decir: el resultado estaba escondido detrás de una convención que nadie declara como tal.

## Relación con la convención √t

`√(H/Δ)·ES_{1d}` es **exactamente** `ES_H(μ=0)` (ratio medido 0,9941). La regla de la raíz
del tiempo no escala riesgo: **declara que la prima de riesgo es cero.** Y esa declaración
sesga el ES₉₉ un +3,9% a diez días —donde Basilea la validó y es correcta— y un **+145,9% a
diez años**, donde IFRS-9 y Solvencia II la heredan por inercia.

## Lo que hay que auditar antes de reclamarlo

1. **La pieza «el ES cruza cero» es trivial** y seguro que está en algún manual. Lo que hay
   que buscar es la **combinación** con el intervalo de confianza de μ̂ y la forma
   adimensional H\* = [k/(Ŝ+z/√T)]².
2. El criterio supone **μ constante**. Si μ revierte o es predecible (Pástor–Stambaugh 2012),
   la banda se estrecha y H\* sube. Esa es la grieta declarada.
3. Supone normalidad para el cuantil. Con colas gordas k_α es mayor, luego H\* **baja**: el
   resultado va en la dirección conservadora, pero hay que medirlo.

## Por qué solo se puede corroborar con los años

El criterio es una identidad dado el modelo: se verifica con álgebra. Lo que **no** se puede
verificar hoy es si el μ real cae donde el intervalo dice. Para saberlo hay que esperar a
que transcurran los años que el propio criterio dice que hacen falta — y el criterio dice
que son más de los que hay.

Esa circularidad no es un defecto del resultado: **es su contenido.**
