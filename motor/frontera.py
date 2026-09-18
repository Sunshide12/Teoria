"""
Poda del grafo por peso. El grafo completo es el registro auditable y crece sin
limite; la FRONTERA es lo que hay que leer para retomar la investigacion.

Sin esto, la promesa del sistema de memoria se rompe sola: 92 nodos y 43 KB ya no
caben en el presupuesto de ~1,5k tokens con el que se diseno.

Uso:  python3 motor/frontera.py [umbral]   (por defecto 0.80)
"""
import re, sys

def podar(ruta="memoria/GRAFO.md", umbral=0.80):
    txt = open(ruta).read()
    nodos = re.findall(r"^(N\d+[ab]?) ≡ (.*?)\s+w=([\d.]+)\s*$", txt, re.M)
    vivos  = [(i,c,float(w)) for i,c,w in nodos if float(w) >= umbral]
    muertos= [(i,c,float(w)) for i,c,w in nodos if float(w) <  umbral]
    return vivos, muertos

if __name__ == "__main__":
    u = float(sys.argv[1]) if len(sys.argv) > 1 else 0.80
    vivos, muertos = podar(umbral=u)
    vivos.sort(key=lambda t: -t[2])
    print(f"# FRONTERA — nodos con w ≥ {u}\n")
    print(f"<!-- {len(vivos)} vivos de {len(vivos)+len(muertos)}. "
          f"El grafo completo, con lo refutado y lo degradado, está en GRAFO.md. -->\n")
    for i,c,w in vivos:
        print(f"{i} ≡ {c}   **w={w}**\n")
    print(f"\n---\n\n## Degradado o refutado ({len(muertos)} nodos)\n")
    print("Se conservan en `GRAFO.md` con su peso y el motivo. Los principales:\n")
    for i,c,w in sorted(muertos, key=lambda t: t[2])[:12]:
        corto = c[:150] + ("…" if len(c) > 150 else "")
        print(f"- **{i}** (w={w}) — {corto}")
