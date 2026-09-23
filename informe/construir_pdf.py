"""Construye informe/investigacion-explicada.pdf. Ejecutar: python3 informe/figuras.py && python3 informe/construir_pdf.py"""
import os, json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, Table,
                                TableStyle, PageBreak, KeepTogether, NextPageTemplate)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

AQUI = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(AQUI, "fig")
SALIDA = os.path.join(AQUI, "investigacion-explicada.pdf")
EXTRA = os.path.join(AQUI, "estrato.json")   # resultado de la tercera muestra bibliografica

D = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("DV", D + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", D + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-I", D + "LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DV-BI", D + "LiberationSans-BoldItalic.ttf"))
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DV-B"); addMapping("DV", 0, 1, "DV-I"); addMapping("DV", 1, 1, "DV-BI")

AZUL = colors.HexColor("#2a78d6"); NARANJA = colors.HexColor("#eb6834")
TINTA = colors.HexColor("#0b0b0b"); TINTA2 = colors.HexColor("#52514e"); MUDO = colors.HexColor("#898781")
REJILLA = colors.HexColor("#e1e0d9"); FONDO = colors.HexColor("#f4f7fc"); FONDO_N = colors.HexColor("#fdf3ee")
FONDO_G = colors.HexColor("#f5f5f2")

E = {}
E["titulo"] = ParagraphStyle("t", fontName="DV-B", fontSize=25, leading=31, textColor=TINTA, spaceAfter=10)
E["subt"] = ParagraphStyle("st", fontName="DV", fontSize=13, leading=19, textColor=TINTA2)
E["h1"] = ParagraphStyle("h1", fontName="DV-B", fontSize=17, leading=22, textColor=TINTA, spaceBefore=4, spaceAfter=10)
E["h2"] = ParagraphStyle("h2", fontName="DV-B", fontSize=12.2, leading=16, textColor=TINTA, spaceBefore=10, spaceAfter=5)
E["h1"].keepWithNext = 1; E["h2"].keepWithNext = 1
E["p"] = ParagraphStyle("p", fontName="DV", fontSize=10.2, leading=15.2, textColor=TINTA, spaceAfter=7)
E["pi"] = ParagraphStyle("pi", parent=E["p"], leftIndent=14, bulletIndent=3)
E["cap"] = ParagraphStyle("cap", fontName="DV-I", fontSize=8.6, leading=12, textColor=TINTA2, spaceBefore=3, spaceAfter=12)
E["caja"] = ParagraphStyle("caja", fontName="DV", fontSize=10, leading=14.6, textColor=TINTA)
E["cajat"] = ParagraphStyle("cajat", fontName="DV-B", fontSize=10.2, leading=14.6, textColor=TINTA, spaceAfter=3)
E["cel"] = ParagraphStyle("cel", fontName="DV", fontSize=8.6, leading=11.6, textColor=TINTA)
E["celb"] = ParagraphStyle("celb", fontName="DV-B", fontSize=8.6, leading=11.6, textColor=TINTA)
E["mono"] = ParagraphStyle("mono", fontName="DV", fontSize=9.4, leading=13, textColor=TINTA, alignment=TA_CENTER,
                           spaceBefore=4, spaceAfter=8)
E["cita"] = ParagraphStyle("cita", fontName="DV-I", fontSize=10.6, leading=16, textColor=TINTA2, leftIndent=18,
                           rightIndent=18, spaceBefore=6, spaceAfter=10)
E["ref"] = ParagraphStyle("ref", fontName="DV", fontSize=8.4, leading=11.4, textColor=TINTA, leftIndent=12,
                          firstLineIndent=-12, spaceAfter=3)

H = []
def h1(t): H.append(Paragraph(t, E["h1"]))
def h2(t): H.append(Paragraph(t, E["h2"]))
def p(t): H.append(Paragraph(t, E["p"]))
def bl(items):
    for it in items: H.append(Paragraph(it, E["pi"], bulletText="•"))
    H.append(Spacer(1, 3))
def cita(t): H.append(Paragraph(t, E["cita"]))
def formula(t): H.append(Paragraph(t, E["mono"]))
def fig(nombre, ancho_cm, pie):
    ruta = os.path.join(FIG, nombre)
    from reportlab.lib.utils import ImageReader
    w, h = ImageReader(ruta).getSize()
    im = Image(ruta, width=ancho_cm * cm, height=ancho_cm * cm * h / w)
    H.append(KeepTogether([im, Paragraph(pie, E["cap"])]))
def caja(titulo, cuerpo, fondo=FONDO, borde=AZUL):
    contenido = []
    if titulo: contenido.append(Paragraph(titulo, E["cajat"]))
    for c in (cuerpo if isinstance(cuerpo, list) else [cuerpo]):
        contenido.append(Paragraph(c, E["caja"]))
    t = Table([[contenido]], colWidths=[16.4 * cm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), fondo), ("LINEBEFORE", (0, 0), (0, -1), 3, borde),
                           ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                           ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    H.append(Spacer(1, 3)); H.append(t); H.append(Spacer(1, 10))
def tabla(filas, anchos, cab=True, zebra=True):
    datos = [[Paragraph(str(c), E["celb"] if (cab and i == 0) else E["cel"]) for c in f] for i, f in enumerate(filas)]
    t = Table(datos, colWidths=[a * cm for a in anchos], repeatRows=1 if cab else 0)
    est = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, 0), 0.8, MUDO),
           ("LINEBELOW", (0, 1), (-1, -1), 0.4, REJILLA), ("TOPPADDING", (0, 0), (-1, -1), 4),
           ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5)]
    if cab: est.append(("BACKGROUND", (0, 0), (-1, 0), FONDO_G))
    t.setStyle(TableStyle(est)); H.append(t); H.append(Spacer(1, 10))

