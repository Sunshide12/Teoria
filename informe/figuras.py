"""Figuras del informe divulgativo. Todas salen de protocolo/serie-congelada.csv."""
import math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

AQUI = os.path.dirname(os.path.abspath(__file__))
SERIE = os.path.join(AQUI, "..", "protocolo", "serie-congelada.csv")
OUT = os.path.join(AQUI, "fig")

# tokens (paleta de referencia, modo claro; el PDF es un medio impreso)
AZUL, NARANJA = "#2a78d6", "#eb6834"
AZUL_CLARO = "#cde2fb"
TINTA, TINTA2, MUDO = "#0b0b0b", "#52514e", "#898781"
REJILLA, EJE, NEUTRO = "#e1e0d9", "#c3c2b7", "#e8e7e2"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.edgecolor": EJE, "axes.labelcolor": TINTA2, "axes.linewidth": 0.8,
    "xtick.color": MUDO, "ytick.color": MUDO, "xtick.labelsize": 9, "ytick.labelsize": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": REJILLA, "grid.linewidth": 0.6,
    "axes.axisbelow": True, "figure.dpi": 200, "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})

from matplotlib.ticker import FuncFormatter
def _coma(v, _pos=None):
    t = f"{v:g}" if abs(v - round(v)) > 1e-9 else f"{int(round(v))}"
    return t.replace(".", ",").replace("-", "\u2212")
COMA = FuncFormatter(_coma)
def ejes(ax):
    ax.xaxis.set_major_formatter(COMA); ax.yaxis.set_major_formatter(COMA)

def serie():
    ym, r = [], []
    for ln in open(SERIE, encoding="latin-1"):
        p = ln.strip().split(",")
        if len(p) == 5 and p[0].strip().isdigit() and len(p[0].strip()) == 6:
            ym.append(int(p[0])); r.append((float(p[1]) + float(p[4])) / 100)
    return np.array(ym), np.array(r)

ym, x = serie()
k = stats.norm.pdf(stats.norm.ppf(.99)) / .01
z = 1.959963985
pos = int(np.where(ym == 194108)[0][0])
w = x[pos:]; T = len(w) / 12
mu = w.mean() * 12; sd = w.std(ddof=1) * math.sqrt(12); S = mu / sd
fmt = lambda v, d=1: f"{v:.{d}f}".replace(".", ",")

# ---------------------------------------------------------------- figura 1
H = np.linspace(0.01, 30, 400)
colchon = k * sd * np.sqrt(H)
ganancia = mu * H
H0 = (k / S) ** 2
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.plot(H, colchon, color=AZUL, lw=2)
ax.plot(H, ganancia, color=NARANJA, lw=2)
ax.plot([H0], [mu * H0], "o", ms=7, color=TINTA, mec="white", mew=2, zorder=5)
ax.annotate(f"se cruzan hacia los {fmt(H0)} años", (H0, mu * H0), (H0 + 1.5, mu * H0 - 0.55),
            color=TINTA, fontsize=9, arrowprops=dict(arrowstyle="-", color=MUDO, lw=0.8))
ax.text(29.5, 1.72, "lo que pueden hacerte\nperder las oscilaciones", color=TINTA2,
        ha="right", va="top", fontsize=9)
ax.text(19.0, 2.95, "lo que se espera ganar\nen promedio", color=TINTA2,
        ha="right", va="bottom", fontsize=9)
ax.plot([], [], color=AZUL, lw=2, label="oscilaciones (volatilidad)")
ax.plot([], [], color=NARANJA, lw=2, label="promedio esperado (deriva)")
ax.legend(frameon=False, loc="lower right", fontsize=9, labelcolor=TINTA2)
ax.set_xlabel("horizonte (años)"); ax.set_ylabel("fracción del dinero invertido")
ax.set_xlim(0, 30); ax.set_ylim(0, 3.9); ejes(ax)
fig.savefig(os.path.join(OUT, "f1_dos_fuerzas.png")); plt.close(fig)

# ---------------------------------------------------------------- figura 2
ventanas = [5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100]
es_mu, es_0 = [], []
for Tw in ventanas:
    n = min(Tw * 12, len(x)); ww = x[-n:]
    m_ = ww.mean() * 12; s_ = ww.std(ddof=1) * math.sqrt(12)
    es_mu.append(-m_ * 10 + k * s_ * math.sqrt(10)); es_0.append(k * s_ * math.sqrt(10))
