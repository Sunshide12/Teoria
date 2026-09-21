# T3 — RETRACTADO

*Lo que el ciclo 6 presentó como resultado principal no sobrevivió a la auditoría del ciclo 7.
Se conserva íntegro, con el mismo detalle con que se escribió, porque el registro de lo que
no funcionó es la parte del método que no se puede reconstruir después.*

El enunciado original está en `T3-horizonte-de-determinacion.md`. Aquí va por qué cae.

---

## 1. El cruce por cero está publicado, literal

**Dowd, Blake & Cairns, «Long-Term Value at Risk»**, Pensions Institute DP468 (rev. sep-2003)
/ *Journal of Risk Finance* 5(2):52–57 (2004), §2, verificado por extracción íntegra del PDF:

> *«As the time horizon increases, the VaR rises initially but then peaks and turns down;
> after that it keeps falling, becomes negative at some point, and thereafter remains
> negative.»*

Y su nota 7:

> *«A negative VaR simply means that the likely worst outcome … is a profit.»*

Con la tabla: VaR₉₉ = 0,244 (5 años) → 0,098 (10 años) → **−0,552 (20 años)**.

No solo el cruce: también el **pico**, la **sensibilidad creciente al μ supuesto** (*«VaR
estimates become more sensitive to assumed mean returns, the longer the time horizon»*) y
hasta la recomendación que N98 presentaba como nuestra (*«the best approach is simply to take
a view about the values of the mean long-term parameters»*).

**Aportación nuestra en esa pieza: cero.**

Y las demás piezas también estaban: `H*_∞=(k_α/Ŝ)²` en sustancia es Kritzman (FAJ 1994);
«√t ≡ μ=0» es Bodie (1995) en lenguaje de opciones; `SE(μ̂)=σ/√T` es Merton (1980).

## 2. El error metodológico, que es peor que el precedente

**Enchufé el intervalo de confianza de μ̂ en la fórmula del ES. Eso no es propagar
incertidumbre.**

El tratamiento coherente —y publicado, es el componente de *estimation risk* de
Pástor–Stambaugh 2012— integra la incertidumbre en la **varianza predictiva**:

```
ES_pred = −μ̂H + k_α·σ·√( H·(1 + H/T) )
```

y ese objeto es **estrictamente positivo a todo horizonte** cuando `Ŝ√T < k_α`, porque

```
sup_H [ Ŝ·√H / √(1+H/T) ] = Ŝ·√T
```

Verificado numéricamente: con Ŝ=0,375 y T=10 años, el Sharpe ajustado por incertidumbre
crece 0,358 → 0,839 → 1,131 (H = 1 / 10 / 100 años) y **satura en 1,186. Nunca alcanza
k₉₉ = 2,665.**

> **T3 declaraba indeterminado lo que el tratamiento coherente determina.** Y determina que
> es pérdida.

Propagar bien la incertidumbre **aumenta** el ES —ensancha la predictiva— en lugar de dejarlo
sin signo. La dirección del efecto que anuncié era la contraria a la correcta.

## 3. Y el mapa regulatorio no sobrevive a nuestro propio grafo

H\* = 7,18 años está calculado bajo iid, que es exactamente el mundo que N45, N60 y N99
declaran no disponible. Sustituyendo T por el n_eff de N43:

| d | T_eff | H\* |
|---|---|---|
| 0,00 | 10,0 a | 7,18 a |
| 0,20 | 3,98 a | 3,86 a |
| 0,26 | 3,02 a | 3,15 a |
| **0,40** | **1,58 a** | **1,90 a** |

Con el d≈0,40 que el propio ciclo 3 midió, H\* cae a **1,90 años**: ni Solvencia II a un año
queda holgadamente dentro, y la tabla de «IFRS-9 fuera, Basilea dentro» se derrumba con el
número.

## 4. Lo que hay que retirar

- La palabra **«indeterminado»**.
- La centralidad de **H\***.
- La tabla regulatoria.
- El título de «resultado principal».

**N96 baja de 0,90 a 0,55. N97 baja de 0,88 a 0,60.**

## 5. Nota de método

Es la quinta vez en este trabajo que un resultado propio se cae, y la más importante porque
era el principal. Pero conviene fijarse en cómo: **el agente que lo tumbó se lanzó
precisamente para auditarlo antes de construir encima.** El bucle hizo lo que estaba
diseñado para hacer. Los cuatro ciclos que se perdieron persiguiendo la frontera de cuarto
momento se perdieron porque esa auditoría llegó tarde.
