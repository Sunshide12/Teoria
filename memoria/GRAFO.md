# GRAFO — conexiones neuronales de la investigación

Formato en `FORMATO.md`. IDs estables: cítalos por ID, no reexpliques el concepto.

## Nodos

N01 ≡ El drift es inestimable in-fill: I(μ)=T/σ² no depende de la frecuencia. Girsanov — cambiar μ da medidas equivalentes, cambiar σ las da singulares. SE(μ̂)=σ/√T es un suelo, no una elección   [C01·A2] w=.97
N02 ≡ Invariante adimensional R(H)=√(H/T_eff)=epistémico/aleatorio. Sin σ ni μ dentro. H*=T_eff es donde R=1 y el error de estimar supera a la aleatoriedad   [C01·A1,A2 ⊕] w=.93
N03 ≡ [**NO ES NUESTRO** — literal en Danielsson 2002 §3.5: «si se usan 250 días para un VaR diario hacen falta diez años para un VaR a 10 días con la misma precisión». Sobrevive la verificación numérica (1070 vs 1140), no el concepto] n_eff=T/H (no T·252) gobierna TODA falsabilidad. T_req≈11,4·H/p para poder 80%. VERIFICADO: n=1070 medido vs 1140 predicho   [C01·A1,A2,A3 ⊕] w=.55
N04 ≡ El MC reporta el error de integración (1/√N, elegido) y oculta el de inferencia (√(H/T), heredado). Subreporte ≈√(N·H/T), CRECIENTE en N   [C01·A2,A3 ⊕] w=.93
N05 ≡ La escalera NO colapsa a GBM en ningún horizonte humano. CV de varianza integrada decae H^−0,24 y no H^−0,5; ES99(GJR)/ES99(GBM)=1,77 a 1a y 1,62 a 20a   [C01·A1] w=.82
N06 ≡ Frontera de fase M2=E[(α+γ1{ε<0}+β)²]=1 empíricamente NO identificable: las acciones caen en M2≈1,0085±0,02 y la curtosis muestral (3,6→5,5) no distingue una poblacional de 13,5 de una infinita   [C01·A1 +verif] w=.45
N07 ≡ EVT no es ajustable a horizonte largo: N_u=p_u·T/H. A H=10a con bloques no solapados N_u≈0,5. Toda aplicación de EVT a largo plazo usa solapamiento o una regla de agregación asumida   [C01·A2] w=.80
N08 ≡ Colapso de canal: a H≫τ (mezcla) el futuro es cond. indep. del pasado dado θ, luego I(datos;futuro) ≤ I(datos;θ) ≈ (d/2)log₂T ≈ 50 bits. Toda la información pasa por θ   [C01·A3] w=.80
N09 ≡ [DEBILITADO C02] Dambis–Dubins–Schwarz: la ley de TODO funcional de trayectoria depende solo de la ley de ⟨M⟩_H más los saltos. La escalera entera es una reparametrización de ⟨M⟩. Solo el drift queda fuera   [C01·A3] w=.55
N10 ≡ Reflexividad: el estimando no está quieto, P=Φ(P̂). Migración de cola — tras estandarizarse una métrica, la crisis siguiente nace fuera de su perímetro (Basilea I→1998, VaR→2008, FRTB→2023)   [C01·A3] w=.82
N11 ≡ N*≈T_eff/(H(1−q)): existe un número de trayectorias más allá del cual simular es teatro. T=20a,H=10a,q=.99 ⇒ N*≈200. Correr 40.000 es precisión espuria de 2 órdenes   [C01·A1] w=.75
N12 ≡ [C03: d̂≈0,4 es igualmente compatible con d=0 y n_eff=100-330; T_eff=T^(1-2d) solo vale si la clase ARFIMA es cierta] **T_eff = H^(2d)·T^(1−2d)** (media geométrica ponderada entre H y T). Con T=100a, H=10a, d=0,4: **T_eff=15,8 años**, no 2,5. Límites: d=0⇒T_eff=T; d→½⇒T_eff→H. La versión del ciclo 1 subestimaba ×6,3. El horizonte epistémico se mide en AÑOS, no en décadas   [C01·A1] w=.80
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

N16 ≡ [CASI: Phillips-Yu 2005, Tang-Chen 2009 ya tienen el piso. Solo la RECURSIÓN es nueva, y hay que demostrarla invariante de nivel] **TORRE DEL DRIFT**: el drift no es un canal sino una posición estructural que se reproduce en cada nivel de la jerarquía de volatilidad. θ (media de largo plazo de v) es el drift de v, con SE(θ̂)/θ=η/(κ√(2θT)) ∝ 1/√T. Subir un nivel traslada el problema, no lo resuelve   [C02·B1,B2 ⊕ +orq] w=.88
N17 ≡ Contribución del estado presente observable a horizonte H con reversión κ: ρ(H)=(1−e^{−κH})/(κH) → 1/(κH). Con κ=5, H=10a: **2%**. Alta frecuencia da el presente con precisión ilimitada y el futuro con precisión nula   [C02·B2 +orq] w=.92
N18 ≡ **CUOTA DECISIONAL INVARIANTE**: la parte del problema de decisión accesible a un funcional drift-invariante es de unidades porcentuales. Vol constante Φ=2S²/m (0,13% diario); Heston Φ_∞=S²η²/(2κ²θ+S²η²)≈2%; techo universal **1/4** (solo si ⟨σ²⟩⟨σ⁻²⟩=2). Los tres agentes   [C02·B1,B2,B3 ⊕] w=.95
N19 ≡ [PUBLICADO: Rockafellar-Uryasev-Zabarankin 2006 — NO es hallazgo nuestro] **MONETARIEDAD ⊥ INVARIANCIA**: toda medida de riesgo aditiva en efectivo es Girsanov-equivariante (se desplaza en ∫θσds). La frontera Artzner(coherente)/Rockafellar(desviación) ES la frontera de Girsanov. Margen y vol-target son drift-libres por necesidad matemática; ES y capital económico no pueden serlo jamás   [C02·B3] w=.25
N20 ≡ **COLAPSO DE VILLE POR SATURACIÓN**: si el nulo está saturado por equivalencia, todo e-proceso cumple ess-sup E_τ≤1 → error tipo I exactamente 0 y escala de evidencia vacía. Deja de ser test y pasa a certificado cuasi-seguro. Corolario: todo funcional invariante a cambio equivalente con Fatou colapsa al ess-sup   [C02·B3, corrobora B2(iii), REFUTA B1-C4] w=.87
N21 ≡ **ANIQUILACIÓN CLARK–OCONE**: si Ψ(P)=E_P[φ] es invariante bajo TODA Q~P, entonces E[D_tφ|F_t]=0 y φ es c.s. constante. (b-fuerte) no admite funcional no trivial, y (b-débil)="depende solo de la ley de ⟨M⟩_H" NO es equivalente: presupone la escisión, o sea ya es paramétrica   [C02·B2] w=.83
N22 ≡ [REFUTADO C03·D1] **CANCELACIÓN ERGÓDICA**: promediar dentro del horizonte es una transformación GAUGE. Mejora θ̂ por H/τ y concentra IV_H por el mismo H/τ. Control exacto OU con H/τ=504: n_eff=4,992, no 2.520. El «umbral d≈0,37» era artefacto de unidades — τ se cancela. Lo que era: si H≫τ_vol, Ψ deja de ser funcional de la ley TERMINAL y pasa a serlo de la ley INVARIANTE, con n_eff=(T/τ)^(1−2d) en vez de T/H. Con d=0,26, T=50a, τ=1mes: n_eff pasa de 5 a 21,6. **UMBRAL: la puerta se cierra si d > ≈0,37**, y el d≈0,4 de N12 la deja cerrada — pero dentro del error de estimación   [C02·B3] w=.15
N23 ≡ **PARTICIÓN DEL EJE P**: la grieta P no era desacuerdo sino dos preguntas confundidas. Libre de modelo acierta en la ANCHURA (desviación, margen); paramétrico es imprescindible para la UBICACIÓN (capital, ES)   [C02·⊕] w=.90
N24 ≡ [**REFUTADO C04·E1** — ESCINDIDO en N24a/N24b. El flanco Hall-Yao queda descartado: ν≈7>4, el QMLE es regular] La frontera M2=1 **no es identificable a ningún T**: el sesgo del MLE no encoge (−0,018 a 10a, −0,015 a 80a) mientras el SE sí (0,0124→0,0038). RMSE se estanca en ~0,015 > |M2−1|=0,011. Sospecha: el sesgo se hereda de ν̂, el índice de cola de la innovación — o sea N07 reapareciendo   [verificación propia] w=.30
N25 ≡ [CASI: Merton 1980 + Chopra-Ziemba 1993. Solo vale si se convierte en DESIGUALDAD general] **Lo que se refuta rápido es lo que no decide.** Refutar un error del 20% en varianza: ~4 días. En drift: 37–800 años. Ratio 10⁴–10⁵. Y la cuota decisional (N18) va exactamente al revés   [C02·B1,B2,B3 ⊕] w=.55
N26 ≡ [FORMALIZADO C05·F2: la condición exacta es **T·T_max > T\*² = 3v²/(fω²)**; con σ² paseando al c/año da T\*=0,154/c, o sea 5,1–7,7 años, que reproduce el 5–10 medido] **INVERSIÓN κ=0**: si la volatilidad es no estacionaria (κ=0), E[v_H|v₀]=v₀ y no hay θ que estimar — la cuota observable es 1. Cuanto más no estacionaria la vol, MEJOR se pronostica su nivel medio y PEOR se comporta su cola. Las dos patologías apuntan en direcciones opuestas   [C02·orq] w=.88

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

