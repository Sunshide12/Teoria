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
N09 ≡ [DEBILITADO C02] Dambis–Dubins–Schwarz: la ley de TODO funcional de trayectoria depende solo de la ley de ⟨M⟩_H más los saltos. La escalera entera es una reparametrización de ⟨M⟩. Solo el drift queda fuera   [C01·A3] w=.55
N10 ≡ Reflexividad: el estimando no está quieto, P=Φ(P̂). Migración de cola — tras estandarizarse una métrica, la crisis siguiente nace fuera de su perímetro (Basilea I→1998, VaR→2008, FRTB→2023)   [C01·A3] w=.68
N11 ≡ N*≈T_eff/(H(1−q)): existe un número de trayectorias más allá del cual simular es teatro. T=20a,H=10a,q=.99 ⇒ N*≈200. Correr 40.000 es precisión espuria de 2 órdenes   [C01·A1] w=.75
N12 ≡ T_eff=T^(1−2d) con d≈0,4 (memoria larga de |r|) ⇒ con T=100a, T_eff≈2,5a. El horizonte epistémico se mide en AÑOS, no en décadas   [C01·A1] w=.70
N13 ≡ [DEGRADADO C02: solo vale en invariancia débil y H≪1/κ] SÍNTESIS: el drift es el único canal irreducible Y es exactamente la dirección en la que las medidas son equivalentes. Un funcional invariante al drift sería estimable in-fill — ahí está la salida, si existe   [C01·⊕] w=.62
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

N16 ≡ [CASI: Phillips-Yu 2005, Tang-Chen 2009 ya tienen el piso. Solo la RECURSIÓN es nueva, y hay que demostrarla invariante de nivel] **TORRE DEL DRIFT**: el drift no es un canal sino una posición estructural que se reproduce en cada nivel de la jerarquía de volatilidad. θ (media de largo plazo de v) es el drift de v, con SE(θ̂)/θ=η/(κ√(2θT)) ∝ 1/√T. Subir un nivel traslada el problema, no lo resuelve   [C02·B1,B2 ⊕ +orq] w=.60
N17 ≡ Contribución del estado presente observable a horizonte H con reversión κ: ρ(H)=(1−e^{−κH})/(κH) → 1/(κH). Con κ=5, H=10a: **2%**. Alta frecuencia da el presente con precisión ilimitada y el futuro con precisión nula   [C02·B2 +orq] w=.88
N18 ≡ **CUOTA DECISIONAL INVARIANTE**: la parte del problema de decisión accesible a un funcional drift-invariante es de unidades porcentuales. Vol constante Φ=2S²/m (0,13% diario); Heston Φ_∞=S²η²/(2κ²θ+S²η²)≈2%; techo universal **1/4** (solo si ⟨σ²⟩⟨σ⁻²⟩=2). Los tres agentes   [C02·B1,B2,B3 ⊕] w=.94
N19 ≡ [PUBLICADO: Rockafellar-Uryasev-Zabarankin 2006 — NO es hallazgo nuestro] **MONETARIEDAD ⊥ INVARIANCIA**: toda medida de riesgo aditiva en efectivo es Girsanov-equivariante (se desplaza en ∫θσds). La frontera Artzner(coherente)/Rockafellar(desviación) ES la frontera de Girsanov. Margen y vol-target son drift-libres por necesidad matemática; ES y capital económico no pueden serlo jamás   [C02·B3] w=.25
N20 ≡ **COLAPSO DE VILLE POR SATURACIÓN**: si el nulo está saturado por equivalencia, todo e-proceso cumple ess-sup E_τ≤1 → error tipo I exactamente 0 y escala de evidencia vacía. Deja de ser test y pasa a certificado cuasi-seguro. Corolario: todo funcional invariante a cambio equivalente con Fatou colapsa al ess-sup   [C02·B3, corrobora B2(iii), REFUTA B1-C4] w=.87
N21 ≡ **ANIQUILACIÓN CLARK–OCONE**: si Ψ(P)=E_P[φ] es invariante bajo TODA Q~P, entonces E[D_tφ|F_t]=0 y φ es c.s. constante. (b-fuerte) no admite funcional no trivial, y (b-débil)="depende solo de la ley de ⟨M⟩_H" NO es equivalente: presupone la escisión, o sea ya es paramétrica   [C02·B2] w=.83
N22 ≡ **ESCAPATORIA ERGÓDICA**: si H≫τ_vol, Ψ deja de ser funcional de la ley TERMINAL y pasa a serlo de la ley INVARIANTE, con n_eff=(T/τ)^(1−2d) en vez de T/H. Con d=0,26, T=50a, τ=1mes: n_eff pasa de 5 a 21,6. **UMBRAL: la puerta se cierra si d > ≈0,37**, y el d≈0,4 de N12 la deja cerrada — pero dentro del error de estimación   [C02·B3] w=.70
N23 ≡ **PARTICIÓN DEL EJE P**: la grieta P no era desacuerdo sino dos preguntas confundidas. Libre de modelo acierta en la ANCHURA (desviación, margen); paramétrico es imprescindible para la UBICACIÓN (capital, ES)   [C02·⊕] w=.85
N24 ≡ [FLANCO: Hall-Yao 2003 — el sesgo plano podría ser su no-regularidad. Reconciliar ANTES de reclamar] La frontera M2=1 **no es identificable a ningún T**: el sesgo del MLE no encoge (−0,018 a 10a, −0,015 a 80a) mientras el SE sí (0,0124→0,0038). RMSE se estanca en ~0,015 > |M2−1|=0,011. Sospecha: el sesgo se hereda de ν̂, el índice de cola de la innovación — o sea N07 reapareciendo   [verificación propia] w=.70
N25 ≡ [CASI: Merton 1980 + Chopra-Ziemba 1993. Solo vale si se convierte en DESIGUALDAD general] **Lo que se refuta rápido es lo que no decide.** Refutar un error del 20% en varianza: ~4 días. En drift: 37–800 años. Ratio 10⁴–10⁵. Y la cuota decisional (N18) va exactamente al revés   [C02·B1,B2,B3 ⊕] w=.55
N26 ≡ **INVERSIÓN κ=0**: si la volatilidad es no estacionaria (κ=0), E[v_H|v₀]=v₀ y no hay θ que estimar — la cuota observable es 1. Cuanto más no estacionaria la vol, MEJOR se pronostica su nivel medio y PEOR se comporta su cola. Las dos patologías apuntan en direcciones opuestas   [C02·orq] w=.60

