# GRAFO — conexiones neuronales de la investigación

Formato en `FORMATO.md`. IDs estables: cítalos por ID, no reexpliques el concepto.

## Nodos

N01 ≡ El drift es inestimable in-fill: I(μ)=T/σ² no depende de la frecuencia. Girsanov — cambiar μ da medidas equivalentes, cambiar σ las da singulares. SE(μ̂)=σ/√T es un suelo, no una elección   [C01·A2] w=.95
N02 ≡ Invariante adimensional R(H)=√(H/T_eff)=epistémico/aleatorio. Sin σ ni μ dentro. H*=T_eff es donde R=1 y el error de estimar supera a la aleatoriedad   [C01·A1,A2 ⊕] w=.89
N03 ≡ n_eff=T/H (no T·252) gobierna TODA falsabilidad. T_req≈11,4·H/p para poder 80%. VERIFICADO: n=1070 medido vs 1140 predicho   [C01·A1,A2,A3 ⊕] w=.92
N04 ≡ El MC reporta el error de integración (1/√N, elegido) y oculta el de inferencia (√(H/T), heredado). Subreporte ≈√(N·H/T), CRECIENTE en N   [C01·A2,A3 ⊕] w=.93
N05 ≡ La escalera NO colapsa a GBM en ningún horizonte humano. CV de varianza integrada decae H^−0,24 y no H^−0,5; ES99(GJR)/ES99(GBM)=1,77 a 1a y 1,62 a 20a   [C01·A1] w=.85
N06 ≡ Frontera de fase M2=E[(α+γ1{ε<0}+β)²]=1 empíricamente NO identificable: las acciones caen en M2≈1,0085±0,02 y la curtosis muestral (3,6→5,5) no distingue una poblacional de 13,5 de una infinita   [C01·A1 +verif] w=.90
N07 ≡ EVT no es ajustable a horizonte largo: N_u=p_u·T/H. A H=10a con bloques no solapados N_u≈0,5. Toda aplicación de EVT a largo plazo usa solapamiento o una regla de agregación asumida   [C01·A2] w=.80
N08 ≡ Colapso de canal: a H≫τ (mezcla) el futuro es cond. indep. del pasado dado θ, luego I(datos;futuro) ≤ I(datos;θ) ≈ (d/2)log₂T ≈ 50 bits. Toda la información pasa por θ   [C01·A3] w=.80
N09 ≡ Dambis–Dubins–Schwarz: la ley de TODO funcional de trayectoria depende solo de la ley de ⟨M⟩_H más los saltos. La escalera entera es una reparametrización de ⟨M⟩. Solo el drift queda fuera   [C01·A3] w=.72
N10 ≡ Reflexividad: el estimando no está quieto, P=Φ(P̂). Migración de cola — tras estandarizarse una métrica, la crisis siguiente nace fuera de su perímetro (Basilea I→1998, VaR→2008, FRTB→2023)   [C01·A3] w=.68
N11 ≡ N*≈T_eff/(H(1−q)): existe un número de trayectorias más allá del cual simular es teatro. T=20a,H=10a,q=.99 ⇒ N*≈200. Correr 40.000 es precisión espuria de 2 órdenes   [C01·A1] w=.75
N12 ≡ T_eff=T^(1−2d) con d≈0,4 (memoria larga de |r|) ⇒ con T=100a, T_eff≈2,5a. El horizonte epistémico se mide en AÑOS, no en décadas   [C01·A1] w=.70
N13 ≡ SÍNTESIS: el drift es el único canal irreducible Y es exactamente la dirección en la que las medidas son equivalentes. Un funcional invariante al drift sería estimable in-fill — ahí está la salida, si existe   [C01·⊕] w=.80
N14 ≡ SÍNTESIS: la escalera añade ESTRUCTURA, no INFORMACIÓN. Cambia la respuesta (N05) sin cambiar lo que puede saberse (N08). Resuelve la tensión: subir peldaños mueve el número y no mueve el conocimiento   [C01·⊕] w=.75

## Aristas

N01 ⊕ N09 ⇒ N13      el drift es lo único fuera de ⟨M⟩, y lo único no estimable in-fill
N05 ⊥ N08            la escalera cambia el número pero no aporta información
N05 ⊕ N08 ⇒ N14      resolución de esa tensión
N03 → N07            n_eff explica por qué EVT no se puede ajustar a H largo
N03 → N11            el mismo conteo fija cuándo dejar de simular
N02 → N11
N01 → N02            SE(μ̂)=σ/√T es el numerador del invariante
N12 ⊣ N02            T_eff≪T empeora R(H) en un orden de magnitud
N06 ⊣ N05            la frontera que decide el ritmo de agregación no es localizable
N10 ⊣ N03            si el estimando se mueve, ni siquiera n_eff está bien definido

N15 ≡ El sesgo del estimador en el filo TIENE DIRECCIÓN: con 20a de datos el MLE sitúa M̂2<1 el 80% de las veces en que la verdad es M2>1. No es que no se pueda estimar — es que se estima mal hacia el lado tranquilizador. Precisión de clasificación 52,9% vs 50% de azar   [C01·A1 + verificación propia] w=.90
