# N133 — La banda ciega

Verificación numérica sobre datos reales, no simulados. Serie: Fama–French
`F-F_Research_Data_Factors`, mensual, `Mkt-RF + RF` (rentabilidad total del mercado
estadounidense), 1926-07 a 2026-07, 1.201 meses. SHA-256 `347bdca…`, congelada en
`protocolo/serie-congelada.csv`.

Todo lo de abajo lo reproduce `python3 protocolo/resolve.py`.

---

## 1. El punto de partida: el signo ya está del revés

| ventana | μ̂ | σ̂ | ES₉₉ a 10 años con μ≡0 | con μ̂ |
|---|---|---|---|---|
| últimos 10 años | 15,25% | 15,91% | **+1,3408** | **−0,1842** |

Con la ventana de diez años que usaría cualquiera, **el ES₉₉ a diez años corregido por
media es negativo**. No es que la banda «incluya» capital negativo: el estimador puntual
ya lo es.

## 2. La curva de determinación del signo

Para cada ventana `T` que termina en 2026-07 se contrasta μ̂ contra la deriva que anula
el número, μ\* = k_α·σ̂/√H, con el error típico combinado por delta-method (μ̂ y σ̂
independientes).

| T | μ̂ | σ̂ | μ\* | ES₉₉(10a) | z | ¿signo determinado? |
|---|---|---|---|---|---|---|
| 5 | 0,1245 | 0,1619 | 0,1364 | +0,1193 | 0,16 | no |
| **10** | 0,1525 | 0,1591 | 0,1341 | **−0,1842** | 0,36 | no |
| **15** | 0,1452 | 0,1485 | 0,1251 | **−0,2006** | 0,52 | no |
| 20 | 0,1211 | 0,1576 | 0,1328 | +0,1171 | 0,33 | no |
| 30 | 0,1138 | 0,1585 | 0,1336 | +0,1976 | 0,67 | no |
| 50 | 0,1266 | 0,1543 | 0,1301 | +0,0349 | 0,16 | no |
| 90 | 0,1164 | 0,1572 | 0,1325 | +0,1610 | 0,96 | no |
| **96** | 0,1141 | **0,1824** | 0,1537 | +0,3962 | **2,10** | **sí** |
| 100 | 0,1155 | 0,1834 | 0,1546 | +0,3910 | 2,10 | sí |

**T_det = 96 años.** Y el punto estimado **cambia de signo** con la ventana: negativo a
10 y 15 años, positivo en las demás.

Mírese la columna σ̂: salta de 0,157 a 0,182 exactamente entre T=94 y T=96. Ese salto es
el régimen de volatilidad anterior a 1941. **Las únicas ventanas que determinan el signo
son las que cruzan la ruptura.** La determinación se compra con no estacionariedad.

## 3. El techo de estacionariedad

Búsqueda secuencial tipo Bai–Perron de cambios de nivel, con error típico HAC
(Newey–West, retardo 6), recorte 15%, valor crítico sup-Wald de Andrews al 1% = 12,35.

| proxy de volatilidad | rupturas | sup-Wald |
|---|---|---|
| log(r²) | 1941-08 | 16,8 |
| \|r\| | 1941-08 | 40,7 |
| r² | 1941-07 | 38,8 |

Los tres proxies coinciden en la misma fecha, y ninguno encuentra una segunda ruptura.
**T_est = 85,0 años.**

Sobre la **media**, en cambio, el sup-Wald HAC es **1,67** — muy por debajo de 12,35. La
asimetría importa y es el eje E del grafo hecho número: **la volatilidad tiene ruptura
documentada; la deriva no la tiene detectable.**

## 4. El teorema

```
T_det = 96 años    (hace falta para determinar el signo)
T_est = 85 años    (disponible sin cruzar una ruptura)
                   ──────────────────────────────────────
                   brecha 11 años ⇒ CONJUNTO ADMISIBLE VACÍO
```

## 5. La forma cerrada

El signo está indeterminado exactamente cuando `H⁻ < H < H⁺`, con

```
H^∓ = [ k_α / (Ŝ ± z/√T) ]²          Ŝ = μ̂/σ̂
```

Es el mismo funcional de N118/N119 leído al revés: sus **dos** polos, no uno.

**Verificación: la forma cerrada reproduce el T_det medido por búsqueda en 18 de 18
casos** (H ∈ {1,2,3,5,7,10,15,20,30} × α ∈ {0,95 · 0,99}).

