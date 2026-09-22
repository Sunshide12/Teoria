# T6 — La banda ciega

> Preregistrado el 22-09-2026. Sellado en `protocolo/protocol.json`
> (`e4f4c3d9…`). Resolutor ejecutable en `protocolo/resolve.py`.
> Verificación numérica en `verificacion/N133-la-banda-ciega.md`.

---

## Enunciado

Sea la medida de riesgo a horizonte `H` bajo escalamiento raíz-de-t con corrección de
media, estimada por sustitución directa sobre una ventana de `T` años:

```
ÊS(α, H) = −μ̂H + k_α · σ̂ · √H          k_α = φ(z_α)/(1−α)
```

**(i) Existe una banda de horizontes en la que el signo no está determinado por los
datos.** El contraste de `ÊS(α,H) = 0` no se rechaza al nivel `z` si y solo si

```
H⁻ < H < H⁺        con        H^∓ = [ k_α / (Ŝ ± z/√T) ]²,     Ŝ = μ̂/σ̂
```

Fuera de la banda el signo se determina trivialmente: positivo por debajo de `H⁻`
—domina la volatilidad—, negativo por encima de `H⁺` —domina la deriva—.

**(ii) La banda no se cierra: colapsa a un punto.** Cuando `T → ∞`,

```
H⁻, H⁺  →  H₀ = (k_α / Ŝ)²
```

y `H₀` es precisamente el horizonte donde `ÊS(α,H₀) = 0`. El horizonte al que el número
se anula es el horizonte al que ninguna cantidad de datos puede decirte su signo, porque
**un cero no tiene signo**. Para todo `H ≠ H₀` el `T` necesario es finito pero crece sin
cota conforme `H → H₀`, como `[z/(k_α/√H − Ŝ)]²`.

**(iii) `T` no es libre: está acotado por la estacionariedad.** Sea `T_est` la ventana más
larga que termina en el presente sin contener una ruptura estructural en la varianza.
Entonces el conjunto de horizontes cuyo signo es determinable **con una ventana
defendible** es el complementario de

```
( [k_α/(Ŝ + z/√T_est)]² ,  [k_α/(Ŝ − z/√T_est)]² )
```

y **ese conjunto no crece con el paso del tiempo**, porque `T_est` no es el calendario:
es la edad del régimen actual, y el proceso de rupturas la reinicia.

---

## Lo que lo convierte en teorema y no en despeje

(i) es álgebra de dos líneas. (ii) es su límite. Lo que hace que esto sea una afirmación
sobre el mundo y no sobre una fórmula es **(iii) conjugado con una medición**:

Sobre el mercado estadounidense —Fama–French, 1926-07 a 2026-07, 1.201 meses—

| | |
|---|---|
| ventana necesaria para determinar el signo a H=10 años | **T_det = 96 años** |
| ventana disponible sin cruzar una ruptura de volatilidad | **T_est = 85,0 años** |
| | **brecha: 11 años** |

**El conjunto de ventanas admisibles está vacío.** Y no por poco, ni por casualidad: la
ruptura está en agosto de 1941 (sup-Wald HAC **16,8 / 40,7 / 38,8** con los tres proxies
de volatilidad, al 1%), y σ̂ salta de 0,157 a 0,182 exactamente entre `T=94` y `T=96`.

> **Las únicas ventanas que determinan el signo son las que cruzan la ruptura. La
> determinación se compra con no estacionariedad.**

La banda con `T_est = 85` es **(6,60 , 18,96) años**, y contiene la ECL hipotecaria (7),
la ECL vitalicia (10) y el ALM de pensiones (15). No contiene los 10 días del FRTB ni el
año de Solvencia II. **No cae donde no molesta.**

---

## La forma cerrada, verificada

`H^∓` reproduce el `T_det` obtenido por búsqueda numérica bruta en **18 de 18 casos**
(`H ∈ {1,2,3,5,7,10,15,20,30}` × `α ∈ {0,95 · 0,99}`). No es un ajuste: es la misma
cantidad calculada por dos caminos.

---

## La objeción que podía matarlo

> *«Usa el estimador predictivo y el signo queda determinado.»* — Barberis (2000),
> Pitera & Schmidt (2018). Integrar `μ` fuera produce siempre un capital mayor.

Se comprobó, y **no lo mata**. El estimador predictivo sustituye `√H` por `√(H(1+H/T))`:

| versión | banda | ¿H=10 dentro? | H₀ |
|---|---|---|---|
| plug-in | (6,60 , 18,96) | sí | 10,444 |
| **predictivo** | **(7,16 , 24,40)** | **sí** | 11,907 |

**La banda se ensancha un 39%.** A `H=20` el predictivo es *más* indeterminado que el
plug-in. La razón es elemental y merece decirse despacio: la corrección predictiva añade
**varianza**, no **información sobre μ**. `SE(μ̂)` sigue siendo `σ/√T`, y el término
`−μH` es idéntico en las dos versiones.

> Se paga más capital por exactamente la misma ignorancia.

---

## Lo que NO es nuestro

