# Verificación numérica — ciclo 1

Ejecutado con `motor/lab.py`. Los claims de los agentes no entran al grafo sin pasar por aquí.

## V1 — A2-C4: ¿hace falta T ≥ 11,4·H/p para falsar un ES mal especificado?

Poder del test de cobertura de Kupiec (p=1%, detectar tasa real = 2× la nominal):

| n independientes | poder |
|---|---|
| 100 | 0,141 |
| 300 | 0,396 |
| 600 | 0,540 |
| 900 | 0,716 |
| 1140 | 0,817 |
| 2000 | 0,958 |

n para poder 80% = **1070**. A2 predecía 11,4/p = 1140. **Confirmado**, error 6%.

A p=1% y H=10 años ⇒ **T_req ≈ 10.700 años estacionarios**.

## V2 — A3-C1: contenido empírico N = α·T_s/H

Con T_s = 30 años de estacionariedad defendible:

| afirmación | N eventos | suelo RSE |
|---|---|---|
| VaR95 diario | 378 | 5,1% |
| VaR99 diario | 75,6 | 11,5% |
| ES99 a 1 año | 0,30 | 183% |
| ES99 a 10 años | **0,03** | **577%** |

**Confirmado.** La frontera entre "ciencia" y "metafísica" cae entre el VaR diario y el ES anual.

## V3 — A3-C3: sensibilidad numérica vs sensibilidad de ventana

| perturbación | ES99 a 10 años | cambio |
|---|---|---|
| 40k → 4M trayectorias (mismo dato) | 0,654 → 0,649 | 0,77% |
| cambiar la ventana de estimación | 0,654 → 0,908 | 38,8% |

Razón de sensibilidades = **51×**. A3 predecía >200×.

**Parcialmente confirmado**: la dirección y el orden de magnitud aguantan —lo que se hace
con los datos importa ~50 veces más que cuántas trayectorias se corren—, pero el valor
concreto de 200× no se sostiene. La razón depende de cuán distintos sean los dos regímenes
comparados, así que el test es fuerte sobre el signo y débil sobre la magnitud.
Se registra como claim **acotado**, no confirmado.