# ============================================================== PORTADA
H.append(Spacer(1, 3.2 * cm))
H.append(Paragraph("Lo que no se puede saber del riesgo a largo plazo", E["titulo"]))
H.append(Paragraph("Una investigación de diez ciclos sobre los límites de las simulaciones de Monte Carlo en "
                   "finanzas, explicada para cualquier persona: qué encontramos, qué resultó no ser nuevo, "
                   "y para qué sirve en la vida diaria.", E["subt"]))
H.append(Spacer(1, 1.4 * cm))
caja(None, ["<i>A corto plazo, lo que importa es cuánto oscila un precio. A largo plazo, lo que importa es "
            "cuánto sube en promedio. Y eso —el promedio— es justo lo que peor se puede medir.</i>"],
     fondo=FONDO_G, borde=MUDO)
H.append(Spacer(1, 3.2 * cm))
H.append(Paragraph("Septiembre de 2026", E["subt"]))
H.append(Paragraph("Todo lo que aparece aquí es reproducible: el código, los datos y cada cifra están en el "
                   "repositorio <b>Sunshide12/Teoria</b>.", ParagraphStyle("x", parent=E["p"], textColor=TINTA2)))
H.append(PageBreak())

# ============================================================== EN UNA PÁGINA
h1("En una página")
p("<b>La pregunta.</b> Bancos, aseguradoras, fondos de pensiones y las aplicaciones que te dicen «con este ahorro "
  "tendrás tanto dinero dentro de 20 años» usan simulaciones: juegan el futuro miles de veces y miran los "
  "peores casos. Nos preguntamos: <b>¿cuánto se puede fiar uno de esos números cuando miran a 10, 15 o 30 años?</b>")
p("<b>Lo que encontramos, en cuatro frases.</b>")
bl(["Todo pronóstico financiero necesita dos ingredientes: cuánto <b>oscila</b> el precio y cuánto <b>sube en "
    "promedio</b>. Las oscilaciones se miden bien con datos; el promedio, muy mal. Con 10 años de historia, el "
    "promedio de la bolsa sólo se conoce con un margen de unos ±10 puntos: si los datos dicen 7 %, la verdad "
    "puede estar entre −3 % y +17 % anual.",
    "A corto plazo el promedio no importa. A largo plazo lo es casi todo. En el mercado estadounidense, "
    "hacia los <b>10 años</b> el promedio pesa ya tanto como todas las oscilaciones juntas.",
    "Por eso, con los mismos datos y decisiones razonables, el «colchón» que hay que guardar para un escenario "
    "muy malo a 10 años puede salir <b>positivo o negativo</b>. Hay una franja de horizontes —en EE.UU., "
    "aproximadamente de 7 a 19 años— donde los datos <b>no pueden decir ni el signo</b>.",
    "Eso cae justo sobre los horizontes de las hipotecas, las pérdidas esperadas de los bancos «a vida del "
    "préstamo» y los planes de pensiones."])
p("<b>Para qué sirve.</b>")
bl(["Para leer con otros ojos cualquier simulador de jubilación o de inversión: la cifra depende casi "
    "entera de un promedio que nadie conoce, y el abanico de escenarios que te enseñan es más estrecho de lo real.",
    "Para saber dónde vale la pena gastar esfuerzo: a corto plazo, en mejorar el modelo; a largo plazo, en "
    "admitir y declarar lo que no se sabe.",
    "Para detectar números «maquillados»: un número que depende de un promedio estimado debería cambiar "
    "bastante cada año; si no cambia, alguien lo está suavizando."])
caja("Lo que honestamente NO encontramos",
     "El encargo era llegar a una teoría completamente nueva. No la hay: de once resultados que creímos propios, "
     "<b>once</b> resultaron estar ya publicados, ser incorrectos, o ambas cosas. Lo que queda es una forma nueva "
     "de <i>leer</i> un problema conocido desde 1980, un programa que se niega a dar un número cuando los datos "
     "no lo sostienen, y un protocolo sellado para comprobarlo con los años. Este documento explica todo, "
     "incluidos los errores.", fondo=FONDO_N, borde=NARANJA)
H.append(PageBreak())

# ============================================================== 1
h1("1. De dónde salió esto")
p("La investigación empezó con un vídeo corto sobre las <b>simulaciones de Monte Carlo</b> aplicadas a fondos de "
  "inversión. La idea de Monte Carlo es sencilla: como no sabemos qué va a pasar, se inventan diez mil futuros "
  "posibles con las reglas de azar que creemos que siguen los precios, y se mira qué ocurre en todos ellos. "
  "Si en el 1 % de los futuros más malos se pierde, en promedio, un 30 % del dinero, ese 30 % es el "
  "<b>colchón</b> que conviene tener apartado.")
p("Los modelos para inventar esos futuros han ido mejorando durante cincuenta años: primero precios que "
  "oscilan de forma regular; luego con saltos bruscos (crisis); luego con oscilaciones que se calman y se "
  "agitan por rachas; luego con «colas gordas», es decir, con desastres más frecuentes de lo que diría una "
  "campana de Gauss. Cada modelo es más realista que el anterior.")
p("Pero el análisis del vídeo tropezó con algo que <b>ninguno</b> de esos modelos arregla, y esa es la grieta por "
  "la que entró esta investigación.")

h1("2. Los dos ingredientes: cuánto oscila y cuánto sube")
p("Cualquier simulación financiera necesita dos números. La <b>volatilidad</b>: cuánto oscila el precio de un "
  "año a otro. Y la <b>deriva</b>: cuánto sube en promedio. El problema es que se miden de forma muy distinta.")
