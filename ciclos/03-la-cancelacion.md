# Ciclo 3 — La cancelación

**Pregunta:** ¿Es real la escapatoria ergódica (N22)? Era la única ruta conocida capaz de
batir el muro `n_eff = T/H`, el resultado más sólido de la investigación.

**Agentes:** D1 memoria larga y ergodicidad · D2 estimabilidad de d · D3 adversarial.

| métrica | C1 | C2 | C3 |
|---|---|---|---|
| κ | 0,9085 | 0,6199 | **0,6887** |
| κ_forma | 0,9803 | −0,0793 | −0,0217 |
| grieta | P (0,114) | P (0,342) | **E (0,262)** |

---

## La respuesta: no. Y por una razón más limpia de lo que esperaba

D1 derivó la cancelación exacta. Sea v_t estacionaria con ρ(k) ≈ c·k^(2d−1), y
Var(Σ_{t≤n} v_t) = σ²S(n):

```
aleatorio:  CV(IV_H)     = σ√S(n_H)/(θ·n_H)  ∝  H^(d−½)
epistémico: sd(θ̂_T)/θ    = σ√S(n_T)/(θ·n_T)  ∝  T^(d−½)
```

Es **la misma función evaluada en dos argumentos distintos**. Al dividir se cancelan σ, θ,
c, τ y la unidad de muestreo, y queda

> **R = epistémico/aleatorio = (H/T)^(½−d)**
>
> **n_eff = 1/R² = (T/H)^(1−2d) ≤ T/H**, con igualdad solo si d = 0.

La memoria larga **engrosa** el muro. Nunca lo abre.

El error concreto de N22, que D1 localizó con un control exacto: promediar dentro del
horizonte mejora θ̂ por un factor H/τ, pero **concentra IV_H por exactamente el mismo
factor**. Son el mismo H/τ. Con un Ornstein–Uhlenbeck de τ=1 semana y H/τ=504 —mixing
perfecto, la premisa de N22 satisfecha con holgura— el n_eff medido es **4,992**, no 2.520.
La ganancia de ×4,3 que N22 reclamaba comparaba un estimador afilado contra un objetivo
sin afilar.

**N22 baja de 0,70 a 0,15. Refutado, no debilitado.**

## El umbral no existía

El «d ≈ 0,37» que organizó todo el ciclo resultó ser `d* = log(H/τ)/(2·log(T/τ))`, un
**artefacto de unidades**: varía entre 0,19 y 0,43 al mover τ o H. No es una frontera
estructural.

Los umbrales de teorema existen y son otros: `d*_m = ½(1−1/m)` de la jerarquía de rango de
Hermite (Taqqu; Dobrushin–Major): 0, ¼, ⅓, **3/8**, … → ½.

Y aquí aparece algo que no buscaba nadie: **3/8 = 0,375 es el umbral de rango 4, es decir
la condición de cuarto momento — N06 otra vez**, llegando por un camino completamente
distinto. Pero con el sentido invertido: por debajo de 3/8 el muro *satura* en T/H, por
encima *empeora*. La coincidencia numérica con el 0,3742 era real y engañosa (N44).

## Dos agentes que parecían contradecirse

D2 midió que cinco procesos con d̂ ∈ [0,36; 0,41] —indistinguibles, AUC 0,52–0,65— tienen
n_eff real entre **7,2 y 331,4**. Factor 46. Concluyó: d no es identificable.

D3 midió lo contrario: bajo estacionariedad y especificación correcta, local Whittle con
T=100 años da SE=0,019 y sesgo <0,002, y clasifica bien el 84–97% de las veces. Y lo
reportó como **fallo de su propio ataque**, que es la clase de honestidad que hace que esto
funcione.

No se contradicen. El conjunto de D2 incluye alternativas **no estacionarias** —saltos de
nivel, regímenes Pareto—, y ahí, como dice D3, «el problema no es el umbral sino la
inexistencia de la ley invariante». Dentro de los estacionarios d se estima bien y la
escapatoria está cerrada igualmente por N40. Entre estacionarios y no estacionarios d̂ no
distingue, y entonces no hay nada que estimar.

**N22 muere en los dos casos, por razones distintas** (N42). Y como subproducto queda
acotado N24: el patrón de no identificabilidad es específico de fronteras de momento, no
universal.

## El muro se sella a sí mismo

El hallazgo más autorreferencial vino de D2 (N33). El error estándar de d̂ restringido a
frecuencias limpias es ≈ (1−d)/√K, donde K = T/τ_reg **es el propio n_eff**. Resolver d a
±δ exige `n_eff ≥ ((1−d)/δ)²`. Separar n_eff=5 de n_eff=20 exige n_eff ≈ 400.