N27 ≡ [REFORMULADO C04: NO es ley general. Con el DGP bien especificado el modelo complejo GANA a los tres horizontes. La complejidad solo penaliza si es INCORRECTA o SUPERFLUA] **COMPLEJIDAD ÓPTIMA DECRECIENTE EN H**: modelo óptimo por RMSE = GJR-t+EVT(8p) a 1 mes → GARCH-N(4p) a 1 año → GBM(2p) a 10 años. La sofisticación que gana a corto pierde a largo. MATIZ: a 10a todos fallan (RMSE mínimo 47%); GBM gana por ser el menos catastrófico, no por ser bueno   [C02·orq, verificado] w=.40
N28 ≡ [EXPLICADO C05: el EVT gasta su presupuesto de estimación en la FORMA DE LA COLA, que aporta el **0,14%** de la varianza del ES a 10 años. El 377% de RMSE es sofisticación asignada al 0,14% del problema. De anomalía pasa a corolario de N71] **LA COLA DEL ERROR**: la distribución de error de un modelo de cola hereda las colas gordas del fenómeno que modela. A 10a el modelo EVT tiene RMSE 377% con mediana 43,6% (razón 8,7); el GBM 47,0%/35,1% (razón 1,34). El coste de la sofisticación no se paga en error típico sino en frecuencia de error catastrófico — y nadie lo mide porque nadie reporta la distribución del error de su modelo, solo el número   [C02·orq, verificado] w=.88

N27 → N28            la monotonía y la curtosis del error son el mismo fenómeno visto dos veces
N28 → N07            EVT no ajustable a H largo, apareciendo de forma dinámica en vez de estática
N27 ⊣ N05            la escalera no colapsa a GBM, pero a H largo conviene usar GBM igualmente

N29 ≡ **EL RIVAL**: Pástor–Stambaugh 2012 (JF 67(2):431–478) es el mismo programa ya ejecutado — riesgo a largo plazo sin tratar los parámetros como conocidos, descompuesto en componentes epistémicos, con conclusión que invierte la sabiduría convencional. Ellos bayesianos sobre varianza predictiva; nosotros frecuentistas sobre medidas de cola. Tratar como rival, no como cita   [auditoría A01] w=.99
N30 ≡ **ENCARGO LE CAM**: para que N24 sea teorema y no observación hace falta una cota inferior minimax — dos puntos M2 = 1 ∓ cT^(−a) y demostrar que ninguna sucesión de tests los separa con probabilidad → 1. Una meseta de RMSE es una observación; una cota de Le Cam es un teorema   [auditoría A01] w=.95
N31 ≡ **ENCARGO ÍNDICE DE COLA**: para que N28 sea teorema hay que derivar el índice de cola de la distribución del error de ES ligándolo al error de estimación de la persistencia. El error de ES es ~exponencial en (error de persistencia × horizonte) ⇒ lognormalidad/cola de potencia de forma mecánica   [auditoría A01] w=.88
N32 ≡ **ENCARGO DESIGUALDAD**: N25 solo sobrevive como (información de Fisher sobre θᵢ)×(peso decisional de θᵢ) ≤ C, uniforme sobre una clase de modelos. Sin esa desigualdad es folclore con decimales   [auditoría A01] w=.85

N29 ⊣ (todo el programa)   hay que superarlo, no citarlo
N30 → N24 · N31 → N28 · N32 → N25

N33 ≡ [C04: existe un caso ESTRICTAMENTE MÁS FUERTE — ver N58, donde la cota no es verificable NUNCA] **MURO AUTOSELLADO**: SE(d̂) en frecuencias limpias ≈ (1−d)/√K con K = T/τ_reg = el propio n_eff. Resolver d a ±δ exige n_eff ≥ ((1−d)/δ)². Separar n_eff=5 de n_eff=20 exige n_eff≈400. **Una cota sobre la evidencia solo es verificable cuando ya ha sido superada**   [C03·D2] w=.90
N34 ≡ **PRECISIÓN SIN INFORMACIÓN**: subir el ancho de banda de m=n^0,5 a n^0,7 divide SE(d̂) por 2,7 (0,052→0,019) y lleva la exactitud de clasificación ENTRE CLASES a 0,48–0,51 (azar). Mismo patrón que N01 (in-fill) y N24 (22%): la precisión reportada y la información decisional divergen   [C03·D2] w=.88
N35 ≡ [CORREGIDO C04: la asignación era errónea. M2=1 NO es «filo dentro de un modelo correcto» sino Tipo II disfrazado — la clase es la ley de innovación y la fase es un funcional no continuo en Hellinger de esa ley. **El Tipo I puede no existir**] **DOS TIPOS DE NO IDENTIFICABILIDAD**. Tipo I (M2=1): filo de cuchillo dentro de un modelo correcto, sesgo que no encoge. Tipo II (d): identificable DENTRO de la clase, no ENTRE clases; más precisión empeora la decisión. El tipo II es peor   [C03·D2] w=.60
N36 ≡ **n_eff INDETERMINADO POR FACTOR 46**: cinco procesos con d̂∈[0,36;0,41] indistinguibles (AUC 0,52–0,65) tienen n_eff medido de 7,2 (ARFIMA d=0,40) a 331,4 (saltos de nivel). La magnitud que decide todo queda indeterminada 46× mientras el estimador que debería medirla parece idéntico   [C03·D2, medido] w=.88
N37 ≡ **EL UMBRAL TAMPOCO ESTÁ DEFINIDO**: d*=½[1−ln(T/H)/ln(T/τ)] vale 0,415 (τ=1d) a 0,325 (τ=6meses). Con d̂=0,40±0,05 la banda del estimador y la banda del umbral se solapan por completo. No solo el parámetro es indeterminado: la frontera también   [C03·D2] w=.90
N38 ≡ **PISOS DE LA TORRE** (cuarto añadido en C04: μ→precio, θ→varianza, d→log-periodograma, **T*→duración de régimen**, todos con la misma ley 1/√k sobre el nº de unidades independientes): d es la deriva del log-periodograma en log-frecuencia, y hereda la misma ley 1/√(nº de ciclos independientes de baja frecuencia). μ→precio, θ→varianza, d→log-periodograma. La recursión es la misma ley en los tres pisos — que es exactamente la invariancia de nivel que la auditoría exigía para que N16 fuese resultado   [C03·D2 ⊕ N16] w=.90