caja("Una analogía: las olas y la marea",
     ["Imagina que quieres saber dos cosas de la orilla del mar: qué tan altas son las olas y si el nivel del "
      "mar está subiendo un centímetro al año. Para las olas, basta mirar un rato: cada ola nueva te da información. "
      "Para la subida del nivel, en cambio, mirar cada segundo no sirve de nada; las olas tapan el centímetro. "
      "Hace falta mirar <b>muchos años</b>.",
      "En la bolsa, las olas son la volatilidad y la marea es la deriva. Tener datos de cada minuto mide "
      "mejor las olas, pero no dice nada nuevo sobre la marea. Lo único que ayuda es el <b>tiempo de calendario</b>."])
p("Esto no es un descubrimiento nuestro: lo demostró el economista Robert Merton en 1980. El error con el que se "
  "conoce el promedio depende sólo de cuántos años de historia hay:")
formula("error del promedio  ≈  volatilidad  /  √(años de historia)")
p("Con la volatilidad típica de la bolsa (16 % anual), el margen de error al 95 % queda así:")
tabla([["años de historia", "5", "10", "20", "30", "50", "100"],
       ["el promedio real puede estar a más o menos…", "±14 puntos", "±10", "±7", "±5,7", "±4,4", "±3,1"]],
      [5.6, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8])
p("Es decir: si los últimos 10 años dicen que la bolsa ha dado un 7 % anual, lo único que se puede afirmar "
  "con seguridad razonable es que el promedio verdadero está entre −3 % y +17 %. Un informe de la Sociedad de "
  "Actuarios de EE.UU. lo resumía así en 2012: <i>«incluso con 50 años de datos de EE.UU., no podemos estar "
  "seguros de que la prima de la bolsa sea mayor que cero»</i>.")

h1("3. Por qué a corto plazo da igual y a largo plazo es todo")
p("El colchón para un escenario muy malo resulta de restar dos cosas: lo que te pueden hacer perder las "
  "oscilaciones, menos lo que se espera ganar en promedio. Y las dos crecen de forma distinta con el tiempo: "
  "las oscilaciones crecen como la <b>raíz cuadrada</b> del horizonte; el promedio crece en <b>línea recta</b>. "
  "Tarde o temprano, la línea recta gana.")
fig("f1_dos_fuerzas.png", 15.2, "Figura 1. Las dos fuerzas que forman el colchón, con los datos del mercado de "
    "acciones de EE.UU. de 1941 a 2026 (rentabilidad media 12,2 % y volatilidad 14,8 % anuales). A diez días el "
    "promedio no pesa casi nada; a diez años pesa tanto como todas las oscilaciones juntas. Las cifras siguen la "
    "aproximación que usan los modelos de riesgo, sin interés compuesto.")
p("A 10 días —el horizonte de la banca de inversión— el promedio es el 3 % del número. A 10 años es el 44 %. "
  "Por eso, en los horizontes largos, todo depende del ingrediente que peor conocemos.")

# ============================================================== 4
h1("4. Primer hallazgo: con los mismos datos, el signo cambia")
p("Tomamos la serie más larga y fiable que existe: el rendimiento total del mercado de acciones de EE.UU., mes "
  "a mes, desde julio de 1926 hasta julio de 2026 (1.201 meses, de la biblioteca de datos de Kenneth French). "
  "Y calculamos el colchón para el peor 1 % de los escenarios a 10 años, cambiando sólo una cosa: <b>cuántos "
  "años de historia se usan</b> para estimar.")
fig("f2_ventana.png", 15.2, "Figura 2. El colchón a 10 años según cuántos años de historia se usen. La línea "
    "naranja supone que el promedio es cero (la costumbre en la banca de inversión). La azul usa el promedio que "
    "dicen los datos: con 10 o 15 años de historia, el modelo dice que <b>no hace falta colchón</b>.")
p("Con los últimos 10 o 15 años, el modelo dice algo absurdo: que <b>incluso en el peor 1 % de los casos se "
  "gana dinero</b>. Con 20 años, dice lo contrario. Suponiendo un promedio de cero —la costumbre en banca— dice "
  "que hay que tener apartado más de lo invertido. Todos son cálculos correctos sobre los mismos datos.")
caja("Qué significa",
     ["Dos analistas igual de competentes, con los mismos datos y decisiones defendibles, pueden llegar a "
      "«hay que apartar mucho» y a «no hay que apartar nada». A un año de plazo, las dos elecciones que casi "
      "nunca se declaran —cuántos años de historia usar y qué promedio suponer— cambian el colchón en un "
      "factor de <b>3,4</b>. A diez años cambian <b>el signo</b>.",
      "<i>Nota: estos modelos pueden dar pérdidas mayores al 100 % a horizontes largos, cosa imposible en una "
      "inversión en acciones. Es otra señal de que las cifras a 10 años no deben leerse literalmente: lo que "
      "importa aquí es el signo y cuánto cambia, no el nivel.</i>"])

h1("5. Segundo hallazgo: la banda ciega")
p("Si el promedio sólo se conoce con un margen de error, el colchón también. La pregunta natural es: ¿a qué "
  "horizontes ese margen de error es tan grande que incluye el cero? Es decir, ¿cuándo no se puede saber ni "
  "si hace falta colchón?")
fig("f3_banda.png", 15.2, "Figura 3. El colchón para el peor 1 % de los casos según el horizonte (línea azul) y "
    "su margen de error por no conocer el promedio (franja azul claro). En la zona gris el margen cruza el cero: "
    "los datos no pueden decir si el colchón es positivo o negativo.")
