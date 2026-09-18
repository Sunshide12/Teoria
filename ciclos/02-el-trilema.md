# Ciclo 2 — El trilema, y por qué era un dilema

**Pregunta:** ¿Existe un funcional de riesgo Ψ a horizonte H que sea simultáneamente
**(a)** decisión-relevante, **(b)** invariante al drift y **(c)** refutable sobre una única
trayectoria?

**Agentes:** B1 libre de modelo (P→0) · B2 paramétrico con identificación parcial (P→1)
· B3 adversarial, buscando un teorema no-go.

| métrica | ciclo 1 | ciclo 2 |
|---|---|---|
| κ (coherencia) | 0,9085 | **0,6199** (Δ = −0,289) |
| κ_forma | 0,9803 | **−0,0793** |
| grieta | P, σ=0,114 | **P, σ=0,342** |

La polarización deliberada funcionó: la coherencia cayó casi treinta puntos y la
correlación de forma se volvió negativa — los agentes dejaron de coincidir incluso en
qué eje importa más. La grieta del eje P no se cerró: **se triplicó**.

Y sin embargo el ciclo se resolvió. Esa aparente contradicción es el hallazgo.

---

## La respuesta: sí existe, pero no es una medida de riesgo

B3 encontró la obstrucción y con ella la salida, en el mismo teorema.

> **T1.** Toda medida de riesgo aditiva en efectivo es Girsanov-*equivariante*: bajo un
> cambio de medida Q^θ la P&L se desplaza en ∫θσ ds, y por aditividad en efectivo
> ρ_Q = ρ_P − ∫θσ ds ≠ ρ_P. Luego (b) implica que **Ψ no puede denominarse en dinero.**

De ahí sale N19, que es el resultado más limpio del ciclo: **la frontera entre medidas
coherentes (Artzner) y medidas de desviación (Rockafellar) es exactamente la frontera de
Girsanov.** No es una taxonomía: es una consecuencia. El margen y el objetivo de
volatilidad son libres de drift por necesidad matemática. El Expected Shortfall y el
capital económico no pueden serlo jamás.

La escapatoria de B3 es debilitar la aditividad en efectivo a invariancia por traslación.
La clase que sobrevive es exactamente la de las **medidas de desviación**. Ahí Ψ existe,
cumple (b) y (c), y es decisión-relevante **solo como restricción** —vol-target, margen,
haircut— nunca como óptimo ni como capital.

En palabras de B3: *la construcción que buscan los otros dos agentes sí existe, pero lo
que sale por la puerta no es una medida de riesgo: es un sistema de márgenes.*

## Por qué la grieta se triplicó sin ser un desacuerdo

B1 se sitúa en P=0,15 y B2 en P=0,92. Parece desacuerdo máximo. No lo es: **estaban
respondiendo a preguntas distintas sin saberlo.**

- B1 tiene razón sobre la **anchura**: desviación, margen, lo pathwise. Ahí lo libre de
  modelo funciona y es lo único que funciona.
- B2 tiene razón sobre la **ubicación**: capital, ES, el número que se reporta. Ahí lo
  paramétrico es imprescindible y lo libre de modelo es vacuo.

B2 lo dijo en su autocrítica; B3 lo demostró con T1. El eje P no era un eje: eran dos
preguntas confundidas (N23). El motor de correlación no podía ver eso —solo ve números—
y por eso el informe importa más que el κ.

## Las tres convergencias

**`cuota-decisional-invariante`** — los tres agentes, conf. agregada 0,936. La parte del
problema de decisión accesible a un funcional invariante al drift es de unidades
porcentuales. Tres cifras que parecían contradecirse y no lo hacen:

| agente | cifra | qué mide |
|---|---|---|
| B3 | 0,12% | aporte del término de volatilidad a Var(f*), diario |
| B2 | 0,13% / 1,96% | Φ=2S²/m con vol constante / Φ_∞ con Heston |
| B1 | ≤ 25% | **techo universal** Ψ/(1+Ψ)², alcanzado solo si ⟨σ²⟩⟨σ⁻²⟩=2 |

La fórmula de B3 y la de B2 son la misma (2S²/m con S=0,4, m=252 da 0,127%). Y el 25% de
B1 no es un valor típico sino una cota superior que exigiría una dispersión de
volatilidad enorme. Los tres dicen lo mismo: **unidades porcentuales, con techo duro en
un cuarto.**

