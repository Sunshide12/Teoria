# Ciclo 10 — El ciclo que destruyó su propio teorema

**Encargo:** cerrar el estrato regulatorio (K1), **destruir T6** (K2), construir el
algoritmo (K3). Los tres reportaron.

`κ = 0,776` (+0,020) · centroide `[A .87 · E .21 · F .67 · P .87 · H .77 · O .88]` ·
modo GRIETA · **eje F**, y es la primera vez en seis ciclos que la grieta no es el eje E.

Esa grieta es el resultado. K1 pone `F = 0,92` —lo verificó todo, hasta leer un escaneo
de 1996 a ojo—; K2 pone `F = 0,35` —T6 es, en la práctica, infalsificable por la única
ruta que él mismo ofrece—. **No discrepan sobre los hechos. Discrepan sobre si el teorema
se puede matar.**

---

## Lo que K2 hizo, y es lo que nueve ciclos no consiguieron a tiempo

Seis ataques. No encontró ningún error aritmético en lo que le di. Encontró algo peor.

### La banda es una identidad

```
( k_α/√H⁺ , k_α/√H⁻ ) = ( Ŝ − z/√T , Ŝ + z/√T )
```

Coincidencia a `0,00e+00`. Lo comprobé a mano: `0,612112` y `1,037288` por los dos
caminos. **La banda en H no se parece al intervalo de confianza de Ŝ: es el intervalo de
confianza de Ŝ con el eje reetiquetado.**

Lo que el proyecto llamó durante tres ciclos «un funcional con dos polos» es Merton (1980)
con el eje cambiado. Y todo el contenido empírico de T6 cabe en un contraste:

> `H₀: S = k_α/√10 = 0,8428`. Medido `Ŝ = 0,8247`. **t = 0,167, p = 0,867.**

Eso es T6 entero. Sin barrido, sin `T_det`, sin brecha.

### Y las cifras se caen una por una

- **`T_det = 96`** sale de barrer 96 contrastes correlacionados. Nivel efectivo **15,2%**
  (iid) / **25,4%** (bootstrap), no 5%. Con el crítico corregido no existe en la muestra.
  **Borrar el año 1931 la hace desaparecer.**
- **La «brecha de 11 años»** no era una segunda medición: `T_det=96` *es* «H=10 sale de la
  banda a T=96».
- **Los 11.707 años** tienen IC95 bootstrap **(49 , 181.757)**, con **44,7% de la masa en
  infinito o con el signo cambiado**.
- **`H₀ = 10,444`** tiene IC95 **(6,26 , 20,42)**. Un punto de colapso con un IC de factor
  3,3 no es un punto.
- **La conjunción con `T_est` no era portante.** Con `SE(Ŝ)` por bootstrap por bloques
  —×1,28 a ×1,32, que la curtosis mensual de 10,6 exige— H=10 está dentro de la banda para
  **todo** `T_est` de 10 a 100 años. El test de ruptura, 1941 y `T_est` eran decorativos.
- **La ruptura no está identificada.** Desaparece con HAC `L≥50`, con Sansó κ₂ a `L≥60`, y
  al filtrar un GARCH(1,1). Excluyendo la década 1929–39 el sup-Wald cae de 16,8/40,7/38,8
  a **2,83/4,90/4,90**. *No hay dos regímenes: hay una década y noventa años.*
- **No es universal.** En Jordà–Schularick–Taylor 1941–2020, **4 de 16 países**. `H₀` vale
  10,4 en EE.UU. y entre 12,0 y 68,7 en el resto.
- Y **un desliz factual mío**: σ̂ no «salta de 0,157 a 0,182 entre T=94 y T=96». El ascenso
  va de T=93 a T=96.

### El defecto epistémico

> Casi toda corrección de robustez **añade** incertidumbre y por tanto **refuerza** T6. El
> teorema sólo puede morir por especificaciones que hagan la determinación *más fácil*.

Su falsador declarado tiene un margen del **4,0%** y se borra multiplicando `SE(Ŝ)` por
1,14. El bootstrap da ×1,28–1,32. **T6 es en la práctica infalsificable por la única ruta
que él mismo ofrecía.** Eso lo escribió el agente que intentaba matarlo, y va al teorema.

---

## Y el golpe vino del regulador, no de la estadística

K1 fue a buscar precedentes y encontró un número.

La banda `(6,60 , 18,96)` descansa entera sobre `Ŝ = 0,8247`. El **C-3 Phase II de la
AAA/NAIC (2005)** —única calibración normativa publicada de la pareja deriva/volatilidad
para renta variable estadounidense— implica `Ŝ ≈ 0,489`. Lo verifiqué por dos caminos
independientes: por el cruce del factor de riqueza (0,5038 / 0,4891 / 0,4788 según
cuantil) y por su 8,75% anualizado declarado bajo lognormal (0,480). **Coinciden.**