p("Con los datos de EE.UU. desde 1941, esa franja va aproximadamente de <b>6,6 a 19 años</b>. Por debajo, el "
  "colchón es claramente positivo. Por encima, el modelo dice con seguridad que el colchón es negativo, lo que en "
  "la práctica significa que el modelo deja de ser útil. Y en medio caen justo la <b>vida media de una hipoteca</b> "
  "(unos 7 años, porque muchas se cancelan o se refinancian antes de tiempo), la "
  "<b>pérdida esperada «a vida» que calculan los bancos</b> (unos 10 años) y los <b>planes de pensiones</b> (15 años).")
p("La franja tiene una fórmula cerrada, que comprobamos contra una búsqueda numérica en 18 de 18 casos:")
formula("bordes de la banda  =  [ k<sub>α</sub> / (S ± z/√T) ]<super>2</super>")
p("donde <i>S</i> es el cociente entre promedio y volatilidad (el llamado ratio de Sharpe), <i>T</i> los años de "
  "historia, <i>z</i> = 1,96 y <i>k<sub>α</sub></i> = 2,665 un factor que depende del nivel de confianza.")
caja("Y aquí viene la parte honesta: lo que el agente adversarial destruyó",
     ["En el último ciclo encargamos a un agente, con esa única misión, que intentara destruir este resultado. "
      "No encontró errores de cálculo, pero sí tres cosas que obligan a reducirlo mucho:",
      "<b>1. Es una identidad, no un descubrimiento.</b> La banda es exactamente el margen de error del ratio de "
      "Sharpe dibujado sobre el eje del horizonte. Es Merton 1980 leído de otra manera. Todo su contenido cabe en "
      "una prueba estadística: el Sharpe medido (0,825) no se distingue del que haría cero el colchón a 10 años "
      "(0,843): una diferencia así de pequeña aparecería por puro azar el 87 % de las veces.",
      "<b>2. Depende de qué «promedio» se use.</b> Hay al menos cinco definiciones razonables y dan bandas "
      "distintas (tabla siguiente). El regulador de seguros de EE.UU. usa una con la que la banda se va a 14–93 "
      "años y deja fuera la hipoteca y la pérdida a vida. Sólo los 15 años de las pensiones caen dentro con las cinco.",
      "<b>3. Es sobre todo un fenómeno estadounidense.</b> Con datos de 16 países desarrollados, sólo en 4 cae "
      "el horizonte de 10 años dentro de la banda."], fondo=FONDO_N, borde=NARANJA)
tabla([["cómo se mide el promedio", "Sharpe", "banda ciega (años)", "7 años", "10 años", "15 años"],
       ["rendimiento simple total (el de la figura)", "0,82", "6,6 – 19,0", "dentro", "dentro", "dentro"],
       ["rendimiento logarítmico total", "0,74", "7,8 – 25,1", "fuera", "dentro", "dentro"],
       ["exceso sobre la renta fija, simple", "0,58", "11,3 – 52,9", "fuera", "fuera", "dentro"],
       ["exceso sobre la renta fija, logarítmico", "0,50", "14,0 – 85,8", "fuera", "fuera", "dentro"],
       ["el que fija el regulador de seguros (AAA/NAIC)", "0,49", "14,4 – 92,8", "fuera", "fuera", "dentro"]],
      [6.3, 1.5, 2.8, 1.9, 1.9, 1.9])
h2("El resultado final, y el más honesto")
p("Como el propio ratio de Sharpe tiene margen de error, los bordes de la banda también lo tienen: el borde "
  "inferior puede estar entre 4,3 y 11,4 años, y el superior entre 9,6 y 53 años. Consecuencia: para los "
  "horizontes de 5, 7, 10, 15, 20 y 30 años <b>ni siquiera se puede decidir si están dentro o fuera</b> de la zona "
  "donde nada se puede decidir.")
cita("No se puede determinar qué horizontes están en la región donde nada se determina.")
p("No es un fallo del razonamiento: es el mismo razonamiento aplicado a sí mismo, y es la forma más honesta en "
  "que se puede enunciar lo que encontramos.")

# ============================================================== 6
h1("6. Tercer hallazgo: dónde vale la pena esforzarse")
p("Si el promedio domina a largo plazo, ¿sirve de algo mejorar el modelo de las oscilaciones (añadir saltos, "
  "colas gordas, etc.)? Lo medimos, y la respuesta depende del horizonte.")
fig("f4_esfuerzo.png", 14.0, "Figura 4. Cuánto cambia el colchón de capital al mejorar el modelo (azul) frente a "
    "cuánto lo cambia el error al estimar el promedio (naranja). A 10 días empatan; a 10 años, mejorar el modelo "
    "queda por debajo del umbral de ruido.")
p("A 10 días las dos cosas pesan parecido. A 10 años, perfeccionar el modelo mueve el número un 14 %, mientras "
  "que el error del promedio lo mueve un 111 %. El punto de cruce está en torno a <b>34 días</b>. Según el tipo de "
  "imperfección del modelo, el cruce llega antes o después:")
tabla([["qué le falta al modelo", "a partir de qué horizonte deja de importar frente al promedio"],
       ["colas gordas (desastres más frecuentes)", "19 días"], ["saltos bruscos", "38 días"],
       ["memoria larga en las oscilaciones", "76 días"], ["saltos asimétricos (más caídas que subidas)", "100 días"],
       ["volatilidad que cambia por rachas", "10 meses"], ["volatilidad que sube cuando el precio cae", "3,2 años"],
       ["un nivel de volatilidad que se desplaza con los años", "nunca: este sí importa siempre"]], [9.0, 7.4])
p("También dejamos una fórmula para que cualquier analista sepa si le compensa mejorar su modelo: si el error "
  "del modelo es menor que un porcentaje que depende del horizonte y de los años de historia (2,4 % a 10 días, "
  "11,9 % a un año, 37,5 % a diez años, con 10 años de datos), <b>no merece la pena</b>.")