N33 ⊣ N22            la escapatoria no se puede certificar sin haberla ya superado
N34 ≡ N01 ≡ N24      tres instancias del mismo patrón: precisión ⊥ información
N37 ⊕ N36 ⇒ el parámetro Y la frontera son ambos indeterminados, y sus bandas se solapan
N38 → N16            la invariancia de nivel que la auditoría pedía

N39 ≡ **ORTOGONALIDAD UBICACIÓN/ANCHURA** (medido): la memoria larga degrada la UBICACIÓN agregada (n_eff 10→1,59) y deja la ANCHURA casi intacta (9,2→7,6 al pasar d de 0 a 0,4). Toda mejora de n_eff por agregación temporal es **inaccesible al estimando que fija ES y capital**. N22 y N03 operan en coordenadas ortogonales: nunca compitieron   [C03·D3, Davies–Harte 800 réplicas] w=.88
N40 ≡ **LA ESCAPATORIA ES ASINTÓTICAMENTE VACÍA**: G(T)=n_eff_loc/(T/H) decrece monótonamente (5,14 a T=10a → 1,42 a 50a → 0,81 a 100a → 0,13 a 1000a) y cruza 1 en T_cross=τ(H/τ)^(1/2d)=**71 años**. Solo gana donde n_eff≲6 en ambas contabilidades — el régimen en que nada es estimable. **Acumular datos la cierra**   [C03·D3] w=.90
N41 ≡ **CORRECCIÓN DIMENSIONAL DE N12**: T_eff=T^(1−2d) esconde un τ. Correctamente T_eff=τ·(T/τ)^(1−2d); con τ=1 día da **8,1 días**, no 2,5 años. Los «2,5 años» que arrastrábamos desde el ciclo 1 eran artefacto de fijar τ=1 año   [C03·D3] w=.85
N42 ≡ **RECONCILIACIÓN D2/D3** (adjudicación del orquestador): parecían contradecirse y dicen lo mismo desde dos sitios. DENTRO de modelos estacionarios d SÍ es estimable (SE=0,019, clasifica 84–97%) — y la escapatoria está cerrada igualmente por N40. ENTRE estacionarios y no estacionarios d̂ no distingue (n_eff medido de 7,2 a 331,4) — pero ahí el problema no es el umbral sino que **no existe ley invariante que estimar**. En los dos casos N22 muere, por razones distintas. Y el patrón N24 queda acotado: es específico de fronteras de momento, no universal   [C03·⊕ orq] w=.93
N43 ≡ **n_eff(L) = (T/L)^(1−2d), con L impuesto por el ESTIMANDO, no elegible.** Generalización correcta de N03. Para la media de bloques-H con d=0,4 da 1,59 < 10: la memoria larga DEGRADA el muro en vez de superarlo. N22 era el caso L=τ, lícito solo si el estimando es funcional de la marginal invariante — y el estimando que fija ES no lo es   [C03·D3] w=.88

N39 ⊣ N22            la escapatoria mejoraba la coordenada equivocada
N40 ⊣ N22            y se cierra sola al acumular datos
N43 → N03            generalización: el muro depende del estimando, y el estimando no se elige
N41 ⊣ N12            error dimensional arrastrado desde el ciclo 1
N42 ⊣ N24            el patrón de no identificabilidad NO es universal: es de fronteras de momento
N39 → N23            la partición ubicación/anchura, ahora medida

N44 ≡ **JERARQUÍA DE RANGO DE HERMITE**: n_eff^(m) = (T/H)^min(1, m(1−2d)), con umbrales d*_m = ½(1−1/m) = 0, ¼, ⅓, 3/8, … → ½. La memoria larga es peaje puro por encima de d*_m y gratis por debajo. El 0,3742 que creíamos umbral de escape es ≈3/8 = **el umbral de rango 4, o sea la condición de cuarto momento — N06 otra vez**, y con el sentido INVERTIDO: por debajo el muro satura en T/H, por encima empeora   [C03·D1] w=.50
N45 ≡ **«H≫τ» ES VACÍO, NO LEJANO**: agregar a cualquier escala deja el punto fijo ρ₁*=2^(2d)−1>0 para todo d>0 (verificado idéntico a 1d, 21d, 252d y 1260d; el AR(1) en cambio colapsa 0,953→0,045). **Ninguna escala vuelve iid la volatilidad.** Horizonte para CV(IV_H)=0,1: 8 años con d=0, 1.220 con d=0,26, **8·10⁸ con d=0,40**   [C03·D1] w=.92
N46 ≡ **LA ESCAPATORIA REAL ESTABA EN N17, NO EN N22**: bajo memoria larga ρ(H) ∝ H^(2d−1), no 1/(κH). corr(v₀, IV_10a) = 0,066 (OU τ=1mes) vs 0,112 (d=0,26) vs **0,397 (d=0,40)**. La cuota del estado presente no es el 2% sino el 20–40% con d realista. Es un cambio de constante, no de tasa   [C03·D1] w=.85
N47 ≡ **CONFLICTO DE d SIN RESOLVER**: el CV∝H^(−0,24) de N05 implica d=0,26 exactamente, pero ese d predice ES99(GJR)/ES99(GBM)=1,375 a 20a frente al 1,62 observado. Y el d=0,26 de un GJR simulado es memoria CORTA con τ enorme, no memoria larga genuina. Dos d incompatibles en el grafo: 0,40 (N12) y 0,26 (N05)   [C03·D1] w=.80

N22 ⊣ N22           autodestrucción: premisa y ganancia exigen regímenes opuestos de d
N22 ⊣ N05           N05 es la refutación empírica de la premisa de N22
N03 ← N02           derivación independiente, mismo número: n_eff ≤ T/H con igualdad solo en d=0
N44 → N06           el umbral de Hermite de rango 4 ES la condición de cuarto momento
N12 ⊥ N05           dos d incompatibles: 0,40 vs 0,26 → N47
N46 ⊣ N22           la escapatoria existía, pero en otro nodo

N48 ≡ [REETIQUETADO C05: los +50 puntos son **99,86% DERIVA**. No es «el coste de estimar», es «el coste de estimar μ». Predicho analíticamente 53,4% vs 53,0% medido] **EL COSTE DE ESTIMAR μ CRECE CON EL HORIZONTE** (medido sin contaminación, DGP sin saltos donde el modelo 3 ES la familia del generador): oráculo 3,1%/5,2%/6,6% a 1 mes/1 año/10 años — la especificación no es el problema. Coste de estimar = **+4,0 → +11,2 → +50,0 puntos**. Se multiplica por doce entre un mes y diez años   [orq, verificado] w=.94
N49 ≡ **AUTOCORRECCIÓN**: afirmé, respondiendo al auditor, que el DGP pertenecía a la familia del modelo 3 y por tanto su derrota sería puramente error de estimación. Era FALSO: el DGP tiene saltos y el modelo 3 no. Y a 10 años el error de estimación REDUJO el error del modelo 3 (65,5%→56,4%), lo contrario de mi mecanismo. El test que propuse para defender mi afirmación la refutó   [orq] w=1.0

N49 ⊣ N27           el mecanismo atribuido no está demostrado
N48 → N27           lo único que sí sostiene el test del oráculo