Con `T_est = 85` y `Ŝ = 0,8247`: **banda = (6,60 , 18,96) años.**

| horizonte | ¿dentro? |
|---|---|
| FRTB, 10 días | no |
| Solvencia II, 1 año | no |
| **ECL hipotecaria, 7 años** | **sí** |
| **ECL vitalicia, 10 años** | **sí** |
| **ALM de pensiones, 15 años** | **sí** |
| proyección a 40 años | no |

## 6. La singularidad

Cuando T → ∞ la banda no se cierra a cero: **colapsa al punto** H₀ = (k_α/Ŝ)² = **10,444
años**, donde el requisito de capital es exactamente cero. Un cero no tiene signo.

| H | años de régimen estacionario necesarios |
|---|---|
| 5 | 28 |
| 7 | 115 |
| 9 | 947 |
| **10** | **11.707** |
| 12 | 1.255 |
| 20 | 73 |

Diez años cae a un 4% de H₀. De ahí los 11.707 años.

## 7. La objeción más fuerte, respondida con números

J1 la formuló así: *«C3 es demasiado vulnerable a la réplica "usa el estimador
predictivo"»* — Barberis (2000), Pitera–Schmidt (2018): integra μ fuera y el capital
siempre sale mayor, con signo siempre determinado.

Se comprobó. El estimador predictivo sustituye `√H` por `√(H(1+H/T))`:

| versión | banda | ¿H=10 dentro? | H₀ |
|---|---|---|---|
| plug-in | (6,60 , 18,96) | **sí** | 10,444 |
| **predictivo** | **(7,16 , 24,40)** | **sí** | 11,907 |

**El estimador predictivo desplaza la banda y la ensancha un 39%; no la elimina.** La
razón es elemental y vale la pena decirla: la corrección predictiva añade *varianza*, no
*información sobre μ*. `SE(μ̂)` sigue siendo `σ/√T`, y el término `−μH` es idéntico en
las dos versiones. Se paga más capital por la misma ignorancia.

A H=20 años el predictivo es **más** indeterminado que el plug-in, no menos.

## 8. La firma de revisión — y la retractación del 48×

El ciclo 8 predijo un ratio de **48×** entre la revisión anual de un número con μ̂ y uno
con μ≡0. Medido sobre 90 reestimaciones anuales reales: **3,04×**.

El 48× suponía σ constante. **σ̂ también se revisa** (6,42% del nivel), y eso hunde el
denominador. **Retractado.**

Lo que sí sobrevive, y es mejor porque es una igualdad y no una desigualdad:

```
Var(ΔES | μ̂) − Var(ΔES | μ≡0) = H² · 2σ²/T²
```

| ventana | reestimaciones | medido/teórico |
|---|---|---|
| 10 años | 90 | **1,054** |
| 20 años | 80 | **1,165** |
| 30 años | 70 | **1,110** |

Y la potencia del test a cinco años, medida sobre las 86 ventanas de 5 revisiones del
registro histórico: **P(ratio > 1,3) = 0,953**.

## 9. Corroboración externa que no nos buscaba

La Fed publica (17-abr-2025) que los cambios interanuales del *stress capital buffer*
promedian **65 pb** sobre un nivel medio de **3,88 pp**. Si la revisión es aproximadamente
centrada y gaussiana, σ ≈ 65/0,798 = 81,5 pb ⇒ **21,0% del nivel**, frente al **20,4%**
que predice la aritmética para un número que lleva μ̂ estimada con T=10 años, y frente al
0,42% de uno con μ≡0.

Es la mejor corroboración externa de nueve ciclos. Con dos advertencias que la propia
fuente obliga a poner: la Fed **promedia dos años precisamente para suprimir esa señal**
(65→54 pb), así que el test hay que correrlo sobre 2019–2025; y Curry (2021, §3.7.4)
documenta que las entidades suavizan deliberadamente, lo que hace la firma
observacionalmente confundible con la política de suavizado.

## 10. Dónde NO muerde

**Solvencia II, artículo 101(3):** *«With respect to existing business, it shall cover
only unexpected losses.»* El requisito se define como desviación respecto a la media, así
que **μ se cancela idénticamente** y no hay problema de signo. La banda aplica al ES
plug-in usado como **nivel** —IFRS 9, C-3 Phase II RBC, ALM— no al SCR.

Es una restricción de alcance, y conviene que esté escrita antes que la afirmación.
