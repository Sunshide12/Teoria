# GRAFO — conexiones neuronales de la investigación

Formato en `FORMATO.md`. IDs estables: cítalos por ID, no reexpliques el concepto.

## Nodos

N01 ≡ El drift es inestimable in-fill: I(μ)=T/σ² no depende de la frecuencia. Girsanov — cambiar μ da medidas equivalentes, cambiar σ las da singulares. SE(μ̂)=σ/√T es un suelo, no una elección   [C01·A2] w=.96
N02 ≡ Invariante adimensional R(H)=√(H/T_eff)=epistémico/aleatorio. Sin σ ni μ dentro. H*=T_eff es donde R=1 y el error de estimar supera a la aleatoriedad   [C01·A1,A2 ⊕] w=.93
N03 ≡ n_eff=T/H (no T·252) gobierna TODA falsabilidad. T_req≈11,4·H/p para poder 80%. VERIFICADO: n=1070 medido vs 1140 predicho   [C01·A1,A2,A3 ⊕] w=.96
N04 ≡ El MC reporta el error de integración (1/√N, elegido) y oculta el de inferencia (√(H/T), heredado). Subreporte ≈√(N·H/T), CRECIENTE en N   [C01·A2,A3 ⊕] w=.93
N05 ≡ La escalera NO colapsa a GBM en ningún horizonte humano. CV de varianza integrada decae H^−0,24 y no H^−0,5; ES99(GJR)/ES99(GBM)=1,77 a 1a y 1,62 a 20a   [C01·A1] w=.82
N06 ≡ Frontera de fase M2=E[(α+γ1{ε<0}+β)²]=1 empíricamente NO identificable: las acciones caen en M2≈1,0085±0,02 y la curtosis muestral (3,6→5,5) no distingue una poblacional de 13,5 de una infinita   [C01·A1 +verif] w=.90
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
N18 ≡ **CUOTA DECISIONAL INVARIANTE**: la parte del problema de decisión accesible a un funcional drift-invariante es de unidades porcentuales. Vol constante Φ=2S²/m (0,13% diario); Heston Φ_∞=S²η²/(2κ²θ+S²η²)≈2%; techo universal **1/4** (solo si ⟨σ²⟩⟨σ⁻²⟩=2). Los tres agentes   [C02·B1,B2,B3 ⊕] w=.94
N19 ≡ [PUBLICADO: Rockafellar-Uryasev-Zabarankin 2006 — NO es hallazgo nuestro] **MONETARIEDAD ⊥ INVARIANCIA**: toda medida de riesgo aditiva en efectivo es Girsanov-equivariante (se desplaza en ∫θσds). La frontera Artzner(coherente)/Rockafellar(desviación) ES la frontera de Girsanov. Margen y vol-target son drift-libres por necesidad matemática; ES y capital económico no pueden serlo jamás   [C02·B3] w=.25
N20 ≡ **COLAPSO DE VILLE POR SATURACIÓN**: si el nulo está saturado por equivalencia, todo e-proceso cumple ess-sup E_τ≤1 → error tipo I exactamente 0 y escala de evidencia vacía. Deja de ser test y pasa a certificado cuasi-seguro. Corolario: todo funcional invariante a cambio equivalente con Fatou colapsa al ess-sup   [C02·B3, corrobora B2(iii), REFUTA B1-C4] w=.87
N21 ≡ **ANIQUILACIÓN CLARK–OCONE**: si Ψ(P)=E_P[φ] es invariante bajo TODA Q~P, entonces E[D_tφ|F_t]=0 y φ es c.s. constante. (b-fuerte) no admite funcional no trivial, y (b-débil)="depende solo de la ley de ⟨M⟩_H" NO es equivalente: presupone la escisión, o sea ya es paramétrica   [C02·B2] w=.83
N22 ≡ [REFUTADO C03·D1] **CANCELACIÓN ERGÓDICA**: promediar dentro del horizonte es una transformación GAUGE. Mejora θ̂ por H/τ y concentra IV_H por el mismo H/τ. Control exacto OU con H/τ=504: n_eff=4,992, no 2.520. El «umbral d≈0,37» era artefacto de unidades — τ se cancela. Lo que era: si H≫τ_vol, Ψ deja de ser funcional de la ley TERMINAL y pasa a serlo de la ley INVARIANTE, con n_eff=(T/τ)^(1−2d) en vez de T/H. Con d=0,26, T=50a, τ=1mes: n_eff pasa de 5 a 21,6. **UMBRAL: la puerta se cierra si d > ≈0,37**, y el d≈0,4 de N12 la deja cerrada — pero dentro del error de estimación   [C02·B3] w=.15
N23 ≡ **PARTICIÓN DEL EJE P**: la grieta P no era desacuerdo sino dos preguntas confundidas. Libre de modelo acierta en la ANCHURA (desviación, margen); paramétrico es imprescindible para la UBICACIÓN (capital, ES)   [C02·⊕] w=.90
N24 ≡ [FLANCO: Hall-Yao 2003 — el sesgo plano podría ser su no-regularidad. Reconciliar ANTES de reclamar] La frontera M2=1 **no es identificable a ningún T**: el sesgo del MLE no encoge (−0,018 a 10a, −0,015 a 80a) mientras el SE sí (0,0124→0,0038). RMSE se estanca en ~0,015 > |M2−1|=0,011. Sospecha: el sesgo se hereda de ν̂, el índice de cola de la innovación — o sea N07 reapareciendo   [verificación propia] w=.70
N25 ≡ [CASI: Merton 1980 + Chopra-Ziemba 1993. Solo vale si se convierte en DESIGUALDAD general] **Lo que se refuta rápido es lo que no decide.** Refutar un error del 20% en varianza: ~4 días. En drift: 37–800 años. Ratio 10⁴–10⁵. Y la cuota decisional (N18) va exactamente al revés   [C02·B1,B2,B3 ⊕] w=.55
N26 ≡ **INVERSIÓN κ=0**: si la volatilidad es no estacionaria (κ=0), E[v_H|v₀]=v₀ y no hay θ que estimar — la cuota observable es 1. Cuanto más no estacionaria la vol, MEJOR se pronostica su nivel medio y PEOR se comporta su cola. Las dos patologías apuntan en direcciones opuestas   [C02·orq] w=.72

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