N50 ≡ **T1 — TEOREMA DE LA COLA DEL ERROR** (derivado por el orquestador, encargo N31): si ES ∝ (1−φ)^(−1/2) y φ̂ es asintóticamente normal con desviación s, el error relativo de ES tiene cola de potencia de **índice 2**, con C = φ_N(ρ)/(ρΦ_N(ρ)) y ρ=(1−φ)/s. El índice NO depende de s, H ni p: más datos bajan la constante, no la forma. Corolario: la varianza del estimador de ES está en la frontera de existencia   [orq, derivado+verificado] w=.55
N51 ≡ **MATIZ DE T1**: el índice asintótico es 2 siempre, pero el Hill sobre el 2% superior da 2,28 a ρ=2 y 41 a ρ=10 — la cola de potencia existe siempre y **solo es OBSERVABLE cuando ρ=O(1)**. Esa es la afirmación falsable, porque ρ es medible   [orq, verificado] w=.88
N52 ≡ **ρ = DISTANCIA A LA SINGULARIDAD** (conjetura unificadora): los tres resultados de no identificabilidad del grafo tienen la misma estructura — M2 a 1,2σ de 1 (N24), φ a 2,0σ de 1 (T1), d a 0,6σ de 3/8 (N44). **Los parámetros empíricamente relevantes de la volatilidad viven a uno o dos errores estándar de singularidades del funcional de riesgo, y esa proximidad convierte error normal de estimación en error de riesgo de ley de potencia**   [orq ⊕ C01,C02,C03] w=.70

N50 → N28           la derivación que el encargo N31 pedía
N51 ⊣ N50           el índice universal solo es observable cerca de la singularidad
N52 ⊕ N24 ⊕ N44 ⊕ N50   los tres comparten estructura: parámetro a O(1) errores estándar de una singularidad

N53 ≡ [**RETRACTADO**] Afirmé que ρ̂ está sesgado hacia la calma. FALSO: comparé contra φ=0,99 cuando el DGP tiene φ=α+γ/2+β=0,975. Con el valor correcto φ̂ está insesgado (error −0,4%, −0,5%, −0,0%) y ρ̂ sigue de cerca al ρ verdadero. Error factual del orquestador   [orq, RETRACTADO] w=.0

N53 ⊣ N53           retractado por el propio orquestador
N54 ≡ **T1 NO ESTÁ ACTIVO EN NUESTRO DGP**: con φ=0,975 y SE=0,0046 sale ρ≈5,4, donde la cola de potencia existe pero es inobservable (Hill α≈14, P(error>2×)≈0,01%). Luego **T1 no explica la razón RMSE/mediana de 8,7 del modelo EVT a 10 años**, que sigue sin explicación. El canal candidato que queda es la composición del error de ξ de la GPD sobre 2.520 pasos. Y «ρ≈2 en la práctica» es un SUPUESTO no medido: hace falta medir ρ sobre series reales   [orq] w=.85

N55 ≡ [**PUBLICADO** (Ma–Wei 2025 JEDC 177 lo asume como premisa) + **NON SEQUITUR MÍO**: medido α del proceso = 2,43 > 2, luego el ES SÍ tiene varianza finita] T2 — AUTOVIOLACIÓN (medido, 20 ajustes): el FHS+EVT produce ξ̂ en la cola de pérdidas con media **+0,372** y **95% de los ajustes por encima de 1/4**, es decir innovaciones SIN CUARTO MOMENTO. Cuarto momento muestral de la empalmada: mediana 117, p95 10.224, máx 57.708 (normal=3, t(7)=5), CV entre ajustes **3,32**. Al pasarlas por la recursión GARCH el proceso simulado tiene M2=∞>1 y su ES **no tiene varianza finita**. El modelo construido para no subestimar las colas se coloca por construcción del lado no identificable de la frontera N06   [orq, medido] w=.20
N56 ≡ **EL MECANISMO DE N28 ES MULTIPLICATIVO, NO ADITIVO**: sumar H variables de índice 1/ξ solo da factor e^(ξ lnH)≈18 a H=2520. Lo que explota es la realimentación GARCH: cada innovación grande entra al cuadrado en la recursión y eleva la varianza futura. Con E[z⁴]=∞ la condición M2<1 falla y la varianza del proceso simulado no converge   [orq] w=.20

N55 → N28           el mecanismo que el encargo N31 pedía, encontrado tras retractar T1
N55 → N06           el modelo EVT cae por construcción del lado M2>1
N55 ⊥ N50           T1 inactivo aquí (ρ≈5,4), T2 activo: son canales distintos

N57 ≡ **EL CRUCE**: a 10 años un modelo MAL especificado con parámetros CONOCIDOS (ORÁCULO-GBM, RMSE 24,0%) bate a uno BIEN especificado con parámetros ESTIMADOS (MODELO-3, RMSE 56,6%). A 1 mes ocurre lo contrario y por un factor de ocho (3,1% vs 26,3%). **Entre un año y diez años, saber los parámetros de un modelo malo pasa a valer más que tener el modelo bueno y estimarlo**   [orq, medido] w=.94

N57 → N48           el cruce es la consecuencia operativa de la amplificación
N57 ⊣ N27           y es lo que queda de N27 una vez quitado lo que no era cierto

N58 ≡ [ALCANCE CORREGIDO C05·F2: el regreso SÍ opera sobre la MAGNITUD (p95/p5 de τ̂ = 12,8× a 50a, 8,4× a 100a, **2,3× aún a 400 años**) pero las DECISIONES BINARIAS escapan (rama decidible al 92,5% con 50a). «Nunca verificable» era demasiado fuerte para el signo, correcto para la magnitud] REGRESO DE LA ESTACIONARIEDAD: certificar T* con precisión relativa ε exige observar k=1/ε² regímenes, o sea T ≥ T*/ε² (±20% ⇒ 25·T*; con T*=50a son 1.250 años), y ese presupuesto mayor exige otro 25× mayor. **La sucesión T_{k+1}=T_k/ε² no tiene punto fijo finito.** Estrictamente más fuerte que N33: allí la cota se vuelve verificable una vez superada; aquí **NUNCA es verificable**   [C04·E2] w=.55
N59 ≡ **FRONTERA DE FALSABILIDAD — H/p < T*/11,4**. Acopla N03 con el presupuesto de estacionariedad. Con T*=5a solo es falsable H≤1,1 días (p=1%) o 5,5 días (p=5%). Lo que exigiría cada norma vigente: **FRTB (ES 10d 97,5%) T*≥18,1a · Basilea II (VaR 10d 99%) 45,2a · Solvencia II (1a 99,5%) 2.280a · ECL vitalicia 10a 11.400a**. Solo el VaR diario sobrevive   [C04·E2] w=.75
N60 ≡ **T̂* NO ES IDENTIFICABLE**: segmentación binaria con valores críticos iid sobre una serie ESTACIONARIA d=0,40 **sin ninguna ruptura** da 3,97 rupturas en 50 años (T̂*=10,1a), indistinguible de un proceso con 4 rupturas reales (4,00 → 10,0a). Tasa de rechazo espurio 0,974. **El T* de la literatura empírica es la sombra del supuesto de memoria corta**   [C04·E2] w=.91
N61 ≡ [CORREGIDO C05·F2: 1,34/2,16 era la componente SISTEMÁTICA. El grado de libertad REALIZADO por trayectoria es **1,91× mediana / 3,36× p90 / 8,29× p99**. N61 subestimaba su propio hallazgo en 1,4× y 3,8×] **CUOTA DE VENTANA**: elegir T* (ventana 1–50a, misma trayectoria, mismo día) mueve el ES₉₉ un factor 1,34 (mediana), 1,73 (p90), **2,16 (p99)**. ~34% del capital regulatorio es un grado de libertad que ningún dato fija. Y el sesgo va al lado tranquilizador: solo el 21% de los saltos reales son visibles ⇒ **T̂*_medido = 4,8·T*_real**   [C04·E2] w=.75
N62 ≡ **PODER CON n_eff, NO CON n**: calibrando bajo la nula honesta (memoria larga sin ruptura), 50 años no detectan al 80% ningún cambio de volatilidad menor que **×1,55**. Δ₈₀ ∝ n^(−(1−2d)/2): 25a→×1,62, 100a→×1,49, 400a→×1,45. Llegar a ×1,10 exige **1,7·10⁶ años**. La literatura documenta el TAMAÑO distorsionado de estos tests; el PODER bajo la nula honesta no   [C04·E2] w=.88
N63 ≡ **CIRCULARIDAD NO RESUELTA** (grieta honesta de E2): la nula «honesta» supone d=0,40 constante, y **el propio d hereda el presupuesto de estacionariedad que se está denunciando**. Además T* no se midió sobre S&P real sino simulado (PDF de Stărică–Granger no extraíble, Stooq bloqueado). Debilidad real del ciclo 4   [C04·E2] w=.90