**`drift-recursivo`** — B1 y B2, conf. 0,927. Ver la nota del orquestador
`sintesis/S02-la-torre-del-drift.md`: ninguno lo puso de titular y es el hallazgo del
ciclo.

**`Lo que se refuta rápido es lo que no decide`** (N25) — los tres, por rutas distintas:

| | refutar 20% de error en varianza | refutar 20% de error en drift |
|---|---|---|
| B1 | ~4 días (a 5 min) | ~800 años |
| B2 | ~2,5 días | ~37 años |

Ratio de 10⁴ a 10⁵, y la cuota decisional (N18) va exactamente al revés. Esta
anticorrelación entre relevancia y refutabilidad es el candidato más fuerte a teorema
final de toda la investigación hasta ahora.

## Una refutación interna

B1 sostuvo (su C4) que la invariancia al drift **no** es un coste sino lo que *regala* la
validez tipo Ville exacta: reducir la nula compuesta vía invariante maximal.

B3 lo refutó (T3, N20): si el nulo está saturado por equivalencia, todo e-proceso cumple
ess-sup E_τ ≤ 1, el error tipo I es exactamente cero y la escala de evidencia 1/α queda
vacía. El e-proceso **deja de ser un test y pasa a ser un certificado cuasi-seguro**. La
invariancia regala refutabilidad, sí — pero vacía.

B2 había llegado a lo mismo por su cuenta en la autocrítica ("(b)⇒(c) es casi trivial, no
un logro"). Dos contra uno, y el que pierde lo hace contra un teorema citado
(Ruf–Larsson–Koolen–Ramdas, EJP 2023). B1-C4 se registra como refutado.

## Correcciones al grafo

B2 y B1 llegaron por rutas distintas —Clark–Ocone uno, Esscher el otro— a la misma
corrección: la escisión de Dambis–Dubins–Schwarz en «ley de ⟨M⟩ + saltos + drift» **no es
invariante gauge**. Bajo un cambio equivalente de medida cambian las dos piezas, porque
la prima de riesgo de varianza mueve la ley de ⟨M⟩ y el compensador de saltos es él mismo
un drift.

Consecuencia: **N13, la síntesis con la que cerró el ciclo 1, estaba mal planteada.**
Decía que un funcional invariante al drift sería estimable in-fill. Solo vale en la
versión débil de la invarianza y solo para H ≪ 1/κ. Se degrada de w=0,80 a w=0,62, y su
degradación es precisamente el resultado del ciclo 2.

N09 baja de 0,72 a 0,55.

## Verificación propia

Ver `verificacion/N06-frontera-de-fase.md`. El estudio de escalamiento terminó mientras
corría el ciclo, y el resultado es más fuerte de lo que el agente del ciclo 1 reportó:

| T (años) | sesgo | SE | RMSE | acierta la fase |
|---|---|---|---|---|
| 10 | −0,0181 | 0,0124 | 0,0219 | 23% |
| 20 | −0,0142 | 0,0149 | 0,0205 | 40% |
| 40 | −0,0156 | 0,0069 | 0,0170 | 16% |
| 80 | −0,0149 | **0,0038** | 0,0154 | 22% |

El error estándar cae a la cuarta parte entre 10 y 80 años. **El sesgo no se mueve.** El
RMSE se estanca en ~0,015, por encima de la distancia a la frontera (0,0114). No es un
problema de cantidad de datos: la frontera M2=1 no se localiza a ningún T (N24).

Sospecha a verificar: el sesgo se hereda de ν̂, el índice de cola de la innovación — es
decir N07 reapareciendo un nivel abajo.

## Salida hacia el ciclo 3

De todo el ciclo sobrevive **una sola ruta** capaz de batir el muro n_eff = T/H, que es
el resultado más sólido de la investigación: la **escapatoria ergódica** de B3 (N22). Si
H ≫ τ_vol, el objeto a estimar deja de ser la ley terminal y pasa a ser la ley invariante,
con n_eff = (T/τ)^(1−2d) en vez de T/H.

Todo depende de un único número. **Umbral: la puerta se cierra si d > ≈0,37.** Nuestra
estimación de d es ≈0,4 — justo al otro lado, y dentro del error de estimación.

Es exactamente el patrón de N24 otra vez: un parámetro que decide una fase, estimado con
un error mayor que su distancia a la frontera. El ciclo 3 va a determinar si se repite.