caja("En corto",
     "En la banca de inversión, a días o semanas, el presupuesto de modelización debe ir a especificar mejor. En "
     "las pérdidas esperadas a vida y en pensiones, todo gasto en sofisticar la cola del modelo es trabajo asignado "
     "a un efecto del 14 %, cuando el efecto grande es un promedio que nadie conoce.")

h1("7. Cuarto hallazgo: una prueba que se puede hacer en cinco años")
p("Casi todo lo anterior sólo se podrá comprobar con décadas de datos. Buscamos algo observable pronto, y lo "
  "encontramos en el propio número, no en el mercado.")
p("Si un banco calcula su colchón a 10 años usando el promedio estimado, cada año que añade un dato nuevo el "
  "promedio se mueve, y el colchón con él. Si en cambio supone un promedio fijo de cero, el número apenas se "
  "mueve. Sobre 90 años de recálculos anuales reales, el número con promedio estimado se revisa <b>unas tres veces "
  "más</b> que el otro. Y el exceso de revisión sigue una ley exacta:")
formula("exceso de variación anual del número  =  H<super>2</super> · 2σ<super>2</super> / T<super>2</super>")
p("Medido sobre la historia real, la ley acierta con un margen del 3 al 17 %, y también si se usa sólo el tramo "
  "más estable de la historia. Por su parte, la Reserva Federal publica que el colchón por estrés que exige a los "
  "grandes bancos cambia en promedio 0,65 puntos de un año a otro sobre un nivel de 3,88: eso equivale a una variación de alrededor "
  "del 21 % del nivel, muy cerca del 20,4 % que predice la aritmética. Es la corroboración externa más clara del "
  "proyecto, aunque la propia Fed está promediando dos años precisamente para reducir esa variación.")
caja("Para qué sirve",
     "Es una prueba de auditoría. Si una entidad dice que su cifra a largo plazo usa un promedio estimado, esa "
     "cifra debería moverse bastante cada año. Si apenas se mueve, o bien el promedio está fijado por decisión (y "
     "debería declararse), o bien alguien está suavizando el número.")
p("<i>Honestidad: la idea de medir cuánto se revisa un número al añadir un año de datos ya estaba publicada para "
  "el riesgo de longevidad (Richards, Currie y Ritchie, 2012), y nuestra primera estimación —que la diferencia "
  "sería de 48 veces— era falsa: al medirla con datos reales es de unas 3 veces.</i>")
H.append(PageBreak())

# ============================================================== 8 USOS
h1("8. ¿Para qué sirve? Usos prácticos")
p("Esta es la parte que más importa si no trabajas en un banco. La lección de fondo cabe en una línea: "
  "<b>cuanto más lejos se mira, más depende todo del promedio, y el promedio es lo que peor se conoce</b>. "
  "Estos son sus usos concretos.")

h2("8.1 Si ahorras o inviertes para tu jubilación")
p("Muchas aplicaciones, bancos y asesores muestran un «abanico» de Monte Carlo: «con un 90 % de probabilidad "
  "tendrás entre X e Y dentro de 25 años». Ese abanico casi siempre trata la rentabilidad media como conocida. "
  "Sólo refleja las olas, no la incertidumbre sobre la marea. A 25 años, <b>el abanico real es bastante más ancho "
  "que el que te enseñan</b>.")
p("Preguntas que conviene hacer ante cualquier simulador:")
bl(["¿Qué rentabilidad media supone, y de dónde sale? ¿De cuántos años de historia?",
    "¿Qué pasa con el plan si esa rentabilidad es 2 o 3 puntos menor? Si el plan deja de funcionar, el plan "
    "depende de una apuesta, no de un cálculo.",
    "¿Esa media viene de EE.UU. en el último siglo? Fue un caso excepcionalmente bueno: en 12 de 16 países "
    "desarrollados la rentabilidad por unidad de riesgo fue más baja."])
caja("Una regla práctica",
     ["Margen de error de la rentabilidad media ≈ 2 × volatilidad / √(años de historia). Con la bolsa "
      "(volatilidad ≈ 16 %) y 20 años de datos: ±7 puntos. Si alguien te dice «históricamente ha dado un 8 %», "
      "con 20 años de historia eso es compatible con cualquier cosa entre el 1 % y el 15 %.",
      "Lo que sí controlas y no depende del promedio: cuánto ahorras, cuánto pagas en comisiones y cuánto tiempo "
      "dejas el dinero. Planifica con una rentabilidad prudente y trata cualquier exceso como un regalo."])

h2("8.2 Si tienes o concedes un crédito a largo plazo")
p("Las normas contables obligan a los bancos a apartar dinero para las pérdidas que esperan a lo largo de toda "
  "la vida de un préstamo: en EE.UU. para todos los préstamos (norma CECL) y en el resto del mundo para los que "
  "han empeorado desde que se concedieron (norma IFRS 9). Para una hipoteca, eso son de 7 a 10 años o más: "
  "justo la banda ciega. El resultado práctico es que esa provisión <b>no debería presentarse como un número "
  "único</b>, sino como un rango acompañado de los supuestos sobre el promedio que la sostienen.")

h2("8.3 Si trabajas en pensiones o seguros")
p("El horizonte de 15 años típico de la gestión de activos y pasivos de un fondo de pensiones es el único que "
  "cayó dentro de la banda con las cinco definiciones del promedio. Los fondos públicos de EE.UU. suelen suponer "
  "rentabilidades en torno al 7 % para valorar sus compromisos, y la investigación académica muestra que esas "
  "expectativas están relacionadas con los resultados pasados de cada fondo (Andonov y Rauh, 2022). Usos concretos:")