N33 ≡ [C04: existe un caso ESTRICTAMENTE MÁS FUERTE — ver N58, donde la cota no es verificable NUNCA] **MURO AUTOSELLADO**: SE(d̂) en frecuencias limpias ≈ (1−d)/√K con K = T/τ_reg = el propio n_eff. Resolver d a ±δ exige n_eff ≥ ((1−d)/δ)². Separar n_eff=5 de n_eff=20 exige n_eff≈400. **Una cota sobre la evidencia solo es verificable cuando ya ha sido superada**   [C03·D2] w=.90
N34 ≡ **PRECISIÓN SIN INFORMACIÓN**: subir el ancho de banda de m=n^0,5 a n^0,7 divide SE(d̂) por 2,7 (0,052→0,019) y lleva la exactitud de clasificación ENTRE CLASES a 0,48–0,51 (azar). Mismo patrón que N01 (in-fill) y N24 (22%): la precisión reportada y la información decisional divergen   [C03·D2] w=.88
N35 ≡ **DOS TIPOS DE NO IDENTIFICABILIDAD**. Tipo I (M2=1): filo de cuchillo dentro de un modelo correcto, sesgo que no encoge. Tipo II (d): identificable DENTRO de la clase, no ENTRE clases; más precisión empeora la decisión. El tipo II es peor   [C03·D2] w=.85
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

