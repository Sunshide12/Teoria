# Ciclo 8 — La precedencia primero

**Encargo:** auditar T5, cerrar la grieta del eje E, escribir el protocolo de falsación.
**Agentes:** I1, I2, I3. **I2 murió sin informar** (límite de tasa). Asumí su papel.

---

## Lo que pasó

T5 —«la regla √t convierte la medida de capital en medida de desviación»— era, tras siete
ciclos, lo más parecido a un teorema que teníamos. I1 lo mató dos veces en el mismo
informe.

**Primero por precedencia.** Danielsson & Zigrand (2006), *JBF* 30(10):2701–2713, **36
ocurrencias de «drift»**. §3 ec.(4): *«Absent the drift term −μηk, it embodies the
square-root-of-time rule»*. §4 se titula *«More on Scaling with a Positive Drift»*. El
mecanismo, el diagnóstico, el nombre y hasta la racionalización de los diez días de
Basilea: todo publicado hace veinte años, **por el mismo autor y en la misma revista que
el grafo ya señalaba como rival**.

**Después por las matemáticas.** La pieza axiomática de T5 usaba la biyección de
Rockafellar–Uryasev–Zabarankin, `R(X) = D(X) − E[X]`, para argumentar que `k_α·σ` es una
desviación disfrazada de capital. Esa biyección **sólo vale bajo dominancia de rango
inferior**, `D(X) ≤ E[X] − inf X`, que `k_α·σ` viola para todo `k_α > 1` — o sea, para
todo `α > 61,89%` en el ES. Contraejemplo verificado: `X=(0,0)`, `Y=(0,10)`, `Y ≥ X`
puntualmente, y sin embargo `R(X)=0 < R(Y)=8,33`. **Viola monotonía.**

No es cuestión de precedente. **Apliqué una biyección sin comprobar la condición bajo la
que vale.**

## Y nuestra propia auditoría tenía un error de muestreo

El nodo N91 afirmaba cero ocurrencias de «drift» en 64 páginas de la literatura rival.
Extrajo Danielsson 2002 y DJVZ 2016 — **los dos artículos donde efectivamente no está**—
y **omitió Danielsson–Zigrand 2006**, mismo autor, misma revista, y sobre la regla √t
específicamente. Ese nodo sostuvo cinco ciclos. Bajó de 0,92 a **0,05**.

## Lo que I3 construyó sobre las ruinas

Si la tesis está publicada, ¿qué queda? I3 respondió: **su irresolubilidad, fechada.**

- El estadístico de la brecha es `ĝ = μ̂√H/(k_α σ)`, con `SE(ĝ) = √(H/T)/k_α`, libre de
  σ y de μ. Luego `t = Ŝ√T` y **H se cancela exactamente**: el tamaño de muestra
  necesario es el mismo para diez días que para treinta años. Verificado: `t = 2,8016`
  idéntico en los cuatro horizontes.
- Con `Ŝ=0,375`: **T_req = 55,8 años**. Una década con umbral `g<0,20` da tamaño 21,4% y
  potencia 40,6%: **2036 no puede resolver nada**.
- Techo transversal: `T_eff ≤ T/ρ̄`. Con ρ̄=0,6, todos los mercados del mundo durante una
  década son **16,7 años efectivos**. Fechas mínimas: **2059** (pool) y **2082** (serie
  única).

Y la pieza que resultó ser la más importante del ciclo, aunque parecía burocracia:

> **Captura-recaptura de Chapman sobre nuestras propias búsquedas.** n₁=7, n₂=4,
> solapamiento m=1 ⇒ N̂=19 con 10 vistas: **47% de la literatura relevante sin ver.**
> Regla: ninguna afirmación de novedad es admisible mientras la fracción no vista supere
> el 20%.

Y el criterio que distingue «es nuevo» de «no lo hemos buscado bien»: **el claim debe
implicar un número que un artículo publicado calcule distinto.**

## El orden que sale de aquí

`resolve.py` ejecuta el test **bibliográfico antes que el empírico**. Si devuelve
precedente anterior a la fecha de preregistro, el veredicto es MOOT y no se resuelve
empíricamente.

No es una preferencia de estilo. **Este ciclo es la demostración: seis consultas
resolvieron en un día lo que el test empírico habría tardado 56 años.**

## Balance

Sexta retractación. El ciclo 8 no produjo un teorema: produjo **la regla que impide
publicar teoremas antes de haber buscado**, y la aplicó contra sí mismo el mismo día.

**Pregunta para el ciclo 9:** no simular. Gastar el presupuesto entero en un segundo
buscador con consultas disjuntas, y bajar la masa no vista por debajo del 20%.