fig, ax = plt.subplots(figsize=(6.4, 3.3))
ax.axhline(0, color=EJE, lw=1)
ax.plot(ventanas, es_0, color=NARANJA, lw=2)
ax.plot(ventanas, es_mu, color=AZUL, lw=2)
ax.plot(ventanas, es_mu, "o", ms=6, color=AZUL, mec="white", mew=1.5)
ax.text(101, es_0[-1], "suponiendo que el\npromedio es cero", color=TINTA2, fontsize=9, va="center")
ax.text(101, es_mu[-1], "usando el promedio\nque dicen los datos", color=TINTA2, fontsize=9, va="center")
ax.text(8.6, -0.30, "\u22120,18", ha="right", va="top", color=TINTA, fontsize=8.5)
ax.text(16.4, -0.30, "\u22120,20", ha="left", va="top", color=TINTA, fontsize=8.5)
ax.text(24, -0.58, "por debajo de cero el modelo dice «ganarás\nincluso en el peor 1 % de los casos»", ha="left",
        va="center", color=TINTA2, fontsize=8.5)
ax.set_xlabel("cuántos años de historia se usan para estimar")
ax.set_ylabel("colchón necesario a 10 años\n(peor 1 % de los casos)")
ax.set_xlim(0, 100); ax.set_ylim(-0.9, 1.8); ejes(ax)
fig.savefig(os.path.join(OUT, "f2_ventana.png")); plt.close(fig)

# ---------------------------------------------------------------- figura 3
H = np.linspace(0.02, 30, 600)
se = sd / math.sqrt(T)
centro = -mu * H + k * sd * np.sqrt(H)
lo = -(mu + z * se) * H + k * sd * np.sqrt(H)
hi = -(mu - z * se) * H + k * sd * np.sqrt(H)
Hm = (k / (S + z / math.sqrt(T))) ** 2; Hp = (k / (S - z / math.sqrt(T))) ** 2
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ax.axvspan(Hm, Hp, color=NEUTRO, zorder=0, lw=0)
ax.axhline(0, color=TINTA2, lw=1)
ax.fill_between(H, lo, hi, color=AZUL_CLARO, lw=0)
ax.plot(H, centro, color=AZUL, lw=2)
ax.text((Hm + Hp) / 2, 0.78, f"BANDA CIEGA\n{fmt(Hm)} – {fmt(Hp)} años", ha="center", va="top",
        color=TINTA, fontsize=9.5, weight="bold")
ax.text(3.2, -0.55, "colchón positivo:\nel signo es seguro", ha="center", color=TINTA2, fontsize=8.5)
ax.text(25.2, 0.30, "colchón negativo:\nel modelo dice que\nno hace falta ninguno", ha="center", color=TINTA2, fontsize=8.5)
marcas = [(1, "1 año\n(seguros)", (0.5, 0.40), "left"), (7, "7 años\n(hipoteca)", (7.0, 0.30), "center"),
          (10, "10 años (pérdida\nesperada a vida)", (9.6, -0.10), "right"),
          (15, "15 años\n(pensiones)", (14.2, -0.40), "right")]
for h, lab, xy, ha in marcas:
    v = -mu * h + k * sd * math.sqrt(h)
    ax.plot([h], [v], "o", ms=6, color=TINTA, mec="white", mew=1.5, zorder=5)
    ax.text(xy[0], xy[1], lab, ha=ha, va="top" if h >= 10 else "bottom", fontsize=7.5, color=TINTA2)
ax.set_xlabel("horizonte (años)"); ax.set_ylabel("colchón necesario\n(peor 1 % de los casos)")
ax.set_xlim(0, 30); ax.set_ylim(-1.6, 0.85); ejes(ax)
fig.savefig(os.path.join(OUT, "f3_banda.png")); plt.close(fig)