> Certificar que la evidencia es suficiente requiere que la evidencia ya sea suficiente.
> Una cota sobre la evidencia solo es verificable cuando ya ha sido superada.

Y el acompañante (N34): subir el ancho de banda de m=n^0,5 a n^0,7 divide el error estándar
de d̂ por 2,7 —de 0,052 a 0,019— y lleva la exactitud de clasificación entre clases a
**0,48–0,51, azar puro**. Más precisión, menos información. Es el mismo patrón que N01
(muestrear más fino no informa sobre el drift) y que N24 (clasificación al 22%). Tres
instancias de lo mismo.

## Un error nuestro, arrastrado desde el ciclo 1

`T_eff = T^(1−2d)` no es invariante a unidades: esconde un τ. La forma correcta, que se
deduce de R = (H/T)^(½−d), es

> **T_eff = H^(2d) · T^(1−2d)** — media geométrica ponderada entre H y T.

Con T=100 años, H=10 años, d=0,4 da **15,8 años**, no los 2,5 que el grafo llevaba
arrastrando. Límites correctos: d=0 ⇒ T_eff=T; d→½ ⇒ T_eff→H. **El ciclo 1 subestimaba por
un factor de 6,3.** La situación es menos grave de lo que creíamos, y conviene decirlo con
la misma claridad con que se dijo lo contrario.

D3 propuso una corrección distinta (T_eff = τ(T/τ)^(1−2d) = 8,1 días). Adjudico a favor de
D1: su derivación es autoconsistente con la definición de T_eff vía R, y demuestra
explícitamente que τ se cancela —verificado idéntico a 1 día, 21 días, 63 días y 252 días—.
La de D3 mantiene τ dentro, que es justo lo que D1 prueba que no puede estar.

## Lo que se lleva D3, y dónde estaba la escapatoria de verdad

D3 midió que la **anchura** —la dispersión entre bloques de H años, que es lo que fija el ES
y el capital— es casi insensible a d: n_eff cae solo de 9,2 a 7,6 al pasar d de 0 a 0,4,
frente a 10. Mientras la **ubicación** se degrada de 10 a 1,59.

> N22 y N03 nunca compitieron: operan sobre coordenadas ortogonales del estimando. La
> escapatoria, aunque hubiera funcionado, habría mejorado la coordenada equivocada (N39).

Es la partición del eje P del ciclo 2 —anchura contra ubicación— reapareciendo medida.

Y D1 encontró dónde sí hay escapatoria, en un nodo que nadie estaba mirando: bajo memoria
larga ρ(H) ∝ H^(2d−1) en vez de 1/(κH), y corr(v₀, IV_10a) pasa de 0,066 con un OU de
τ=1 mes a **0,397 con d=0,40**. La cuota del estado presente no es el 2% de N17 sino el
20–40%. Es un cambio de constante y no de tasa, pero es real (N46).

## «H ≫ τ» no es lejano: es vacío

D1 verificó que agregar a cualquier escala deja el punto fijo `ρ₁* = 2^(2d) − 1 > 0` para
todo d>0 —idéntico a 1 día, 21 días, 252 días y 1260 días, mientras un AR(1) colapsa de
0,953 a 0,045—. **Ninguna escala vuelve iid la volatilidad.** El horizonte necesario para
que CV(IV_H)=0,1 es 8 años con d=0, 1.220 años con d=0,26 y **8·10⁸ años con d=0,40** (N45).

## Un conflicto sin resolver

El CV ∝ H^(−0,24) de N05 implica d = 0,26 exactamente. Pero ese d predice
ES99(GJR)/ES99(GBM) = 1,375 a 20 años frente al 1,62 observado. Y el d=0,26 de un GJR
simulado es memoria *corta* con τ enorme, no memoria larga genuina.

Hay dos d incompatibles en el grafo: 0,40 (N12) y 0,26 (N05). Queda abierto como N47.

## Salida hacia el ciclo 4

La grieta se movió al **eje E (estacionariedad)**, y coincide con el encargo de la auditoría
de novedad. Todo el edificio —n_eff, T_eff, R(H), ES, capital— presupone que existe una ley
invariante que estimar. Si esa presuposición es ella misma indecidible, el edificio entero
descansa sobre un supuesto no verificable, y *eso* es el teorema.

> ¿Se puede decidir, con T años de datos, si el proceso tiene una ley invariante — y puede
> demostrarse que no, como **cota inferior minimax de Le Cam** en vez de como meseta
> empírica?
