# Ciclo 6 — el algoritmo bajo no estacionariedad

*Experimento del orquestador, asumiendo los papeles de los dos agentes que cayeron por
límite de sesión (G1, el algoritmo; G3, la grieta del eje E y el sesgo bajista).*

**Diseño.** DGP con el nivel de volatilidad **a la deriva** —no estacionario, que es el
régimen que N60 y N62 dicen que no se puede descartar—, μ verdadero constante al 6% anual,
60 años de historia y evaluación a H=1 y H=10 años. 60 réplicas. La verdad es el ES₉₉
calculado con el μ verdadero y la volatilidad **realizada en el futuro** [t, t+H].

## Resultados

### H = 1 año (ES verdadero mediano: 0,362)

| procedimiento | capital medio | capital/verdad | déficit p95 | P(infraestimar) |
|---|---|---|---|---|
| A. práctica vigente (ventana 2a) | 0,374 | 1,032 | 0,215 | 48,3% |
| B. muestra completa | 0,370 | 1,019 | 0,093 | 46,7% |
| C. escalera + 2º mayor | 0,416 | 1,139 | 0,082 | 31,7% |
| D. algoritmo completo | 0,418 | 1,141 | **0,002** | **8,3%** |

### H = 10 años (ES verdadero mediano: 0,742)

| procedimiento | capital medio | capital/verdad | déficit p95 | P(infraestimar) |
|---|---|---|---|---|
| A. práctica vigente (ventana 2a) | 0,614 | **0,945** | 1,595 | 50,0% |
| B. muestra completa | 0,701 | **0,892** | 0,561 | **63,3%** |
| C. escalera + 2º mayor | 1,063 | 1,322 | 0,420 | 31,7% |
| D. algoritmo completo | 1,136 | 1,480 | **0,000** | **3,3%** |

---

## 1. El sesgo bajista, confirmado — y es del horizonte, no de la ventana

N88 lo había medido como propiedad de las ventanas. **No lo es.** A un año no hay sesgo:
los procedimientos convencionales dan 1,032 y 1,019. A diez años dan **0,945 y 0,892**, e
infraestiman el **50% y el 63,3%** de las veces.

**El sesgo bajista aparece con el horizonte.** El mecanismo es el de T3: a horizonte largo el
término de deriva (−μH) domina, y estimar μ con ruido lo hace sistemáticamente demasiado
grande en la mitad de las muestras — pero el error entra restando, así que el ES sale
demasiado pequeño. Y el efecto crece como H mientras la parte de cola crece como √H.

**Consecuencia:** acotar la dispersión de la ventana no corrige nada, porque el sesgo no
viene de la ventana. El ataque que el frente 4 planteaba como el más peligroso al entregable
**acierta en la conclusión y se equivoca en la causa**.

## 2. La cota de bolsillo NO sobrevive a la no estacionariedad

Este es el resultado que va contra nosotros y hay que ponerlo primero.

| | cobertura nominal | cobertura medida |
|---|---|---|
| `RMSE_rel ≥ 0,27·√(H/T)` a 1 año | 90% | **35,0%** |
| `RMSE_rel ≥ 0,27·√(H/T)` a 10 años | 90% | **43,3%** |

La cota que el ciclo 5 verificó con ratio 1,01–1,06 —y que era la pieza constructiva del
trabajo— **cubre menos de la mitad de lo que promete en cuanto el proceso deja de ser
estacionario.**

F1 la derivó y la verificó correctamente **bajo especificación correcta y estacionariedad**.
Fuera de ese dominio, la información de Fisher deja de ser el objeto adecuado y el sesgo de
especificación no está acotado por nada.

**Y aquí se cierra el círculo del trabajo entero:**

> La cota solo es válida si el proceso es estacionario. Y saber si el proceso es estacionario
> es precisamente lo que N60 demuestra que no se puede saber: la segmentación encuentra 3,97
> rupturas en una serie estacionaria sin ninguna, el mismo número que en una con cuatro
> reales.

Una cota cuyo dominio de validez no es verificable **no es una cota utilizable**. Y una cota
que no cubre es peor que no reportar nada, porque da falsa confianza con aspecto de rigor.

**N81 baja de w=0,80 a w=0,45**, con el dominio declarado explícitamente.

## 3. El algoritmo funciona, y cuesta

El algoritmo D —escalera fija para σ, μ declarado en el rango que cubre el IC95, capital en
el extremo conservador del rango— **elimina prácticamente el déficit**: 0,000 en el p95 a
diez años, con probabilidad de infraestimar del 3,3% frente al 50–63% de lo vigente.

**Y cuesta un 48% más de capital a diez años** (1,480 frente a 1,0). No es gratis, y la
afirmación del ciclo 5 de que el algoritmo era «neutral en capital» solo vale para la pieza
de la escalera, no para el conjunto.

El compromiso razonable es **C**, la escalera con la regla del segundo mayor sin declarar μ:
a diez años reduce el déficit p95 de 1,595 a 0,420 —**un factor 3,8**— por un 32% más de
capital. Eso sí supera holgadamente el umbral de 1,3× que la investigación se fijó, al
contrario de lo que la medición anterior sugería (1,27×), **porque aquella medía en régimen
estacionario y esta en el régimen que de verdad no se puede descartar.**

El rango declarado del algoritmo cubre el ES verdadero el **90,0%** de las veces a diez años
(nominal 95%) y el 78,3% a un año. A horizonte largo la cobertura es casi correcta; a
horizonte corto el rango de μ es demasiado estrecho respecto a la variabilidad de σ.

## Lo que queda del ciclo 6

| pieza | estado |
|---|---|
| T3, horizonte de determinación del signo | **nuevo, derivado y verificado** |
| El sesgo bajista es del horizonte, no de la ventana | **corregido respecto a N88** |
| La cota de bolsillo bajo no estacionariedad | **rota — cubre 35–43% de un 90% nominal** |
| La escalera + segundo mayor | **3,8× menos déficit por 32% más capital** |
| El algoritmo completo | funciona, cuesta 48% de capital a 10 años |
| La confrontación con Danielsson 2002 | la contribución es la media, ausente en 64 páginas |