# ---------------------------------------------------------------- figura 4
grupos = ["a 10 días", "a 10 años"]
modelo = [1.289, 1.142]; estim = [1.231, 2.111]
xg = np.arange(2); ancho = 0.34
fig, ax = plt.subplots(figsize=(6.0, 3.2))
b1 = ax.bar(xg - ancho / 2 - 0.01, [m - 1 for m in modelo], ancho, bottom=1, color=AZUL)
b2 = ax.bar(xg + ancho / 2 + 0.01, [e - 1 for e in estim], ancho, bottom=1, color=NARANJA)
ax.axhline(1.3, color=MUDO, lw=1, ls=(0, (4, 3)))
ax.set_xlim(-0.5, 1.5)
ax.text(1.53, 1.3, "1,3×: por debajo\nes ruido", color=MUDO, fontsize=8, ha="left", va="center", clip_on=False)
for bars, vals in ((b1, modelo), (b2, estim)):
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.03, fmt(v, 2) + "×", ha="center", fontsize=9, color=TINTA)
ax.set_xticks(xg, grupos); ax.set_ylim(1, 2.35); ax.yaxis.set_major_formatter(COMA)
ax.set_ylabel("cuánto cambia el\ncolchón de capital")
ax.bar([0], [0], color=AZUL, label="mejorar el modelo de las oscilaciones")
ax.bar([0], [0], color=NARANJA, label="error al estimar el promedio")
ax.legend(frameon=False, loc="upper left", fontsize=9, labelcolor=TINTA2)
ax.grid(axis="x", visible=False)
fig.savefig(os.path.join(OUT, "f4_esfuerzo.png")); plt.close(fig)

print(f"mu={mu:.4f} sd={sd:.4f} S={S:.4f} T={T:.1f} H0={H0:.2f} banda=({Hm:.2f},{Hp:.2f})")
print("ES10a por ventana:", [round(v, 3) for v in es_mu])

# ---------------------------------------------------------------- figura 5: el bucle
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.set_xlim(0, 10.1); ax.set_ylim(0, 5.75); ax.axis("off")
def rect(x, y, w, h, fc="white", ec=EJE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=fc, ec=ec, lw=1))
def flecha(x1, y1, x2, y2, rad=0.0, color=MUDO, lw=1.1):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=11,
                                 color=color, lw=lw, connectionstyle=f"arc3,rad={rad}"))
def txt(x, y, t, size=8, color=TINTA2, weight="normal"):
    ax.text(x, y, t, ha="center", va="center", fontsize=size, color=color, weight=weight)
# pregunta
rect(0.1, 2.3, 2.1, 1.3); txt(1.15, 3.15, "Pregunta", 9.5, TINTA, "bold"); txt(1.15, 2.7, "la grieta del\nciclo anterior")
# agentes
for lab, yy in [("Agente 1", 3.35), ("Agente 2", 2.7), ("Agente 3", 2.05)]:
    rect(3.0, yy - 0.05, 1.7, 0.5, fc=AZUL_CLARO, ec=AZUL); txt(3.85, yy + 0.2, lab, 8.5, TINTA)
    flecha(2.22, 2.95, 2.98, yy + 0.2); flecha(4.72, yy + 0.2, 5.38, 2.95)
# motor
rect(5.4, 2.3, 2.25, 1.3); txt(6.525, 3.15, "Motor", 9.5, TINTA, "bold"); txt(6.525, 2.7, "coherencia κ y\neje de desacuerdo")
# decisiones
rect(7.95, 2.95, 2.05, 1.2, fc="#fdf0ea", ec=NARANJA)
txt(8.975, 3.78, "¿Demasiado\nde acuerdo?", 7.8, TINTA, "bold"); txt(8.975, 3.25, "entra un agente\nque intenta refutar", 7.2)
rect(7.95, 1.7, 2.05, 1.05)
txt(8.975, 2.43, "Si discrepan", 7.8, TINTA, "bold"); txt(8.975, 2.02, "se ataca el eje\ndel desacuerdo", 7.2)
flecha(7.67, 3.2, 7.93, 3.5); flecha(7.67, 2.7, 7.93, 2.3)
# memoria
rect(2.6, 0.15, 4.8, 1.0, fc="#f6f6f3")
txt(5.0, 0.83, "Memoria comprimida", 9.5, TINTA, "bold")
txt(5.0, 0.45, "157 afirmaciones con peso + 1 línea por ciclo (2,8 KB)", 7.5)
flecha(6.5, 2.28, 6.0, 1.18)
# retorno por arriba
flecha(8.975, 4.17, 1.15, 3.62, rad=0.26, color=AZUL, lw=1.4)
txt(5.0, 5.5, "× 10 ciclos: la respuesta de uno es la pregunta del siguiente", 8.5, AZUL, "bold")
fig.savefig(os.path.join(OUT, "f5_bucle.png")); plt.close(fig)