bl(["Tratar la rentabilidad supuesta como una <b>decisión de política</b>, declarada y justificada, no como una "
    "estimación de los datos.",
    "Presentar siempre el resultado con al menos tres supuestos de rentabilidad, uno de ellos claramente prudente.",
    "Aprender del regulador de seguros de EE.UU., que desde 2005 hace dos cosas sensatas: rebaja a propósito el "
    "promedio histórico para reconocer la incertidumbre, y se niega a fijar los puntos de la cola a 20 años "
    "«porque los datos históricos no permiten inferencias creíbles»."])

h2("8.4 Si haces planes de negocio o previsiones a varios años")
p("La estructura es la misma fuera de las finanzas: toda proyección a largo plazo es ruido más tendencia. Los "
  "datos miden bien el ruido y mal la tendencia, y cuanto más lejos se proyecta, más pesa la tendencia. Un plan de "
  "negocio a 10 años que supone un crecimiento medio del 8 % porque «los últimos cinco años fueron así» está "
  "haciendo exactamente la misma apuesta que un banco con su colchón a 10 años. Usos:")
bl(["Presentar escenarios de crecimiento, no una sola cifra.",
    "Mirar cuánto cambia tu previsión cada vez que añades un año de datos: si salta mucho, está dominada por una "
    "tendencia estimada y hay que tratarla con cautela.",
    "Cuando la tendencia se apoya en un mecanismo conocido (un contrato firmado, una ley física, una demografía "
    "que ya existe), la advertencia pierde fuerza; cuando sólo sale de extrapolar datos, la gana."])

h2("8.5 Si eres regulador, auditor o periodista")
bl(["Pide que se declare el promedio supuesto en cualquier cifra de riesgo a más de unos pocos años.",
    "Usa la prueba de revisión del apartado 7: si una cifra que dice usar un promedio estimado apenas cambia "
    "de un año a otro, pregunta por qué.",
    "Desconfía de las cifras de riesgo a largo plazo presentadas como un punto sin rango."])

h2("8.6 Si programas o analizas datos: el algoritmo")
p("El repositorio incluye un programa (<b>motor/banda.py</b>) que aplica todo lo anterior a cualquier serie de "
  "rendimientos mensuales y cualquier horizonte. Su virtud no es calcular, sino <b>negarse a calcular</b> cuando "
  "los datos no lo permiten. Hace seis pasos, y cada uno puede anular los siguientes:")
tabla([["paso", "qué comprueba", "qué hace si falla"],
       ["0", "si el promedio ha sido estable en el tiempo", "se detiene: todo lo demás sería inválido"],
       ["1", "desde cuándo la volatilidad es estable", "usa sólo ese tramo"],
       ["2", "la banda ciega, en dos versiones", "la muestra junto al resultado"],
       ["3", "si tu horizonte cae dentro de la banda", "<b>no da un número</b>: da un rango que cruza el cero"],
       ["4", "si merece la pena mejorar el modelo", "te dice el presupuesto de error"],
       ["5", "cuánto debería revisarse el número cada año", "sirve para detectar suavizado"]],
      [1.2, 7.0, 8.2])
p("Se ejecuta con <b>python3 motor/banda.py</b> y pasa 21 de 21 pruebas automáticas. Sobre la bolsa de EE.UU. "
  "divide los horizontes en tres regímenes: a 1, 3 y 5 años el colchón está determinado y es positivo; a 7, 10 y "
  "15 años el programa <b>se niega a dar un número</b>; a 20 y 30 años el colchón está determinado y es negativo, "
  "lo que exige que alguien declare un mínimo en vez de aplicarlo en silencio.")

h2("8.7 La lección general")
cita("Cuanto más lejos miras, más pesa la tendencia; y la tendencia es justo lo que los datos miden peor. "
     "Mirar más a menudo no ayuda: sólo ayuda mirar durante más tiempo.")

# ============================================================== 9 RETRACTACIONES
h1("9. Lo que resultó no ser nuevo, y por qué eso también es un resultado")
p("Esta investigación produjo once resultados que en su momento creímos propios. Los once cayeron: unos porque "
  "ya estaban publicados, otros porque eran incorrectos, y varios por ambas cosas. Seis de ellos se habían "
  "escrito con una confianza del 90 % o más.")
tabla([["lo que creímos", "qué pasó"],
       ["Una frontera entre medidas de capital y de dispersión", "ya publicada (Rockafellar, Uryasev y Zabarankin, 2006)"],
       ["El mecanismo de la complejidad óptima de los modelos", "la prueba que propusimos para defenderlo lo refutó"],
       ["Un sesgo del diagnóstico hacia la calma", "error nuestro sobre un parámetro"],
       ["Que los modelos de cola se contradicen a sí mismos", "publicado y además con un salto lógico"],
       ["Que en la literatura nadie habla de la deriva", "error de muestreo: se nos escapó el artículo clave"],
       ["El horizonte en que se pierde el signo", "publicado (Dowd, Blake y Cairns, 2004) y con error de método"],
       ["Que la regla de la raíz del tiempo cambia la naturaleza del capital", "publicado (Danielsson y Zigrand, 2006) y matemáticamente falso"],
       ["Que hacen falta 55,8 años de datos para decidir", "publicado (Noguer i Alonso, 2026)"],
       ["El límite por correlación entre mercados", "publicado (Giller, 2024)"],
       ["La prueba de revisión con diferencia de 48 veces", "publicada en longevidad (Richards et al., 2012); la cifra real es 3"],
       ["Todo el aparato de la banda ciega", "destruido por nuestro propio agente adversarial (sección 5)"]],
      [8.2, 8.2])