| definición de μ | Ŝ | banda | 7 | 10 | 15 |
|---|---|---|---|---|---|
| simple, total *(publicada)* | 0,8247 | (6,60 , 18,96) | dentro | dentro | dentro |
| log, total | 0,7441 | (7,76 , 25,14) | **fuera** | dentro | dentro |
| simple, exceso | 0,5792 | (11,33 , 52,86) | fuera | **fuera** | dentro |
| log, exceso | 0,5003 | (13,98 , 85,80) | fuera | fuera | dentro |
| **AAA, prescrito** | 0,4892 | (14,42 , 92,84) | fuera | fuera | dentro |

**Sólo H=15 cae dentro bajo las cinco. H=7 y H=10 dependen de cuál elijas, y no hay dato
que elija.**

Y K1 cerró los dos encargos pendientes:

- **Jorion 1996 no es precedente**, leído a ojo sobre el escaneo original. Su ec. (1)
  define el VaR *relativo a la media*, y su Figura 4 publica error estándar **exactamente
  0** en α=0, donde T6 publica `σ√(H/T) > 0`. La literatura fundacional del VaR definió el
  problema de modo que esta banda no pudiera aparecer.
- **Las cifras 2,93/1,04 son exactas pero estaban mal atribuidas**: son de Dahlquist &
  Ibert (JFE 2026), no de Couts–Gonçalves; el ciclo 9 fusionó dos artículos. Y el panel
  tiene mediana de 5,5 años por gestora, no 26, así que la inferencia de anclaje es mucho
  más débil de lo que parecía.
- **Y el rival de marco**: la AAA/LCAS 2005 escribe *«factors for the 20-year horizon at
  the 2.5% and 97.5% points are deliberately excluded from the calibration»*. Un regulador
  que **se niega a fijar** las celdas que el dato no soporta. «Ningún documento supervisor
  lo reconoce» no sobrevive.

---

## El resultado de segundo orden

Si la banda es el IC de Ŝ, entonces la banda hereda la incertidumbre de Ŝ. Con
`SE(Ŝ) = 0,126` (Lo 2002):

```
H⁻ ∈ [4,31 , 11,35]        H⁺ ∈ [9,64 , 53,02]
```

Para **H = 5, 7, 10, 15, 20 y 30** la pertenencia a la banda es **indecidible**.

> No se puede determinar qué horizontes están en la región donde nada se determina.

No es un fallo. Es el teorema aplicado a sí mismo, y es la forma final honesta del
resultado.

---

## Lo que sobrevivió

1. **El contraste central es robusto hacia abajo**: H=10 dentro de la banda para toda
   ventana de 10 a 95 años.
2. **La normalidad no lo mueve**: `k_α` empírico 2,535–3,041 frente a 2,6652 cuando haría
   falta un −27%. Ruido por la regla de 1,3×.
3. **El estimador predictivo lo ensancha un 40%.**
4. **El algoritmo** (`motor/banda.py`, 1.097 líneas, 21/21 pruebas, verificadas
   ejecutándolas). Su virtud no es calcular: es **negarse a calcular**. Si el paso 0
   detecta ruptura en la media, devuelve `None` en los pasos 1–6. Si H cae dentro de la
   banda, `ES_punto = None`. No se puede leer un número que no existe.

Y K3 cruzó dos álgebras independientes —«H dentro de la banda» (horizonte) y «el intervalo
de ES cruza cero» (capital)— que coinciden en 13 horizontes. Eso sí es verificación.

---

## El estrato sigue abierto, y ahora sabemos que no se puede cerrar así

K1: n₁=17, n₂=20, m=4 ⇒ 55,8% sin ver. **Y el estimador vuelve a ser inválido, ahora por
diseño**: sus consultas se preregistraron *disjuntas*, que es exactamente la violación de
homogeneidad que invalidó el del ciclo 9. La recaptura cruda 4/17 = 0,235 confirma que la
estratificación era correcta, pero no cierra nada.

**Para cerrarlo hace falta una tercera muestra con las mismas consultas, o sorteadas del
mismo universo. No complementarias.** El propio agente lo escribió contra su propio
resultado.

---

## Balance del ciclo, y del bucle

El ciclo 10 no produjo un teorema. **Destruyó el suyo y dejó escrito por qué**, que es lo
que los nueve anteriores hicieron tarde y este hizo a tiempo, antes de publicar.

Lo que queda es esto, y es poco pero es verdad:

> Para el mercado total estadounidense, la Sharpe realizada sobre cualquier ventana de 10
> a 95 años es indistinguible de `k_α/√10` (t=0,167, p=0,87), de modo que el signo del
> `ES₉₉` a diez años corregido por media no está determinado por la muestra. El intervalo
> de horizontes indeterminados —imagen exacta del IC de Ŝ— es (6,6 , 19,0) años y cubre la
> ECL y el ALM de pensiones. Es Merton 1980 leído en el eje del horizonte, con una
> coincidencia numérica estadounidense encima. No se reproduce en 12 de 16 mercados, y
> cuál de los cinco Ŝ defendibles se use cambia qué horizontes entran.

El encargo original pedía «un algoritmo no contemplado hasta ahora» y «un teorema sólo
comprobable a través de los años». El bucle entregó **un algoritmo que se niega a dar
números cuando no los hay**, un protocolo sellado con seis predicciones fechadas hasta
2082, y **once resultados propios retractados** — el último, por el agente al que le
encargué matarlo.