El ciclo 9 desplegó tres buscadores con consultas preregistradas disjuntas —econométrico,
finanzas de inversión, regulatorio/actuarial—, 54 consultas y 27 textos íntegros
extraídos. Mataron tres afirmaciones del ciclo 8 y dejaron esto en pie sólo después de
recortarlo:

| ya publicado | quién |
|---|---|
| `T_req = ((z+z_β)/θ)²`, con «*decades*» para θ=0,33 | **Noguer i Alonso 2026**, ec. (21) — hallado por J1 y J2 **por separado** |
| `0 ≤ N* ≤ 1/ρ` (el techo transversal) | **Giller 2024**, ecs. (17)–(18) |
| que fijar μ=0 es estadísticamente, no prudencialmente, justificado | **Spadafora et al. 2014** |
| el diagnóstico de revisión al añadir un año, con σ_drift separada | **Richards, Currie & Ritchie 2012** (longevidad) |
| `ρ(Z) = −mμ + √m(ρ(Z₁)+μ)` con μ̂ enchufada, y la condición μ≪σ | **Pitera, Schmidt & Stettner 2023** |
| bandas del rendimiento a largo plazo que cruzan cero | **Müller & Watson 2016** · **Fama & French 2018** |
| la brecha μH y la regla corregida por media | **Danielsson & Zigrand 2006** |

Nada de eso es nuestro, y el ciclo 9 lo estableció tumbando lo que el ciclo 8 celebraba.

**Lo que queda, y sólo esto:**

1. La banda `H^∓` como **intervalo en el horizonte** —los dos polos del funcional, no
   uno—, con la forma cerrada verificada 18/18.
2. Su conjunción con `T_est` medido por un test de ruptura ⇒ **conjunto admisible vacío**,
   y el mecanismo: *la determinación se compra con no estacionariedad*.
3. Que el estimador predictivo **la ensancha**, con los números.
4. La singularidad `H₀` y la divergencia `[z/(k_α/√H − Ŝ)]²`.

**Y todavía no es admisible como novedad.** La regla del ciclo 8 (ninguna afirmación con
más del 20% de literatura sin ver) sigue bloqueando: el estrato econométrico está al 47,5%
sin ver, y el estrato regulatorio/actuarial tiene **una sola muestra**, luego no es
estimable en absoluto. Lo que falta es una tarea acotada, no un pozo sin fondo: **una
segunda muestra independiente del estrato regulatorio/actuarial**.

---

## Dónde no muerde

**Solvencia II, artículo 101(3):** *«With respect to existing business, it shall cover
**only unexpected losses**.»* Ahí el requisito se define como desviación respecto a la
media, `μ` se cancela idénticamente, y no hay problema de signo.

T6 aplica al ES plug-in usado como **nivel** —IFRS 9, C-3 Phase II RBC, ALM de
pensiones—, no al SCR. Esta restricción va escrita **antes** que la afirmación, no
después de que alguien la señale.

---

## Cómo se falsa

Seis predicciones fechadas, en `protocolo/protocol.json`. Las dos que importan:

- **P-4 (2046).** Recomputando cada año `T_est`, `Ŝ` y la banda, `H=10` permanece dentro
  en las veinte lecturas anuales. **Mecanismo de fallo identificado:** exige un Sharpe
  realizado sostenido por encima de ~1,0 sobre la ventana estacionaria completa.
- **P-6 (2082).** En 2082, con 56 años más de datos, sigue sin determinarse.

Y **el falsador propio**, escrito para que quien lo ataque empiece por ahí:

> El teorema es **más débil si no hay rupturas**. Sin ruptura, `T_est = 100` años, la
> banda es (10,42 , 37,77) y **H=10 queda fuera**: signo determinado, teorema refutado.

La hipótesis que más cómoda le resultaría a un modelizador —que el mercado es un régimen
homogéneo desde 1926— es exactamente la que mata este resultado. Es el caso que el test
rechaza al 1% con HAC bajo los tres proxies.

---

## Por qué hacen falta ~10⁴ años

Porque `H=10` cae a un 4% de `H₀ = 10,444`, y `T_req = [z/(k_α/√H − Ŝ)]²` diverge ahí.

| H | años de régimen estacionario necesarios |
|---|---|
| 5 | 28 |
| 7 | 115 |
| 9 | ~950 |
| **10** | **~1,2 × 10⁴** |
| 12 | ~1.250 |
| 20 | 73 |

**Aviso de precisión, y es importante.** A `H=10` el denominador `k_α/√H − Ŝ` vale
**0,018**: la cifra es sensible al **quinto decimal de Ŝ**. Con `Ŝ = 0,8247` salen 11.707
años; con Ŝ a precisión completa, 11.717. **Ese dígito no significa nada.** Lo que no
se mueve con ningún redondeo es el orden de magnitud: **dos órdenes por encima de la
historia disponible y tres por encima de la edad del régimen.** Citar «11.707» como si
fuera una medición sería exactamente el tipo de falsa precisión que este proyecto ha
retractado nueve veces.

Con esa salvedad, la tabla es el contenido entero del encargo original: *un teorema que
sólo se pueda comprobar a través de los años*. No por elección retórica — por la
aritmética de `[z/(k_α/√H − Ŝ)]²` cerca de su polo.