p("La lección de método es la más útil de todo el proyecto: <b>siete de las once caídas se habrían evitado "
  "buscando primero en la literatura</b>. Seis consultas bibliográficas resolvieron en un día lo que una prueba "
  "con datos habría tardado 56 años en resolver. Por eso el protocolo que dejamos obliga a buscar precedentes "
  "<b>antes</b> de cualquier prueba empírica.")
p("También medimos si la confianza que asignábamos a cada afirmación era fiable: de las que llevaban 90 % o más, "
  "falló el 8,8 %. Es decir, estaba bien calibrada… y no protegió a ninguna de las seis que cayeron con esa etiqueta.")

h1("10. Cómo se hizo")
p("La investigación se organizó como un bucle de diez ciclos. En cada ciclo trabajaron tres agentes de "
  "inteligencia artificial con enfoques distintos sobre la misma pregunta. Cada uno entregaba su análisis y, "
  "además, su posición en seis ejes (por ejemplo: ¿el problema es de azar o de ignorancia?, ¿se puede comprobar "
  "hoy o no?). Un pequeño programa comparaba las tres posiciones.")
fig("f5_bucle.png", 15.0, "Figura 5. El bucle. El eje en el que los agentes más discrepaban se convertía en la "
    "pregunta del ciclo siguiente; si coincidían demasiado, entraba un agente cuyo único trabajo era refutar. Todo "
    "quedaba en una memoria comprimida que permite retomar la investigación entera leyendo 2,8 KB.")
p("¿Funcionó? Lo medimos. Los agentes nunca cayeron en darse la razón unos a otros: su coincidencia empezó en "
  "0,91 —a un paso del umbral de alarma— y se mantuvo después entre 0,62 y 0,78. El eje de desacuerdo "
  "«¿el mercado es estable en el tiempo?» dominó cinco ciclos seguidos, hasta que el ciclo 9 lo resolvió "
  "midiendo: la volatilidad sí cambió de forma clara (una década de los años 30 muy agitada); el promedio no "
  "muestra un cambio detectable. Y en el último ciclo, el agente adversarial destruyó el teorema principal "
  "<b>antes</b> de publicarlo, que es lo que nueve ciclos anteriores no consiguieron hacer a tiempo.")
p("Tres agentes fallaron por límites técnicos durante el proceso (ciclos 4, 6 y 8); en esos casos su papel lo "
  "asumió el coordinador, y queda anotado en cada informe.")

# ============================================================== 11 AÑOS
h1("11. Lo que se comprobará con los años")
p("El encargo original pedía una conclusión que sólo el tiempo pudiera confirmar. La dejamos como un "
  "<b>protocolo sellado</b>: seis predicciones con fecha, guardadas con una huella digital (SHA-256) que "
  "delata cualquier cambio posterior, y un programa que cualquiera puede ejecutar en el futuro para ver si se "
  "cumplieron. El programa responde con uno de cinco veredictos: se cumple, falla, anulada (si cambia una premisa), "
  "ya publicada por otros (si aparece un precedente anterior) o en espera.")
tabla([["fecha", "qué se comprueba", "estado hoy"],
       ["siempre", "la ley exacta de revisión (control del propio método)", "<b>se cumple</b>"],
       ["2031", "que el número con promedio estimado se revise más de 1,3 veces que el otro", "en espera (lectura provisional: 4,5 veces)"],
       ["2036", "nada: se declara de antemano que 10 años de datos no bastan para decidir", "compromiso contra nosotros mismos"],
       ["2046", "que los 10 años sigan dentro de la banda ciega en 20 lecturas anuales", "en espera"],
       ["2060", "que la banda no se estreche por debajo de 5 años de ancho", "en espera"],
       ["2082", "que ni con 56 años más de datos se pueda decidir el signo a 10 años", "en espera"]],
      [1.8, 9.2, 5.4])
p("Hay que decir con claridad dos debilidades del protocolo. La primera: las predicciones de 2046 y 2082 son "
  "casi seguras, y por eso informan poco; el agente adversarial mostró que casi cualquier corrección razonable "
  "del margen de error <b>refuerza</b> el resultado en vez de ponerlo a prueba. Las pruebas que de verdad "
  "arriesgan algo son las de revisión (siempre y 2031). La segunda: la de 2036 existe precisamente para impedir "
  "que alguien lea como confirmación un dato que no tiene fuerza estadística suficiente.")
ESTRATO_TXT = "__ESTRATO__"
if os.path.exists(EXTRA):
    ESTRATO_TXT = json.load(open(EXTRA, encoding="utf-8"))["texto"]
h2("La última comprobación: ¿es nuevo?")
p(ESTRATO_TXT)

# ============================================================== GLOSARIO
h1("Glosario")
tabla([["término", "qué significa aquí"],
       ["Monte Carlo", "simular miles de futuros posibles con reglas de azar y mirar qué ocurre en todos ellos"],
       ["volatilidad (σ)", "cuánto oscila un precio de un año a otro; se mide bien con datos"],
       ["deriva o promedio (μ)", "cuánto sube un precio en promedio por año; se mide muy mal con datos"],
       ["ratio de Sharpe (S)", "promedio dividido entre volatilidad: cuánto se gana por cada unidad de oscilación"],
       ["horizonte (H)", "cuántos años hacia el futuro se mira"],
       ["colchón / Expected Shortfall", "pérdida media en el 1 % de los escenarios más malos; lo que conviene tener apartado"],
       ["margen de error / intervalo de confianza", "rango en el que, con un 95 % de seguridad, está el valor verdadero"],
       ["banda ciega", "horizontes en los que el margen de error del colchón incluye el cero"],
       ["ruptura estructural", "momento en que el comportamiento de una serie cambia de forma duradera"],
       ["captura-recaptura", "técnica de ecología para estimar cuántos peces hay en un lago; aquí, cuántos artículos "
                            "relevantes no hemos leído"],
       ["IFRS 9 / CECL", "normas contables que obligan a los bancos a provisionar las pérdidas esperadas de toda la vida del préstamo"],
       ["FRTB, Solvencia II", "normas de capital para la banca de inversión (horizonte de días) y para aseguradoras (1 año)"]],
      [4.6, 11.8])