N44 ≡ **JERARQUÍA DE RANGO DE HERMITE**: n_eff^(m) = (T/H)^min(1, m(1−2d)), con umbrales d*_m = ½(1−1/m) = 0, ¼, ⅓, 3/8, … → ½. La memoria larga es peaje puro por encima de d*_m y gratis por debajo. El 0,3742 que creíamos umbral de escape es ≈3/8 = **el umbral de rango 4, o sea la condición de cuarto momento — N06 otra vez**, y con el sentido INVERTIDO: por debajo el muro satura en T/H, por encima empeora   [C03·D1] w=.88
N45 ≡ **«H≫τ» ES VACÍO, NO LEJANO**: agregar a cualquier escala deja el punto fijo ρ₁*=2^(2d)−1>0 para todo d>0 (verificado idéntico a 1d, 21d, 252d y 1260d; el AR(1) en cambio colapsa 0,953→0,045). **Ninguna escala vuelve iid la volatilidad.** Horizonte para CV(IV_H)=0,1: 8 años con d=0, 1.220 con d=0,26, **8·10⁸ con d=0,40**   [C03·D1] w=.92
N46 ≡ **LA ESCAPATORIA REAL ESTABA EN N17, NO EN N22**: bajo memoria larga ρ(H) ∝ H^(2d−1), no 1/(κH). corr(v₀, IV_10a) = 0,066 (OU τ=1mes) vs 0,112 (d=0,26) vs **0,397 (d=0,40)**. La cuota del estado presente no es el 2% sino el 20–40% con d realista. Es un cambio de constante, no de tasa   [C03·D1] w=.85
N47 ≡ **CONFLICTO DE d SIN RESOLVER**: el CV∝H^(−0,24) de N05 implica d=0,26 exactamente, pero ese d predice ES99(GJR)/ES99(GBM)=1,375 a 20a frente al 1,62 observado. Y el d=0,26 de un GJR simulado es memoria CORTA con τ enorme, no memoria larga genuina. Dos d incompatibles en el grafo: 0,40 (N12) y 0,26 (N05)   [C03·D1] w=.80

N22 ⊣ N22           autodestrucción: premisa y ganancia exigen regímenes opuestos de d
N22 ⊣ N05           N05 es la refutación empírica de la premisa de N22
N03 ← N02           derivación independiente, mismo número: n_eff ≤ T/H con igualdad solo en d=0
N44 → N06           el umbral de Hermite de rango 4 ES la condición de cuarto momento
N12 ⊥ N05           dos d incompatibles: 0,40 vs 0,26 → N47
N46 ⊣ N22           la escapatoria existía, pero en otro nodo

N48 ≡ **EL COSTE DE ESTIMAR CRECE CON EL HORIZONTE** (medido sin contaminación, DGP sin saltos donde el modelo 3 ES la familia del generador): oráculo 3,1%/5,2%/6,6% a 1 mes/1 año/10 años — la especificación no es el problema. Coste de estimar = **+4,0 → +11,2 → +50,0 puntos**. Se multiplica por doce entre un mes y diez años   [orq, verificado] w=.92
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

N55 ≡ **T2 — AUTOVIOLACIÓN DEL MODELO DE COLA** (medido, 20 ajustes): el FHS+EVT produce ξ̂ en la cola de pérdidas con media **+0,372** y **95% de los ajustes por encima de 1/4**, es decir innovaciones SIN CUARTO MOMENTO. Cuarto momento muestral de la empalmada: mediana 117, p95 10.224, máx 57.708 (normal=3, t(7)=5), CV entre ajustes **3,32**. Al pasarlas por la recursión GARCH el proceso simulado tiene M2=∞>1 y su ES **no tiene varianza finita**. El modelo construido para no subestimar las colas se coloca por construcción del lado no identificable de la frontera N06   [orq, medido] w=.88
N56 ≡ **EL MECANISMO DE N28 ES MULTIPLICATIVO, NO ADITIVO**: sumar H variables de índice 1/ξ solo da factor e^(ξ lnH)≈18 a H=2520. Lo que explota es la realimentación GARCH: cada innovación grande entra al cuadrado en la recursión y eleva la varianza futura. Con E[z⁴]=∞ la condición M2<1 falla y la varianza del proceso simulado no converge   [orq] w=.82

N55 → N28           el mecanismo que el encargo N31 pedía, encontrado tras retractar T1
N55 → N06           el modelo EVT cae por construcción del lado M2>1
N55 ⊥ N50           T1 inactivo aquí (ρ≈5,4), T2 activo: son canales distintos

