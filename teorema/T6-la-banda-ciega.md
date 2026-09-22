# T6 — La banda ciega

> **Recortado por el ciclo 10, antes de publicarse.** El agente adversarial destruyó tres
> de las cuatro cifras del enunciado original y demostró que su parte (i) es una
> identidad. El buscador regulatorio demostró que el titular depende de un parámetro que
> el regulador fija en otro valor. Lo que queda está abajo, y es bastante menos.
>
> Preregistrado el 22-09-2026 · `protocolo/protocol.json` · verificación en
> `verificacion/N133-la-banda-ciega.md` · algoritmo en `motor/banda.py`.

---

## El enunciado, en la versión que aguantan los datos

Para el mercado total estadounidense, la Sharpe realizada sobre **cualquier** ventana de
10 a 95 años que termine hoy es estadísticamente indistinguible de `k_α/√10 = 0,8428`:

```
Ŝ (1941–2026) = 0,8247        t = 0,167        p = 0,87
```

Por tanto el signo del `ES₉₉` a diez años corregido por media **no está determinado por la
muestra**. El intervalo de horizontes indeterminados es

```
H^∓ = [ k_α / (Ŝ ± z/√T) ]²      →      (6,6 , 19,0) años
```

que contiene los horizontes de la ECL y del ALM de pensiones. El resultado es robusto a la
elección de ventana, al test de ruptura, al estimador predictivo y al `k_α` empírico.

**Y no se reproduce en 12 de los 16 mercados desarrollados con historia comparable.**

---

## Lo primero, porque cambia cómo se lee todo lo demás

**La banda en H es el intervalo de confianza de Ŝ con el eje reetiquetado.** No se parece:
lo es. Bajo la biyección `H ↦ k_α/√H`,

```
( k_α/√H⁺ , k_α/√H⁻ ) = ( Ŝ − z/√T , Ŝ + z/√T )
```

Comprobado numéricamente: `(0,612112 , 1,037288)` por los dos caminos, coincidencia a
`0,00e+00`. Es una identidad algebraica, no un hallazgo.

De ahí se sigue que **todo el contenido empírico de T6 cabe en un contraste**: `H₀: S =
k_α/√10`. No hacen falta barridos, ni `T_det`, ni brechas. Lo que el proyecto llamó «un
funcional con dos polos» durante tres ciclos es Merton (1980) leído en el eje del
horizonte.

**Lo que eso deja en pie, y es lo único que queda de original:** el IC de μ dice *cuánta*
ignorancia hay; la banda dice *a qué horizontes muerde*. Es valor expositivo, y el eje del
horizonte es donde vive la regulación. No es un teorema.

---

## Lo que el ciclo 10 destruyó