h1("Referencias principales")
refs = [
 "Merton, R. (1980). On estimating the expected return on the market. <i>Journal of Financial Economics</i>, 8(4).",
 "Danielsson, J. (2002). The emperor has no clothes: limits to risk modelling. <i>Journal of Banking &amp; Finance</i>, 26(7).",
 "Danielsson, J. y Zigrand, J.-P. (2006). On time-scaling of risk and the square-root-of-time rule. <i>Journal of Banking &amp; Finance</i>, 30(10).",
 "Dowd, K., Blake, D. y Cairns, A. (2004). Long-term value at risk. <i>Journal of Risk Finance</i>, 5(2).",
 "Lo, A. (2002). The statistics of Sharpe ratios. <i>Financial Analysts Journal</i>, 58(4).",
 "Pástor, Ľ. y Stambaugh, R. (2012). Are stocks really less volatile in the long run? <i>Journal of Finance</i>, 67(2).",
 "Kerkhof, J., Melenberg, B. y Schumacher, H. (2010). Model risk and capital reserves. <i>Journal of Banking &amp; Finance</i>, 34(1).",
 "Rockafellar, R., Uryasev, S. y Zabarankin, M. (2006). Generalized deviations in risk analysis. <i>Finance and Stochastics</i>, 10(1).",
 "Jorion, P. (1996). Risk²: measuring the risk in value at risk. <i>Financial Analysts Journal</i>, 52(6).",
 "Müller, U. y Watson, M. (2016). Measuring uncertainty about long-run predictions. <i>Review of Economic Studies</i>, 83(4).",
 "Fama, E. y French, K. (2018). Volatility lessons. <i>Financial Analysts Journal</i>, 74(3).",
 "Richards, S., Currie, I. y Ritchie, G. (2014). A value-at-risk framework for longevity trend risk. <i>British Actuarial Journal</i>, 19(1).",
 "Spadafora, L., Dubrovich, M. y Terraneo, M. (2014). Value-at-risk time scaling for long-term risk estimation. arXiv:1408.2462.",
 "Pitera, M., Schmidt, T. y Stettner, Ł. (2023). A novel scaling approach for unbiased adjustment of risk estimators. arXiv:2312.05655.",
 "Giller, G. (2024). Isotropic correlation models for the cross-section of equity returns. arXiv:2411.08864.",
 "Noguer i Alonso, M. (2026). Markets are not random, they are hard to predict. arXiv:2606.08209.",
 "Andonov, A. y Rauh, J. (2022). The return expectations of public pension funds. <i>Review of Financial Studies</i>, 35(8).",
 "Dahlquist, M. e Ibert, M. (2026). Institutions' return expectations across assets and time. <i>Journal of Financial Economics</i>, 175.",
 "American Academy of Actuaries (2005). Recommended approach for setting regulatory RBC requirements for variable annuities (C-3 Phase II).",
 "Modugno, V. (2012). Estimating equity risk premiums. Society of Actuaries, Pension Section Research Committee.",
 "Mina, J. y Xiao, J. (2001). Return to RiskMetrics: the evolution of a standard. RiskMetrics Group.",
 "Board of Governors of the Federal Reserve System (2025). Propuesta de promediado del stress capital buffer, 17 de abril.",
 "Datos: Kenneth R. French Data Library (factores de Fama–French, 1926–2026); base de datos Jordà–Schularick–Taylor (Macrohistory).",
]
for r in refs: H.append(Paragraph(r, E["ref"]))
H.append(Spacer(1, 12))
h2("Dónde está cada cosa en el repositorio")
tabla([["carpeta", "contenido"],
       ["ciclos/", "un informe por ciclo y los informes literales de los 30 agentes"],
       ["teorema/", "cada intento de teorema, incluidos los retractados y por qué"],
       ["verificacion/", "los cálculos que respaldan cada cifra de este documento"],
       ["motor/banda.py", "el algoritmo, con sus 21 pruebas"],
       ["protocolo/", "las seis predicciones selladas y el programa que las resuelve"],
       ["memoria/", "la memoria comprimida para retomar la investigación"],
       ["informe/", "este documento y el código que genera sus figuras"]], [4.0, 12.4])

# ============================================================== MAQUETA
def pie(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFont("DV", 7.6); canvas.setFillColor(MUDO)
        canvas.drawString(2.3 * cm, 1.3 * cm, "Lo que no se puede saber del riesgo a largo plazo")
        canvas.drawRightString(A4[0] - 2.3 * cm, 1.3 * cm, str(doc.page))
        canvas.setStrokeColor(REJILLA); canvas.setLineWidth(0.5)
        canvas.line(2.3 * cm, 1.65 * cm, A4[0] - 2.3 * cm, 1.65 * cm)
    canvas.restoreState()

doc = BaseDocTemplate(SALIDA, pagesize=A4, leftMargin=2.3 * cm, rightMargin=2.3 * cm, topMargin=2.0 * cm,
                      bottomMargin=2.2 * cm, title="Lo que no se puede saber del riesgo a largo plazo",
                      author="Investigación Teoria (Sunshide12/Teoria)",
                      subject="Límites de la simulación de Monte Carlo en riesgo financiero a largo plazo")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=pie)])
doc.build(H)
print("escrito:", SALIDA)