## Aristas (ciclo 2)

N16 ⊣ N13            la torre degrada la síntesis del ciclo 1: no hay "el" drift que esquivar
N21 ⊣ N09            Clark–Ocone niega que la escisión DDS sea invariante gauge
N20 ⊣ N-B1C4         el colapso refuta que la invariancia REGALE refutabilidad: la regala vacía
N18 ⊥ N25            lo relevante y lo refutable son ortogonales
N19 → N23            la frontera Artzner/Rockafellar explica la partición
N22 ⊣ N03            única ruta conocida que podría batir n_eff=T/H
N24 ⊕ N22 ⇒ DOS fronteras de fase no identificables: M2=1 y d≈0,37
N26 ⊥ N06            no estacionariedad: buena para el nivel, catastrófica para la cola
N24 → N07            el sesgo de M̂2 se heredaría del índice de cola — a verificar

N27 ≡ **COMPLEJIDAD ÓPTIMA DECRECIENTE EN H** (verificado): modelo óptimo por RMSE = GJR-t+EVT(8p) a 1 mes → GARCH-N(4p) a 1 año → GBM(2p) a 10 años. La sofisticación que gana a corto pierde a largo. MATIZ: a 10a todos fallan (RMSE mínimo 47%); GBM gana por ser el menos catastrófico, no por ser bueno   [C02·orq, verificado] w=.85
N28 ≡ **LA COLA DEL ERROR**: la distribución de error de un modelo de cola hereda las colas gordas del fenómeno que modela. A 10a el modelo EVT tiene RMSE 377% con mediana 43,6% (razón 8,7); el GBM 47,0%/35,1% (razón 1,34). El coste de la sofisticación no se paga en error típico sino en frecuencia de error catastrófico — y nadie lo mide porque nadie reporta la distribución del error de su modelo, solo el número   [C02·orq, verificado] w=.80

N27 → N28            la monotonía y la curtosis del error son el mismo fenómeno visto dos veces
N28 → N07            EVT no ajustable a H largo, apareciendo de forma dinámica en vez de estática
N27 ⊣ N05            la escalera no colapsa a GBM, pero a H largo conviene usar GBM igualmente

N29 ≡ **EL RIVAL**: Pástor–Stambaugh 2012 (JF 67(2):431–478) es el mismo programa ya ejecutado — riesgo a largo plazo sin tratar los parámetros como conocidos, descompuesto en componentes epistémicos, con conclusión que invierte la sabiduría convencional. Ellos bayesianos sobre varianza predictiva; nosotros frecuentistas sobre medidas de cola. Tratar como rival, no como cita   [auditoría A01] w=.95
N30 ≡ **ENCARGO LE CAM**: para que N24 sea teorema y no observación hace falta una cota inferior minimax — dos puntos M2 = 1 ∓ cT^(−a) y demostrar que ninguna sucesión de tests los separa con probabilidad → 1. Una meseta de RMSE es una observación; una cota de Le Cam es un teorema   [auditoría A01] w=.90
N31 ≡ **ENCARGO ÍNDICE DE COLA**: para que N28 sea teorema hay que derivar el índice de cola de la distribución del error de ES ligándolo al error de estimación de la persistencia. El error de ES es ~exponencial en (error de persistencia × horizonte) ⇒ lognormalidad/cola de potencia de forma mecánica   [auditoría A01] w=.88
N32 ≡ **ENCARGO DESIGUALDAD**: N25 solo sobrevive como (información de Fisher sobre θᵢ)×(peso decisional de θᵢ) ≤ C, uniforme sobre una clase de modelos. Sin esa desigualdad es folclore con decimales   [auditoría A01] w=.85

N29 ⊣ (todo el programa)   hay que superarlo, no citarlo
N30 → N24 · N31 → N28 · N32 → N25