| cifra publicada | qué le pasó |
|---|---|
| `T_det = 96 años` | **Borrada.** Sale de un barrido de 96 contrastes correlacionados cuyo nivel efectivo es **15,2%** (iid) / **25,4%** (bootstrap), no 5%. El p familiar del z=2,098 observado es 0,116 / 0,214. Con el crítico corregido **T_det no existe en la muestra**. Y **borrar el año 1931 la hace desaparecer**. |
| «brecha de 11 años» | **Borrada.** No era una segunda medición: `T_det=96` **es** «H=10 sale de la banda a T=96». Era la primera repetida. |
| `11.707 años` | **Borrada.** IC95 por bootstrap estacionario: **(49 , 181.757) años**, con **44,7% de la masa en infinito o con el signo cambiado**. Si hace falta una cifra: «entre medio siglo e infinito, sin poder distinguir». |
| `H₀ = 10,444` | **Con IC:** `H₀ = 10,4 (IC95 6,3 – 20,4)`. Un punto de colapso con un IC de factor 3,3 no es un punto. |
| la conjunción con `T_est` | **Retirada como contenido original.** Con `SE(Ŝ)` por bootstrap por bloques (×1,13 a ×1,31, que la curtosis mensual de 10,6 exige), **H=10 está dentro de la banda para todo `T_est` de 10 a 100 años**. El test de ruptura, 1941 y `T_est` no eran portantes. |
| «ruptura en 1941-08» | **Sin fecha exacta.** Es 1939-10 / 1941-08 / 1946-10 / 1951-09 según el recorte (10/15/20/25%); desaparece con HAC `L≥50`, con Sansó κ₂ a `L≥60` y al filtrar un GARCH(1,1). Lo que aguanta: `σ(1926-41)/σ(1941-2026) = 2,14×`, p=0,0027 por bootstrap por bloques. **Régimen y clustering no están identificados en esta muestra.** |
| «σ̂ salta de 0,157 a 0,182 entre T=94 y T=96» | **Falso, y era mío.** Medido: T=90 → 0,1572 · T=93 → 0,1592 · T=94 → 0,1711 · T=95 → 0,1802 · T=96 → 0,1824. El ascenso va de T=93 a T=96. |
| «(ii) colapsa a un punto, no a cero» | **Vacuo.** Es propiedad de *todo* intervalo de confianza consistente: colapsa al estimador puntual. Y «un cero no tiene signo» es una tautología. |
| universalidad implícita | **Restringida.** En Jordà–Schularick–Taylor 1941–2020, **sólo 4 de 16 países** tienen H=10 dentro de la banda. `H₀` vale 10,4 en EE.UU. frente a 12,0–68,7 en el resto (Japón 27,1 · Europa 25,6 · RU 23,4 · Francia 49,1). |

---

## Y el golpe que vino del regulador

La banda `(6,60 , 18,96)` descansa **entera** sobre `Ŝ = 0,8247`, que es la media y la
desviación de rendimientos **simples totales**. Hay al menos cinco definiciones
defendibles, y dan bandas distintas:

| definición de μ | Ŝ | banda (T=85) | H=7 | H=10 | H=15 |
|---|---|---|---|---|---|
| simple, total *(la publicada)* | 0,8247 | (6,60 , 18,96) | dentro | dentro | dentro |
| **log, total** | 0,7441 | (7,76 , 25,14) | **fuera** | dentro | dentro |
| **simple, exceso sobre rf** | 0,5792 | (11,33 , 52,86) | fuera | **fuera** | dentro |
| **log, exceso sobre rf** | 0,5003 | (13,98 , 85,80) | fuera | fuera | dentro |
| **AAA/NAIC, prescrito por norma** | 0,4892 | (14,42 , 92,84) | fuera | fuera | dentro |

La última fila es la que importa. El **C-3 Phase II de la AAA/NAIC (2005)** es la única
calibración normativa publicada de la pareja deriva/volatilidad para renta variable
estadounidense. Sus factores de riqueza cruzan 1,0 —requisito exactamente cero— en 6,47 /
11,31 / 16,76 años según el cuantil, lo que implica `Ŝ = 0,478–0,504`, **estable a través
de cuantiles y consistente con su 8,75% anualizado declarado bajo lognormal**
(`ln(1,0875) − σ²/2 = 0,0725`, `/0,1511 = 0,480`).

**Con el Ŝ del regulador, la banda no contiene ni la ECL hipotecaria ni la vitalicia.** Y
bastarían `T = 30,7` años para determinar el signo a H=10, no 96.

> **Sólo H=15 —el ALM de pensiones— cae dentro de la banda bajo las cinco definiciones.**
> H=7 y H=10 dependen de cuál elijas, y **no hay dato que elija**.

---

## El resultado de segundo orden, que es lo más honesto que salió del ciclo

`SE(Ŝ) = √((1+Ŝ²/2)/T) = 0,126` (Lo 2002). Luego `IC95(Ŝ) = [0,579 , 1,071]`, y los bordes
de la banda heredan esa incertidumbre:

```
H⁻ ∈ [ 4,31 , 11,35 ]          H⁺ ∈ [ 9,64 , 53,02 ]
```

| H | ¿dentro? |
|---|---|
| 3 | fuera siempre |
| 5 · 7 · 10 · 15 · 20 · 30 | **indecidible** |

**No se puede determinar qué horizontes están en la región donde nada se determina.** La
banda cuya posición marca dónde falla la determinación tiene ella misma una posición
indeterminada, y por el mismo mecanismo.

Eso no es un fallo del teorema. Es el teorema aplicado a sí mismo, y es la forma final
honesta del resultado.

---

## El defecto epistémico, escrito por quien intentó matarlo

> Casi toda corrección de robustez **añade** incertidumbre, y por tanto **ensancha la banda
> y refuerza T6**. El teorema sólo puede morir por especificaciones que hagan la
> determinación *más fácil*.

El falsador que T6 declaraba —«sin ruptura, `T_est=100`, banda (10,42 , 37,77), H=10
fuera»— es real y alcanzable (HAC `L≥50` lo consigue), pero tiene un **margen del 4,0%**:
basta multiplicar `SE(Ŝ)` por **1,14** para borrarlo, y el bootstrap por bloques da
**×1,28 a ×1,32**. Con ese SE la banda sin ruptura es (9,04 , 51,09) y H=10 vuelve dentro.

**T6 es, en la práctica, infalsificable por la única ruta que él mismo ofrecía.** Queda
escrito aquí, porque si no cada réplica que «lo confirma» no aporta información.

---

## Lo que sobrevivió a los seis ataques

Tres cosas, y conviene decirlas porque el resto de este documento es demolición:

1. **El contraste central, y es robusto hacia abajo.** H=10 está dentro de la banda para
   **toda** ventana `T_est` de 10 a 95 años. No hay elección de ventana que lo saque.
2. **La normalidad no lo mueve.** `k_α` empírico del agregado por bootstrap estacionario:
   **2,535–3,041** frente a 2,6652, es decir 0,95×–1,14×. Para sacar H=10 haría falta
   bajar `k_α` un **27%**. Por la regla de 1,3× del proyecto, **ruido**. Lo–MacKinlay:
   `VR(10a) = 0,946 ± 0,399`, indistinguible de 1.
3. **El estimador predictivo lo ensancha un 40%**, de (6,60 , 18,96) a (7,16 , 24,40).
   Añade varianza, no información sobre μ.

Y una que no es del teorema sino del método: **Jorion 1996 quedó descartado como
precedente leyendo el escaneo original**. Su ec. (1) define `VAR = E(W) − W* = W₀(μ − R*)`
—VaR relativo a la media, μ entra y sale— y su Figura 4 publica un error estándar
**exactamente 0** en α=0, donde T6 publica `σ√(H/T) > 0`. La literatura fundacional del
VaR definió el problema de modo que esta banda no pudiera aparecer.

---

## Por qué esto no es admisible todavía

La regla del proyecto prohíbe declarar novedad con más del 20% de literatura sin ver. El
estrato regulatorio/actuarial sigue abierto, y la segunda muestra del ciclo 10 **no lo
cerró ni podía**: sus consultas se preregistraron *disjuntas*, que es exactamente la
violación de homogeneidad de captura que invalidó el estimador del ciclo 9. La tasa de
recaptura cruda fue 4/17 = 0,235.

Para cerrarlo haría falta una tercera muestra con las **mismas** consultas del primer
buscador, o sorteadas del mismo universo. No complementarias.

Y hay un rival de marco que hay que confrontar antes de escribir una línea más: la
**AAA/LCAS marzo-2005** ya reconoce que el dato histórico no determina la cola a horizonte
largo, y actúa —*«factors for the 20-year horizon at the 2.5% and 97.5% points are
deliberately excluded from the calibration»*—. La afirmación «ningún documento supervisor
lo reconoce» no sobrevive.