N58 ⊐ N33           estrictamente más fuerte: nunca verificable, no solo aún no verificable
N59 ⊕ N03 ⊕ N58     el acoplamiento: el muro dice cuántos datos hacen falta, el presupuesto cuántos hay
N60 ⊣ N60           el test que mediría T* rechaza el 97% de las veces sobre procesos sin rupturas
N61 → N10           si elegir la ventana mueve el capital un 34%, T* es endógeno y de política
N63 ⊣ N62           la nula honesta presupone lo que denuncia

N24a ≡ **DENTRO DEL MODELO, LA FRONTERA SÍ ES IDENTIFICABLE** — a tasa √T. I(θ) no singular en M2=1, ∇M2≠0, T·KL→1,88 (medido 1,74/1,90/1,93). a_crítico = **1/2**, s=√(∇M2'I⁻¹∇M2)=1,031. Error minimax sharp Φ(−δ√T/s): **34% a 10a, 12% a 80a, 5% a 158 años**. Mi enunciado «no identificable a ningún T» era FALSO   [C04·E1] w=.50
N24b ≡ **SOBRE LA LEY DE INNOVACIÓN, a=0**: para toda brecha fija D>0 existen dos leyes con M2=1∓D/2 cuyo error minimax es **≥0,246, invariante de 10 a 32.000 años**. La irregularidad **no está en θ, está en f**. Un argumento de dos puntos en θ nunca podía dar N24 — el encargo N30 pedía la forma equivocada   [C04·E1] w=.50
N64 ≡ [**TRIVIAL**: biyección bimedible + invariancia de f-divergencias + tensorización. Dos líneas de libro de texto. RETIRADO como aportación] AFINIDAD MULTIPLICATIVA: para todo modelo de escala condicional (GARCH, ARCH(∞), SV con vol observable), con el mismo θ y el mismo σ₁, la afinidad de Hellinger de T observaciones es **exactamente ρ(f₀,f₁)^T**, no asintóticamente. Convierte el módulo T-muestral en forma cerrada y permite calibrar ε=c/T sin asintótica   [C04·E1] w=.10
N65 ≡ **BAHADUR–SAVAGE PARA LA FASE GARCH**: el contaminante menos favorable vive en **|z| ∝ T^¼** (12,3σ a 10a → 20,5σ a 80a, verificado 8^¼=1,68). Capar |z|≤z_max restaura a=1, con cruce en z_max≈12σ a 10 años y ≈16σ a 80. **La decidibilidad se compra asumiendo exactamente la cola cuyo peso define la fase.** Instancia nueva de N33   [C04·E1] w=.83
N66 ≡ **BRECHA DE OCTAVA**: una condición de **cuarto** momento se sondea con un estadístico de **octavo** momento. κ̂=T⁻¹Σẑ⁴ suma términos de índice de cola ν/4∈(1,2) cuando 4<ν<8 ⇒ límite estable sesgado a la derecha, sesgo mediano ~T^−(1−4/ν). **Sesgo y SE decaen al MISMO orden ⇒ razón constante ⇒ la meseta de RMSE que medimos**. Verificado que NO es ν̂ (ν fijo da el mismo sesgo a 1e-4) y NO es Hall–Yao (ν≈7>4)   [C04·E1] w=.55
N67 ≡ **BORRAR TRES DÍAS**: eliminar los 3 mayores |ẑ| voltea la clasificación de fase en **18,3% / 15,0% / 15,8%** de las muestras a 10/40/80 años — **plano en T**. El mayor día carga el 11,5% de Σz⁴ a 10a. **A 10 años, borrar 3 días mueve M̂2 más que la distancia entera a la frontera.** El único estadístico verdaderamente plano del ciclo   [C04·E1] w=.55
N68 ≡ **SEGUNDA RUPTURA DE LA JERARQUÍA DE HERMITE**: el umbral de rango 2 (α+γ/2+β<1, estacionariedad) es **libre de innovación y robustamente decidible**; el de rango 4 (=N06=d*=3/8) es **dependiente de la innovación e indecidible**. La primera ruptura robusto/no-robusto de la jerarquía está exactamente en rango 4   [C04·E1] w=.50

N24a ⊣ N24          mi enunciado era falso: es identificable, tarda 158 años
N24b ⊐ N24a         y sobre la ley de innovación no lo es a ningún T
N66 → N24           el mecanismo real de la meseta que medí: ni ν̂ ni Hall-Yao
N65 → N33           misma estructura autosellada, instancia nueva
N67 ⊣ N24a          la identificabilidad de N24a se evapora si tres días pueden voltearla
N68 → N44 → N06     la jerarquía de Hermite se rompe exactamente donde está la frontera

N69 ≡ **LA FRONTERA M2=1 NO IMPORTA** (medido por el orquestador, ω y persistencia fijos, 60k trayectorias): cruzarla (curtosis 149 → ∞) mueve el ES99 un **1,002× a 1 mes, 1,030× a 1 año, 1,011× a 10 años**. El barrido completo, 1,12×. Razón: el ES99 es un cuantil al 1% y el cuarto momento gobierna la cola ≪1%. **Toda la línea M2 es técnicamente correcta y decisionalmente irrelevante.** Cuatro ciclos persiguiendo la frontera equivocada   [C04·orq, medido] w=.90
N70 ≡ **LA TABLA QUE REORIENTA**: efectos medidos sobre el ES en este mismo trabajo — frontera M2 **1,01×** · barrido M2 1,12× · elegir ventana T* **1,34× / 2,16×** · oráculo vs estimado a 10a **24,0%→56,6%** · coste de estimar 1mes→10a **+4→+50 pts** · modelo EVT a 10a **+175% sesgo, 377% RMSE**. La frontera de fase es el efecto MÁS PEQUEÑO, por un orden de magnitud. Lo que mueve la decisión es el error de estimación y su amplificación con el horizonte   [C04·orq] w=.92

N69 ⊣ N06 ⊣ N24a ⊣ N24b ⊣ N44 ⊣ N66 ⊣ N67 ⊣ N68     toda la línea M2 degradada en bloque
N70 → N48 → N57 → N61 → N28                          hacia donde van los ciclos 5-10

N71 ≡ **EL INVARIANTE H·f = k²/2 = 3,55 OBSERVACIONES**: var(ÊS_H) = H²σ²/T + H·k²σ²/(2fT) con k=φ(z_α)/(1−α). Los dos términos —deriva y cola— se igualan en **3,55 observaciones** (2,73 a α=97,5%), **cancelándose T, σ y la unidad de muestreo**. Cuota de la deriva: 22,0% a 1 día, 85,5% a 1 mes, 98,6% a 1 año, **99,86% a 10 años**. Consecuencia perversa: **muestrear más rápido ADELANTA el cruce** (a 5 minutos, 3,55 barras = **17,8 minutos**; la cifra de «1,6 horas» del informe original era errónea por factor 5,4) — más datos hacen el problema más puramente de media, nunca menos. Predice N48 analíticamente: 53,4% vs 53,0% medido   [C05·F3] w=.85
N72 ≡ **NUNCA VÁLIDA Y ÚTIL A LA VEZ**: la región falsable de N59 (H≤1,1 días) está **contenida** en la región dominada por la cola de N71 (H·f≤3,55 obs). Donde el ES es falsable lo domina el sesgo de especificación (|sesgo|/SD = 21,6 a 1 semana, 18,3 a 1 mes); donde está limpio de sesgo (1,59 a 1 año, 0,12 a 10 años) ya es puramente N01. **Falsabilidad y especificidad-de-cola se apagan juntas**   [C05·F3] w=.86
N73 ≡ [**EL NÚCLEO** — único eje ausente de toda la literatura confrontada. CORRECCIÓN: los «400 años» suponían σ=10%; con σ=16% son **983 años**] **√t ES EXACTAMENTE μ=0, Y μ NO ES ESTIMABLE**: √(H/Δ)·ES₁d = ES_H(μ=0) con ratio medido **0,9941**. Declarar μ∈[0,8%] mueve el ES₉₉ a 10 años **1,903×**; √t frente a μ=5%, **1,413×**. Con T=10a, IC95(μ̂)=[−7,4%,+17,4%] ⇒ **ES₉₉ a 10 años ∈[−0,05, 2,43]: ni el signo está determinado**. Fijar μ a ±1%/año exige 400 años a cualquier frecuencia. *El número regulatorio es una apuesta declarada sobre la prima de riesgo disfrazada de medida de cola*   [C05·F3] w=.80
N74 ≡ **CAPITAL LIBRE DE DATO — VERIFICADO**: las dos cuotas SON ortogonales (rango total 3,39× vs producto de medios 3,28×, 3% de discrepancia). **A 1 año, un factor de 3,4 en el capital regulatorio no está fijado por ningún dato**, solo por dos convenciones no declaradas: la ventana de estimación (2,13–2,79×) y la deriva declarada (1,21–1,59×). **A 10 años ni el signo está determinado**: el ES99 va de −0,120 (μ=8%, ventana 2a) a +1,444 (μ=0%, ventana 50a) — de esperar una GANANCIA en el 1% peor a perder el 76% del valor, con los mismos datos. Comparar con la frontera M2: 1,011×   [C05·F3 ⊕ orq] w=.93
N75 ≡ **ENTREGABLE SUSTITUTIVO**: en vez del ES a horizonte regulatorio, la terna — (i) **ES a 1 día estimado y backtesteado** (relSD 1,6%, único régimen falsable por N59); (ii) **μ o el multiplicador DECLARADOS como convención publicada, no estimados**, con la prueba de que no admiten estimador; (iii) **el choque de ruptura s\*=K/exposición y el recuento histórico de excedencias**. s\* es un hecho contable presente y el recuento un hecho pasado: **ambos verificables por un tercero**   [C05·F3] w=.72

N71 → N48           el mecanismo analítico de los +50 puntos: 99,86% deriva
N71 → N28           el 377% de RMSE del EVT es sofisticación asignada al 0,14% del problema
N71 ⊐ N59 ⇒ N72     la región falsable está contenida en la dominada por la cola
N73 ⊣ (todo el ES)  el número a horizonte regulatorio es una declaración sobre μ
N74 ⊕ N61 ⊕ N73     el producto, si son ortogonales
N75 → N59           mueve la fracción falsable del componente estimado de ~0% a 100%

N76 ≡ **KESTEN, MEDIDO**: índice de cola de la innovación empalmada = **3,40**; del proceso GARCH simulado con ella = **2,43**. La recursión engorda la cola sustancialmente pero **no la cruza por debajo de 2**. Luego el ES SÍ tiene varianza finita y la consecuencia que atribuí a T2 era un non sequitur, como señaló la auditoría   [orq, medido] w=.88
N77 ≡ **EL POLO DE LA GPD**: ES ∝ 1/(1−ξ), luego un ξ̂ normal da un ES con polo en ξ̂=1 e índice de cola **1** (la MEDIA del estimador no existe) — verificado. Pero la constante es a·φ(a) con a=(1−ξ)/SE(ξ̂), y **a los parámetros reales a=7,24 y P(ξ̂≥1)=2·10⁻¹³: inactivo**. Se activa solo con ξ≈0,7–0,85 y pocas excedencias   [orq, derivado+verificado] w=.85
N78 ≡ **TRES MECANISMOS, TRES FALLOS**: para explicar la razón RMSE/mediana=8,7 propuse el polo en φ (correcto, inactivo, ρ≈5,4), el cuarto momento infinito (non sequitur, α=2,43>2) y el polo en ξ (correcto, inactivo, a=7,24). **La medición se sostiene; la explicación no.** Registrado como problema abierto   [orq] w=.95
N79 ≡ **EL RIVAL QUE IMPORTA — Danielsson (2002), «The emperor has no clothes: Limits to risk modelling», JBF 26(7):1273–1296.** La tesis entera de esta investigación, publicada hace 24 años: modelos no robustos, propiedades que cambian al ser observadas, el análisis en calma no informa sobre la crisis. **Todo lo que sobrevive son casos particulares cuantificados de ese artículo.** Si el entregable no lo confronta en el primer párrafo, no vale   [auditoría A02] w=.97
N80 ≡ **LA REFORMULACIÓN**: si la tesis cualitativa es de 2002, la aportación posible es **la cuantificación**. Y hay una sola cifra medida, ortogonal y ausente de Danielsson: **N74** — factor 3,4× en el capital a 1 año y signo indeterminado a 10. Los ciclos 6-10 la vuelven irrefutable; todo lo demás pasa a contexto   [orq] w=.70

N76 ⊣ N55 · N77 ⊣ N28 · N78 ⊣ (los tres mecanismos) · N79 ⊐ (todo el programa) · N80 → N74

N81 ≡ [**ROTA BAJO NO ESTACIONARIEDAD**: cobertura medida 35% a 1a y 43,3% a 10a de un 90% nominal. Solo vale bajo estacionariedad y especificación correcta — y saber si eso se cumple es justo lo que N60 dice que no se puede saber. DOMINIO H≥1 AÑO: el bolsillo predice 0,025 vs 0,054 a 1 mes, error 2,2×] **COTA INFERIOR COMPUTABLE Y ALCANZADA**: RMSE_rel(ÊS_{H,q}) ≥ √[(s_μ/c_q)²(H/n) + (λ_H/2)²g'Σ̂g + (∂log c_q/∂ν)²SE(ν̂)²], con λ_H=σ̄²(H−A_H)/V_H. Vale 5,4%/12,4%/**30,8%** a 1m/1a/10a con T=10a, **y se alcanza**: 800 ajustes MLE dan 5,5%/12,0%/32,6%, ratio 1,01/0,97/**1,06**. La literatura de método delta nunca la evalúa a horizonte multianual. **Bolsillo: RMSE_rel ≥ 0,27·√(H/T)** para H>1,1 años, evaluable con la salida de cualquier paquete GARCH sin simular   [C05·F1] w=.45
N82 ≡ **TOPE DE SATURACIÓN DEL CANAL VOLATILIDAD**: la amplificación con el horizonte del error vía (ω,α,γ,β) está acotada por **(1−β)/(1−π)**; medido 4,50 vs 4,51 analítico. **La persistencia no puede explicar un crecimiento de 12,5×**. Los exponentes: a_μ=1,000 exacto para todo H (no satura), a_vol sube a 0,91 en H≈50d y cae a 0,508, a_ν=0,500 exacto   [C05·F1] w=.86
N83 ≡ **CRUCE H\* = 1,1 AÑOS, INVARIANTE EN T**: H\*=(c_q·ς/2s_μ)²=276 días. Más allá de un año, **más datos no cambian QUÉ domina el error, solo su nivel**. A 10 años la deriva aporta 26,9 de los 30,8 puntos de la cota (76%); el canal volatilidad, 9,0   [C05·F1] w=.84
N84 ≡ [SOLO EL p90 ES ROBUSTO: p95/p99 analíticos exceden los medidos 6–13%, la cola del error es más DELGADA que lognormal] **MULTIPLICADOR DE CAPITAL POR ERROR DE ESTIMACIÓN** (medido, 800 réplicas): fijar capital en el p90 del error en vez del punto estimado multiplica por **1,45× a 10 años** (p95 1,57×, p99 1,79×), frente a 1,073× a 1 mes. Predecible antes de simular: exp(1,282·B)=1,48× vs 1,447× medido. Regulatorio con T=10a: FRTB 10d → 1,02× · Solvencia II 1a → 1,17× · **ECL vitalicia 10a → 1,45×** · con 5a de datos **1,63×** · con 3a **1,89×**. **La frontera M2 movía 1,011×; esto mueve cuarenta veces más**   [C05·F1] w=.92

N81 → N48          explica el 62% de los +50 puntos a 10 años; el resto es polo + especificación
N82 ⊣ (mi sospecha) la persistencia NO domina: satura. La deriva no
N83 → N01          más allá de 1,1 años el error del ES es un problema de deriva, punto
N84 ⊥ N74          dos cuotas distintas: 1,45× por ERROR DE ESTIMACIÓN, 3,4× por CONVENCIÓN

N85 ≡ **BIFURCACIÓN DE LA VENTANA ÓPTIMA**: T\*(H) **no es continuo**. La prima de recencia 2C(T,H)→2Γ/H decae con el horizonte mientras el coste de ser corto no depende de H; al cruzarse, el mínimo global **salta** de la rama corta a «toda la muestra». Locus **H_c = 1,4·τ** (medido 1,20–1,58 para τ∈[0,5;32]a), **factor de salto 57–459×**. Es una transición de primer orden en el argmin. A H=1a la rama la decide τ≷0,71a: **un error de 1,33× en τ invierte la respuesta**   [C05·F2] w=.86
N86 ≡ **CONDICIÓN EXACTA «MÁS DATOS PERJUDICAN»**: L(T_max)>L(T) ⟺ **T·T_max > T\*² = 3v²/(fω²)**. Con T=T\*, todo exceso de muestra es estrictamente dañino y el daño crece sin cota (ω²T_max/3). Con σ² paseando al c=0,02–0,03/año, T\*=5,1–7,7 años — reproduce el «5–10 de 100 disponibles» que N26 había medido   [C05·F2] w=.92
N87 ≡ [**RECUPERADO C06**: el 1,27× se midió en régimen estacionario. En el régimen no estacionario que no se puede descartar, la escalera reduce el déficit p95 de 1,595 a 0,420 — **factor 3,8×** — por un 32% más de capital. Supera holgadamente el umbral] **EL ALGORITMO: ESCALERA FIJA + SEGUNDO MAYOR**. Escalera obligatoria {1,2,5,10,20,muestra completa} con regla «segundo mayor» **domina estrictamente** a la muestra completa: capital **0,943×** (5,7% más barato) **y** déficit p95 **1,539×** vs 1,957× (21% más seguro). Frente a la práctica vigente mueve el capital **1,36×** y reduce el déficit p95 de 2,761× a 1,539×. **Lo esencial no es el rango sino mover la PROPIEDAD del grado de libertad**: escalera fija por el regulador, regla global, y publicación de S=ES_max/ES_min **antes** del número de capital   [C05·F2] w=.85
N88 ≡ [CORREGIDO C06: NO es de la ventana, es **del horizonte**. A 1 año no existe (1,032/1,019); a 10 años los procedimientos convencionales dan 0,945/0,892 e infraestiman el 50–63% de las veces] **EL SESGO BAJISTA**: toda ventana ≤30 años **infraestima** el ES99 prospectivo verdadero (0,75–0,93×). El grado de libertad se apila sobre un sesgo bajista común, y acotar el primero **no corrige el segundo**   [C05·F2] w=.60
N89 ≡ **EL EJE VENTANA ES SUBDOMINANTE**: el «risk ratio» de Danielsson–James–Valenzuela–Zer (máx/mín entre modelos: media ≈4, hasta 55 en crisis) es **mayor** que el nuestro entre ventanas (mediana 2,28×). La elección de modelo domina a la elección de ventana. Y S mide la ANCHURA, no el error: entre terciles de S el error mediano solo pasa de 0,263 a 0,296 — **es una declaración, no un diagnóstico**   [C05·F2] w=.88

N85 → N87           la bifurcación es por qué una escalera fija domina a cualquier óptimo estimado
N86 → N26           la formalización exacta de «más datos perjudican»
N88 ⊣ N87           acotar el grado de libertad no corrige el sesgo bajista común
N89 ⊣ N61 ⊣ N74     el eje ventana es real pero subdominante frente al eje modelo

N91 ≡ **AUSENCIA VERIFICADA DE LA MEDIA**: cero ocurrencias de «mean / expected return / drift» en el texto **íntegro** de Danielsson 2002 (30 pp.) y de Danielsson–James–Valenzuela–Zer 2016 (34 pp.). **Toda la literatura de riesgo de modelo cuantifica dispersión de cola con μ≡0 por convención, y nunca lo menciona.** Verificado por extracción, no de segunda mano   [C06·G2] w=.93
N92 ≡ **LA MÉTRICA RIVAL SE ROMPE**: el risk ratio máx/mín de DJVZ 2016 es **indefinido cuando el mínimo cruza cero**, que es exactamente lo que ocurre a H=10 años (ES₉₉ ∈ [−0,44, +1,54]). El aporte no es un número mayor que el suyo: **es una región donde su número no existe**. Comparable honesto del S&P-500 en muestra completa: 1,71–1,82×, no 55,32 (ese es el máximo diario de una acción en 1987)   [C06·G2] w=.88
N93 ≡ **LA CONVENCIÓN VALIDADA FUERA DE DOMINIO**: μ=0 sesga el ES₉₉ **+3,9% a 10 días** (correcto donde Basilea la validó) **y +145,9% a 10 años** (falso donde IFRS-9 y Solvencia II la heredan por inercia). Escala √H. **Es el mecanismo de transmisión entre la literatura corta y el fallo largo**   [C06·G2] w=.85
N94 ≡ **DESACUERDO MEDIDO CON UNA RECOMENDACIÓN PUBLICADA**: Danielsson 2002 §3.4 concluye que «longer estimation horizons are preferred»; N86/N87 miden lo contrario. Un desacuerdo medido con una recomendación en JBF vale más que cien glosas   [C06·G2] w=.92
N95 ≡ **EL NODO CON MÁS VALOR, Y NO ES N74**: N57 invierte la conclusión de Kerkhof–Melenberg–Schumacher 2010 (el riesgo de especificación domina al de estimación) y **localiza la inversión en H**. El ciclo 7 debe ir a por el punto de cruce exacto, no a por N74   [C06·G2] w=.90

N91 → N73          la ausencia verificada es lo que convierte N73 en el núcleo
N92 ⊣ N29          la métrica del rival no existe donde nosotros medimos
N93 → N73          el mecanismo de transmisión: correcta a 10 días, falsa a 10 años
N94 ⊣ N03          desacuerdo con el mismo texto que nos quitó N03
N95 ⊣ N80          la aportación es el par N73+N57, no N74

N96 ≡ [**RETRACTADO C07**: el cruce está literal en Dowd–Blake–Cairns 2004 §2; y enchufar el IC de μ̂ NO es propagar incertidumbre — el tratamiento coherente (varianza predictiva de Pástor–Stambaugh) da ES>0 a TODO horizonte cuando Ŝ√T<k. **Declaraba indeterminado lo que el tratamiento correcto determina**] T3 — HORIZONTE DE DETERMINACIÓN: el ES cruza cero en μ*=k_α·σ/√H, y su signo está indeterminado cuando μ* cae en el IC de μ̂. Dividiendo por σ **la volatilidad desaparece**: |Ŝ − k_α/√H| < z/√T, de donde **H\* = [k_α/(Ŝ + z/√T)]²**. Verificado: con Ŝ=0,375 y T=10a, P(ES<0) pasa de 0,5% a H=5 a **2,5% justo en H\*=7,18** y 24,4% a H=20. Con Ŝ=0,375 y 10 años de datos **el signo del ES₉₉ está determinado solo hasta 7,2 años**; con 100 años, hasta 21,8. IFRS-9 (10–30a) y pensiones (20–40a) quedan fuera   [C06·orq] w=.55
N97 ≡ **LA CUOTA EPISTÉMICA DEL HORIZONTE**: con datos infinitos H\*_∞=(k_α/Ŝ)² — eso no es ignorancia sino un hecho sobre el activo. La razón **H\*(T)/H\*_∞ = [Ŝ/(Ŝ+z/√T)]²** es la fracción que sobrevive. Con Ŝ=0,375 y T=10a vale 0,142: **la ignorancia sobre μ quita el 85,8% del rango de horizontes en que el signo estaría determinado si μ se conociera**   [C06·orq] w=.60
N98 ≡ **DECLARAR μ CONVIERTE VARIANZA EN SESGO** (medido): a 10 años la desviación del ES pasa de 0,5063 (μ estimado) a 0,0190 (μ declarado), factor **26,7×** — pero aparece un sesgo (μ_dec−μ_real)·H = 0,40 si el convenio yerra 4 puntos. **El error total no baja: cambia de ruido invisible a sesgo declarado.** Y el rango de tres convenios cubre solo el 53,5% de lo que habría salido estimando: declarar tres valores SUBESTIMA la incertidumbre salvo que el rango se elija para cubrir el IC   [C06·orq, medido] w=.88

N96 ← N73 ← N91     el criterio estaba escondido detrás de la convención μ≡0 que nadie declara
N96 ← N71           sale de la descomposición H²σ²/T + Hk²σ²/(2fT): el primer término es el 99,86% a 10a
N97 ⊂ N96           separa la indeterminación epistémica del hecho real sobre el activo
N98 → N87           la justificación correcta del algoritmo no es «reduce el error» sino «lo hace auditable»

N99 ≡ **LA COTA SE ROMPE FUERA DE SU DOMINIO, Y EL DOMINIO NO ES VERIFICABLE**: la cota de bolsillo 0,27·√(H/T), verificada en el ciclo 5 con ratio 1,01–1,06 bajo estacionariedad, **cubre el 35,0% a 1 año y el 43,3% a 10 años de un 90% nominal** cuando el nivel de volatilidad está a la deriva. Y saber si lo está es precisamente lo que N60 demuestra que no se puede saber. **Una cota cuyo dominio de validez no es verificable no es utilizable, y una que no cubre es peor que no reportar nada**   [C06·orq, medido] w=.90
N100 ≡ **EL SESGO BAJISTA ES DEL HORIZONTE, NO DE LA VENTANA**: a 1 año no existe (ratios 1,032 y 1,019); a 10 años los procedimientos convencionales dan **0,945 y 0,892** e infraestiman el **50,0% y 63,3%** de las veces. Mecanismo T3: a horizonte largo el término −μH domina y el ruido de μ̂ entra RESTANDO, así que el ES sale sistemáticamente pequeño; crece como H mientras la cola crece como √H. **Acotar la dispersión de la ventana no corrige nada**   [C06·orq, medido] w=.88
N101 ≡ **EL ALGORITMO, MEDIDO EN RÉGIMEN NO ESTACIONARIO**: escalera+2º mayor reduce el déficit p95 de 1,595 a 0,420 (**3,8×**) por 32% más capital. El algoritmo completo (escalera + μ declarado cubriendo el IC95) lleva el déficit a **0,000** con P(infraestimar)=3,3% frente al 50–63% de lo vigente, **pero cuesta 48% más capital** a 10 años. El rango declarado cubre el ES verdadero el 90,0% a 10 años (nominal 95%)   [C06·orq, medido] w=.86

N99 ⊣ N81           la pieza constructiva del ciclo 5, rota fuera de su dominio
N99 ← N60           y el dominio es justo lo indecidible: el círculo se cierra
N100 ⊣ N88          el ataque acierta en la conclusión y se equivoca en la causa
N100 ← N96          el mecanismo es T3: −μH domina y el ruido entra restando
N101 → N87          el algoritmo funciona; el coste es 48% de capital, no es gratis

N105 ≡ **T4 — LA MUESTRA DECIDE, NO EL HORIZONTE**: con la varianza predictiva σ²H(1+H/T), sup_H[Ŝ√H/√(1+H/T)] = Ŝ√T, luego **el ES₉₉ es estrictamente positivo a TODO horizonte mientras T < (k_α/Ŝ)² = 50,5 años**. Verificado: el Sharpe ajustado satura en 1,186 y nunca alcanza k=2,665 por mucho que se alargue H. **Dualidad exacta**: el horizonte de cruce con μ conocido ES la muestra mínima para que el cruce exista. Invierte la lectura de T3   [C07·H1, verificado] w=.85
N106 ≡ **LA REPARACIÓN MUEVE MÁS QUE EL RESULTADO REFUTADO**: sustituir el ES enchufado por el predictivo multiplica el capital **1,746× (H=10,T=10), 2,319× (T=5), 2,949× (T=3), 12,2× (H=40,T=10)**; a 1 año solo 1,057×, subumbral y coherente con N100. Mayor que el 1,45× de N84 y lo contiene. **La maquinaria es de Pástor–Stambaugh 2012; lo nuestro es medirla sobre el ES**   [C07·H1, medido] w=.85
N107 ≡ **DOS RIVALES NO CONFRONTADOS**: **Dowd–Blake–Cairns 2004** (J. Risk Finance 5(2):52–57) tiene el cruce, el pico, la sensibilidad creciente a μ y hasta la recomendación de declararlo; y **Welch, SSRN 5709087 (nov-2025)** tiene el mismo rango de horizontes y el mismo mensaje: «the central concern is not the sampling of draws but the uncertainty about the distribution». Si el entregable no los cita, repite el error   [C07·H1] w=.90
N108 ≡ **H\* HEREDA EL SUPUESTO iid**: con n_eff=(T/L)^(1−2d) de N43, H\* cae de 7,18 a 3,86 (d=0,20), 3,15 (d=0,26) y **1,90 años (d=0,40)**. Con el d que el propio ciclo 3 midió, ni Solvencia II queda holgadamente dentro. **El mapa regulatorio de T3 no sobrevivía a su propio grafo**   [C07·H1] w=.85

N105 ⊐ N96          lo que sobrevive es más simple y más fuerte que lo que cae
N106 ⊐ N84          contiene el multiplicador anterior y lo supera
N107 ⊣ N96          el cruce estaba publicado en 2004
N108 ⊣ N96          y el mapa regulatorio no aguantaba nuestro propio d
N91 → N105          el único eje intacto sigue siendo la ausencia de la media