N57 ≡ **EL CRUCE**: a 10 años un modelo MAL especificado con parámetros CONOCIDOS (ORÁCULO-GBM, RMSE 24,0%) bate a uno BIEN especificado con parámetros ESTIMADOS (MODELO-3, RMSE 56,6%). A 1 mes ocurre lo contrario y por un factor de ocho (3,1% vs 26,3%). **Entre un año y diez años, saber los parámetros de un modelo malo pasa a valer más que tener el modelo bueno y estimarlo**   [orq, medido] w=.88

N57 → N48           el cruce es la consecuencia operativa de la amplificación
N57 ⊣ N27           y es lo que queda de N27 una vez quitado lo que no era cierto

N58 ≡ **REGRESO DIVERGENTE DE LA ESTACIONARIEDAD**: certificar T* con precisión relativa ε exige observar k=1/ε² regímenes, o sea T ≥ T*/ε² (±20% ⇒ 25·T*; con T*=50a son 1.250 años), y ese presupuesto mayor exige otro 25× mayor. **La sucesión T_{k+1}=T_k/ε² no tiene punto fijo finito.** Estrictamente más fuerte que N33: allí la cota se vuelve verificable una vez superada; aquí **NUNCA es verificable**   [C04·E2] w=.85
N59 ≡ **FRONTERA DE FALSABILIDAD — H/p < T*/11,4**. Acopla N03 con el presupuesto de estacionariedad. Con T*=5a solo es falsable H≤1,1 días (p=1%) o 5,5 días (p=5%). Lo que exigiría cada norma vigente: **FRTB (ES 10d 97,5%) T*≥18,1a · Basilea II (VaR 10d 99%) 45,2a · Solvencia II (1a 99,5%) 2.280a · ECL vitalicia 10a 11.400a**. Solo el VaR diario sobrevive   [C04·E2] w=.90
N60 ≡ **T̂* NO ES IDENTIFICABLE**: segmentación binaria con valores críticos iid sobre una serie ESTACIONARIA d=0,40 **sin ninguna ruptura** da 3,97 rupturas en 50 años (T̂*=10,1a), indistinguible de un proceso con 4 rupturas reales (4,00 → 10,0a). Tasa de rechazo espurio 0,974. **El T* de la literatura empírica es la sombra del supuesto de memoria corta**   [C04·E2] w=.88
N61 ≡ **CUOTA DE VENTANA**: elegir T* (ventana 1–50a, misma trayectoria, mismo día) mueve el ES₉₉ un factor 1,34 (mediana), 1,73 (p90), **2,16 (p99)**. ~34% del capital regulatorio es un grado de libertad que ningún dato fija. Y el sesgo va al lado tranquilizador: solo el 21% de los saltos reales son visibles ⇒ **T̂*_medido = 4,8·T*_real**   [C04·E2] w=.84
N62 ≡ **PODER CON n_eff, NO CON n**: calibrando bajo la nula honesta (memoria larga sin ruptura), 50 años no detectan al 80% ningún cambio de volatilidad menor que **×1,55**. Δ₈₀ ∝ n^(−(1−2d)/2): 25a→×1,62, 100a→×1,49, 400a→×1,45. Llegar a ×1,10 exige **1,7·10⁶ años**. La literatura documenta el TAMAÑO distorsionado de estos tests; el PODER bajo la nula honesta no   [C04·E2] w=.86
N63 ≡ **CIRCULARIDAD NO RESUELTA** (grieta honesta de E2): la nula «honesta» supone d=0,40 constante, y **el propio d hereda el presupuesto de estacionariedad que se está denunciando**. Además T* no se midió sobre S&P real sino simulado (PDF de Stărică–Granger no extraíble, Stooq bloqueado). Debilidad real del ciclo 4   [C04·E2] w=.90

N58 ⊐ N33           estrictamente más fuerte: nunca verificable, no solo aún no verificable
N59 ⊕ N03 ⊕ N58     el acoplamiento: el muro dice cuántos datos hacen falta, el presupuesto cuántos hay
N60 ⊣ N60           el test que mediría T* rechaza el 97% de las veces sobre procesos sin rupturas
N61 → N10           si elegir la ventana mueve el capital un 34%, T* es endógeno y de política
N63 ⊣ N62           la nula honesta presupone lo que denuncia
