# Nota del orquestador — la torre del drift

No es un informe de agente. Es lo que veo yo al cruzar B1 y B2, que llegaron desde
posiciones opuestas del eje P y produjeron el mismo hecho estructural sin ponerlo de
titular ninguno de los dos.

## La tabla que lo dice todo

| | B1 (libre de modelo) | B2 (paramétrico) |
|---|---|---|
| refutar un error del 20% en la **varianza** | ~4 días (a 5-min) | ~2,5 días |
| refutar un error del 20% en el **drift** | ~800 años | ~37 años |
| cuota decisional de lo refutable rápido | ≤25% del crecimiento | ~2% del bienestar |
| dónde reaparece el drift | «recursa por toda la jerarquía de volatilidad» | «θ es el drift de v; reaparece un nivel arriba» |

Los dos números de la última fila son la misma frase dicha dos veces, y ninguno la
reclamó como hallazgo principal. **Lo es.**

## Lo que creo que es el hallazgo del ciclo

El drift no es *un* parámetro inestimable. Es una **posición estructural** dentro de una
jerarquía, y esa posición se reproduce en cada nivel.

- Nivel 0, el precio: su drift μ tiene SE = σ/√T. Inestimable in-fill (N01).
- Nivel 1, la varianza: su *estado* v_t sí es estimable in-fill con precisión arbitraria.
  Pero su comportamiento a horizonte largo lo fija θ, la media de largo plazo — que es el
  **drift del proceso de varianza**, con SE(θ̂)/θ = η/(κ√(2θT)) ∝ 1/√T.
- Nivel 2: la media de largo plazo de θ tendría su propio drift. Y así.

Subir un nivel no resuelve el problema: lo traslada. Cada nivel regala su *presente* y
cobra su *futuro* al mismo precio, 1/√T.

## La cuenta que lo hace cuantitativo

La contribución del estado presente observable al riesgo a horizonte H, en un nivel con
reversión κ, es

```
ρ(H) = (1 − e^(−κH)) / (κH)   →   1/(κH)  cuando H ≫ 1/κ
```

Con κ=5 y H=10 años: **2%**. El 98% de ⟨M⟩_H lo fija θ, no v₀.

Generalizando a una jerarquía con niveles k de reversión κ_k y pesos w_k, la cuota
observable es

```
Ω(H) = Σ_k w_k · (1 − e^(−κ_k H)) / (κ_k H)
```

y **Ω(H) → (1/H)·Σ_k w_k/κ_k → 0** cuando H → ∞.

Los datos de alta frecuencia dan el presente con precisión ilimitada y el futuro con
precisión nula. En cuanto H supera el tiempo de mezcla del nivel más rápido, la precisión
del presente deja de importar. **Esto es N08 —el colapso de canal— derivado por otra
ruta, y le pone la tasa: 1/(κH).**

## La inversión que nadie ha señalado

Hay un caso en el que Ω(H) no decae: **κ = 0**, volatilidad no estacionaria.

Si la varianza es un paseo aleatorio, E[v_H | v₀] = v₀. No hay θ que estimar. El estado
presente *es* el pronóstico, y la cuota observable es 1.

Es decir: **cuanto más no estacionaria es la volatilidad, mejor se pronostica su nivel
medio a horizonte largo — y peor se comporta su cola** (N06: M2 > 1, cuarto momento
infinito). Las dos patologías apuntan en direcciones opuestas.

Eso no lo dijo ninguno de los dos agentes y no lo he visto en la literatura. Es la clase
de tensión de la que suele salir un teorema, y va al ciclo 3.

## Lo que corrige del grafo

B2 tiene razón en debilitar N09. La escisión de Dambis–Dubins–Schwarz en «ley de ⟨M⟩ +
saltos + drift» **no es invariante gauge**: bajo un cambio equivalente de medida cambian
las dos piezas, porque la prima de riesgo de varianza mueve la ley de ⟨M⟩ y el
compensador de saltos es él mismo un drift (Esscher). B1 llega a lo mismo por Esscher.
Dos rutas, misma corrección.

Así que **N13 —la síntesis con la que cerró el ciclo 1— estaba mal planteada.** Decía que
un funcional invariante al drift sería estimable in-fill, y eso solo vale en la versión
débil de la invarianza y solo para H ≪ 1/κ. Se degrada, y su degradación es el resultado
del ciclo 2.

## La frase corta

El ciclo 1 encontró que el drift es el único canal irreducible. El ciclo 2 encuentra que
*«el drift» no es un canal sino un piso de una torre*, y que la torre no tiene último
piso. Lo que se refuta rápido es lo que no decide; lo que decide no se refuta.
