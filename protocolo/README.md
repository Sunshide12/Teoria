# El protocolo

Tres archivos. Se ejecuta sin argumentos y tarda unos segundos.

```
python3 resolve.py
```

| archivo | qué es |
|---|---|
| `protocol.json` | el preregistro, sellado con SHA-256 sobre su propio contenido |
| `resolve.py` | el resolutor: imprime PASS / FAIL / VOID / MOOT / ESPERA por predicción |
| `serie-congelada.csv` | la serie, congelada al sellar (`347bdca…`), para que no haga falta red |

El sello cubre el JSON canónico sin los dos campos del propio sello. `resolve.py` lo
recomprueba en cada ejecución e imprime **ROTO** si alguien editó el preregistro después
de fecharlo. Esa es toda la garantía que puede dar un archivo de texto, y es la que hay.

---

## Qué se está falsando

    ES(α, H) = −μH + k_α · σ · √H          k₀,₉₉ = 2,6652

El signo de ese número está **estadísticamente indeterminado** exactamente cuando

    H⁻ < H < H⁺        con       H^∓ = [ k_α / (Ŝ ± z/√T) ]²,   Ŝ = μ̂/σ̂

Fuera de la banda el signo se determina solo: positivo por debajo (la volatilidad manda),
negativo por encima (la deriva manda). La fórmula cerrada reproduce el `T` mínimo de
determinación **en 18 de 18 casos** contra la búsqueda numérica (`verificacion/N133`).

Lo que convierte eso en un teorema y no en un despeje es la segunda mitad: `T` no puede
crecer libremente, porque **está acotado por la ventana más larga que puedas defender como
estacionaria**. Sobre el mercado estadounidense esa ventana termina en la ruptura de
volatilidad de **agosto de 1941** (sup-Wald HAC 16,8 / 40,7 / 38,8 con los tres proxies, al
1%), lo que deja `T_est = 85 años` y la banda en **(6,60 , 18,96) años**.

| horizonte | dentro de la banda |
|---|---|
| FRTB, 10 días | no — signo determinado |
| Solvencia II, 1 año | no — signo determinado |
| **ECL hipotecaria, 7 años** | **sí — indeterminado** |
| **ECL vitalicia, 10 años** | **sí — indeterminado** |
| **ALM de pensiones, 15 años** | **sí — indeterminado** |
| proyección a 40 años | no — signo determinado |

La banda no cae donde no molesta. Cae encima de los horizontes con los que se provisionan
las partidas más grandes de un balance.

---

## Las seis predicciones

| id | qué | fecha |
|---|---|---|
| P-1 | la firma de revisión supera 1,3× | 2031 |
| P-2 | la ley exacta del exceso de revisión — **control del aparato** | siempre |
| P-3 | **2036 no resuelve nada**: registro sin veredicto, por diseño | 2036 |
| P-4 | **el teorema**: H=10 no sale de la banda en veinte lecturas anuales | 2046 |
| P-5 | la anchura de la banda no converge a cero | 2060 |
| P-6 | el veredicto largo: en 2082 sigue sin determinarse | 2082 |

**P-2 es el control.** Predice una igualdad, no una desigualdad:

    Var(ΔES | μ̂) − Var(ΔES | μ≡0) = H² · 2σ²/T²

Medido sobre 90, 80 y 70 reestimaciones anuales reales: **1,054 · 1,165 · 1,110** veces el
valor teórico. Si P-2 falla, ningún otro veredicto del protocolo significa nada, y
`resolve.py` lo dice en voz alta.

**P-3 es un compromiso contra nosotros mismos.** Con diez años de datos nuevos el contraste
tiene tamaño 21,4% y potencia 40,6%. El protocolo declara **por adelantado** que la lectura
de 2036 no es un veredicto. Leerla como confirmación es incumplirlo.

---

## Las cuatro salidas

- **MOOT** — la puerta bibliográfica encontró precedente anterior al 22-09-2026. Corre
  **antes** que el test empírico, y no es un detalle de orden: en el ciclo 8, seis consultas
  resolvieron en un día lo que el test empírico habría tardado 56 años.
- **VOID** — cayó una premisa. Si el sup-Wald sobre la **media** supera 12,35, μ no es
  constante y el protocolo entero se anula. Al sellar: **1,67**, muy por debajo.
- **PASS / FAIL** — lo normal.

---

## El falsador propio

El teorema es **más débil, no más fuerte, si no hay rupturas de volatilidad**. Sin ruptura,
`T_est = 100` años, la banda es (10,42 , 37,77) y **H=10 queda fuera**: signo determinado,
teorema refutado.

O sea: la hipótesis que más cómoda le resultaría a un modelizador —que el mercado es un
régimen homogéneo desde 1926— es exactamente la que mata este resultado. Es el caso que el
test rechaza al 1% con HAC bajo los tres proxies, y se deja escrito aquí para que quien lo
resuelva en 2046 sepa por dónde atacarlo primero.

---

## La singularidad

Cuando T → ∞ la banda **no se cierra a cero: colapsa a un punto**

    H₀ = (k_α / Ŝ)² = 10,444 años

En H₀ el requisito de capital es exactamente cero, y un cero no tiene signo. El horizonte al
que el número se anula es el horizonte al que ninguna cantidad de datos puede decirte su
signo. Por eso sacar H=10 de la banda exige **11.707 años** de régimen estacionario: 10 cae
a un 4% de H₀.

| H | años de régimen estacionario necesarios |
|---|---|
| 5 | 28 |
| 7 | 115 |
| 9 | 947 |
| **10** | **11.707** |
| 12 | 1.255 |
| 20 | 73 |

---

## Nota sobre lo que esto NO afirma

- **No** afirma que μ sea inestimable. Sobre la serie completa, `t = Ŝ√T = 6,3`.
- **No** afirma que la regla √t sea incorrecta. Eso está publicado: Danielsson & Zigrand (2006).
- **No** afirma que la corrección por media sea nuestra. No lo es.

Afirma una sola cosa: que **el signo** del número corregido, en una banda de horizontes que
contiene los de IFRS 9 y los de ALM de pensiones, no está determinado por ninguna ventana
defendible como estacionaria — y que esa banda **no se cierra con el tiempo**.
