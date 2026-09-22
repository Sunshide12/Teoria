#!/usr/bin/env python3
"""
resolve.py — resolutor del protocolo de falsacion T6 ("la banda ciega").

Se ejecuta sin argumentos. Imprime, para cada prediccion registrada en
protocol.json, uno de cuatro veredictos:

    PASS   la prediccion se cumple con los datos disponibles hoy
    FAIL   la prediccion esta refutada
    VOID   una premisa del protocolo ha caido (ruptura en la media, serie muerta)
    MOOT   la puerta bibliografica encontro precedente anterior al preregistro
    ESPERA aun no ha llegado la fecha de resolucion

Orden de ejecucion (no es negociable, y es el punto del ciclo 8):
la puerta BIBLIOGRAFICA corre antes que el test empirico. Seis consultas
resolvieron en un dia lo que el test empirico habria tardado 56 anos.

Uso:
    python3 resolve.py                 # descarga la serie si hace falta
    python3 resolve.py --csv ruta.csv  # usa una copia local
    python3 resolve.py --anio 2046     # trunca la serie para simular esa lectura
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
import math
import os
import sys
import urllib.request
import zipfile

try:
    import numpy as np
    from scipy import stats
except ImportError:
    sys.exit("hacen falta numpy y scipy:  pip install numpy scipy")

AQUI = os.path.dirname(os.path.abspath(__file__))
PROTO = os.path.join(AQUI, "protocol.json")


# --------------------------------------------------------------- serie

def cargar_serie(csv_path: str | None) -> tuple[np.ndarray, np.ndarray, str]:
    """Devuelve (yyyymm, rentabilidad total mensual en tanto por uno, sha256)."""
    if csv_path:
        crudo = open(csv_path, "rb").read()
    else:
        cache = os.path.join(AQUI, "serie-congelada.csv")
        if os.path.exists(cache):
            crudo = open(cache, "rb").read()
        else:
            url = json.load(open(PROTO, encoding="utf-8"))["serie_congelada"]["url"]
            with urllib.request.urlopen(url, timeout=120) as r:
                zbytes = r.read()
            with zipfile.ZipFile(io.BytesIO(zbytes)) as z:
                nombre = [n for n in z.namelist() if n.lower().endswith(".csv")][0]
                crudo = z.read(nombre)
            open(cache, "wb").write(crudo)

    sha = hashlib.sha256(crudo).hexdigest()
    ym, r = [], []
    for linea in crudo.decode("latin-1").splitlines():
        p = linea.strip().split(",")
        if len(p) == 5 and p[0].strip().isdigit() and len(p[0].strip()) == 6:
            ym.append(int(p[0]))
            r.append((float(p[1]) + float(p[4])) / 100.0)   # Mkt-RF + RF
    return np.array(ym), np.array(r), sha


# --------------------------------------------------------------- estadistica

def anualizar(w: np.ndarray) -> tuple[float, float]:
    return w.mean() * 12, w.std(ddof=1) * math.sqrt(12)


def hac_var(e: np.ndarray) -> float:
    n = len(e)
    L = int(4 * (n / 100) ** (2 / 9))
    e = e - e.mean()
    s = (e @ e) / n
    for l in range(1, L + 1):
        s += 2 * (1 - l / (L + 1)) * (e[l:] @ e[:-l]) / n
    return s


def sup_wald(y: np.ndarray, recorte: float) -> tuple[float, int | None]:
    """sup-Wald de Andrews para un cambio de nivel en la media, con HAC."""
    n = len(y)
    if n < 120:
        return 0.0, None
    s2 = hac_var(y)
    if s2 <= 0:
        return 0.0, None
    mejor = (0.0, None)
    for b in range(int(recorte * n), int((1 - recorte) * n)):
        m1, m2 = y[:b].mean(), y[b:].mean()
        W = (m1 - m2) ** 2 / (s2 * (1 / b + 1 / (n - b)))
        if W > mejor[0]:
            mejor = (W, b)
    return mejor


def ultima_ruptura_volatilidad(x: np.ndarray, crit: float, recorte: float) -> tuple[int | None, dict]:
    """Busqueda secuencial tipo Bai-Perron. Los tres proxies deben coincidir."""
    detalle = {}
    posiciones = []
    for etiqueta, y in (("log(r^2)", np.log(x ** 2 + 1e-12)),
                        ("|r|", np.abs(x)),
                        ("r^2", x ** 2)):
        segs, brks = [(0, len(y))], []
        for _ in range(6):
            cand = []
            for (a, b) in segs:
                W, bb = sup_wald(y[a:b], recorte)
                if bb is not None and W > crit:
                    cand.append((W, a + bb, (a, b)))
            if not cand:
                break
            W, pos, (a, b) = max(cand)
            brks.append(pos)
            segs.remove((a, b))
            segs += [(a, pos), (pos, b)]
        brks.sort()
        detalle[etiqueta] = brks
        posiciones.append(max(brks) if brks else None)

    validas = [p for p in posiciones if p is not None]
    if len(validas) < 2:          # hace falta mayoria de proxies
        return None, detalle
    return int(np.median(validas)), detalle


def banda(S: float, T: float, k: float, z: float) -> tuple[float, float]:
    e = z / math.sqrt(T)
    H_menos = (k / (S + e)) ** 2
    H_mas = (k / (S - e)) ** 2 if S > e else float("inf")
    return H_menos, H_mas


# --------------------------------------------------------------- puerta bibliografica

def puerta_bibliografica(P: dict) -> tuple[bool, list[str]]:
    """Devuelve (hay_precedente_bloqueante, motivos).

    No se automatiza la busqueda: se automatiza la OBLIGACION de haberla hecho.
    Quien resuelva el protocolo escribe aqui, en precedentes_hallados, lo que
    encontro; si alguno cubre una prediccion, esa prediccion es MOOT.
    """
    g = P["puerta_bibliografica"]
    hallados = g.get("precedentes_hallados", [])
    bloqueantes = [h for h in hallados if h.get("bloquea")]
    motivos = [f"{h['cita']} -> bloquea {h['bloquea']}" for h in bloqueantes]
    return bool(bloqueantes), motivos


# --------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv")
    ap.add_argument("--anio", type=int, help="trunca la serie a diciembre de ese ano")
    args = ap.parse_args()

    P = json.load(open(PROTO, encoding="utf-8"))
    C = P["constantes_congeladas"]
    k, z = C["k_alpha"], C["z"]
    crit, recorte = C["valor_critico_supWald"], C["recorte_ruptura"]
    H_obj = C["H_objetivo_anios"]

    # ---- sello
    copia = {kk: vv for kk, vv in P.items() if kk not in ("sello_sha256", "sello_cubre")}
    calc = hashlib.sha256(json.dumps(copia, ensure_ascii=False, indent=2).encode("utf-8")).hexdigest()
    sello_ok = (calc == P.get("sello_sha256"))

    ym, x, sha = cargar_serie(args.csv)
    if args.anio:
        m = ym <= args.anio * 100 + 12
        ym, x = ym[m], x[m]

    print("=" * 76)
    print(P["nombre"])
    print("=" * 76)
    print(f"preregistrado   : {P['fecha_preregistro']}")
    print(f"resuelto        : {dt.date.today().isoformat()}")
    print(f"sello           : {'INTACTO' if sello_ok else 'ROTO — el protocolo fue editado tras sellarse'}")
    print(f"serie           : {ym[0]//100}-{ym[0]%100:02d} .. {ym[-1]//100}-{ym[-1]%100:02d}  ({len(x)} meses)")
    ref = P["serie_congelada"]["sha256_csv_al_sellar"]
    print(f"sha256 serie    : {'igual que al sellar' if sha == ref else 'DISTINTO — la historia fue revisada o ampliada (normal al anadir anos)'}")
    print()

    # ---- PUERTA BIBLIOGRAFICA, PRIMERO
    print("-" * 76)
    print("PUERTA BIBLIOGRAFICA  (se ejecuta ANTES que el test empirico)")
    print("-" * 76)
    bloqueado, motivos = puerta_bibliografica(P)
    estado_puerta = P["puerta_bibliografica"].get("estado", "")
    if bloqueado:
        for m_ in motivos:
            print(f"  PRECEDENTE: {m_}")
    else:
        print("  sin precedente bloqueante registrado")
    print(f"  estado: {estado_puerta}")
    moot = {m_.split("-> bloquea ")[-1].strip() for m_ in motivos}
    print()

    # ---- DISPARADOR VOID: ruptura en la media
    print("-" * 76)
    print("DISPARADORES")
    print("-" * 76)
    W_media, b_media = sup_wald(x, recorte)
    void_media = W_media > crit
    print(f"  sup-Wald HAC sobre la MEDIA = {W_media:6.2f}  (critico {crit})"
          f"  -> {'VOID: mu no es constante' if void_media else 'premisa de mu constante en pie'}")
    if b_media is not None:
        print(f"     (maximo en {ym[b_media]//100}-{ym[b_media]%100:02d}, sin significacion)" if not void_media else "")

    pos, detalle = ultima_ruptura_volatilidad(x, crit, recorte)
    if pos is None:
        T_est = len(x) / 12
        print(f"  rupturas de VOLATILIDAD: ninguna al {C['nivel_ruptura']:.0%} "
              f"-> T_est = {T_est:.1f}a  (ATENCION: este es el caso que DEBILITA el teorema)")
    else:
        T_est = (len(x) - pos) / 12
        print(f"  ultima ruptura de VOLATILIDAD: {ym[pos]//100}-{ym[pos]%100:02d}"
              f"  -> T_est = {T_est:.1f}a")
        for et, br in detalle.items():
            print(f"     {et:9s}: {[f'{ym[p]//100}-{ym[p]%100:02d}' for p in br] or 'ninguna'}")
    print()

    # ---- LA BANDA
    n = int(round(T_est * 12))
    mu, sd = anualizar(x[-n:])
    S = mu / sd
    H_menos, H_mas = banda(S, T_est, k, z)
    dentro = H_menos < H_obj < H_mas
    print("-" * 76)
    print("LA BANDA CIEGA    H-/+ = [ k_alpha / (S -/+ z/sqrt(T_est)) ]^2")
    print("-" * 76)
    print(f"  ventana estacionaria : {T_est:.1f} anios")
    print(f"  mu = {mu:.4f}   sigma = {sd:.4f}   S = {S:.4f}   z/sqrt(T) = {z/math.sqrt(T_est):.4f}")
    print(f"  BANDA = ({H_menos:.2f} , {H_mas:.2f}) anios        H0 = (k/S)^2 = {(k/S)**2:.3f}")
    print(f"  anchura = {H_mas - H_menos:.2f} anios")
    print(f"  H = {H_obj:.0f} anios esta {'DENTRO — signo indeterminado' if dentro else 'FUERA — signo determinado'}")
    print()

    # ---- FIRMA DE REVISION (P-1, P-2)
    def firma(Tv: int):
        nv = Tv * 12
        idx = list(range(len(x) - nv, -1, -12))[::-1]
        vmu, v0, sds = [], [], []
        for i in idx:
            m_, s_ = anualizar(x[i:i + nv])
            vmu.append(-m_ * H_obj + k * s_ * math.sqrt(H_obj))
            v0.append(k * s_ * math.sqrt(H_obj))
            sds.append(s_)
        vmu, v0 = np.array(vmu), np.array(v0)
        dmu, d0 = np.diff(vmu), np.diff(v0)
        base = v0[:-1]
        razon = (dmu / base).std(ddof=1) / (d0 / base).std(ddof=1)
        exc = dmu.var(ddof=1) - d0.var(ddof=1)
        medido = math.sqrt(max(exc, 0.0))
        teorico = H_obj * math.sqrt(2) * float(np.mean(sds)) / Tv
        return razon, medido / teorico if teorico else float("nan"), len(dmu), vmu, v0

    razon10, cociente10, nrev10, vmu10, v010 = firma(10)
    razon20, cociente20, _, _, _ = firma(20)
    razon30, cociente30, _, _, _ = firma(30)

    print("-" * 76)
    print("FIRMA DE REVISION")
    print("-" * 76)
    print(f"  ventana 10a, {nrev10} reestimaciones anuales")
    print(f"    razon SD(revision | mu estimada) / SD(revision | mu=0) = {razon10:.2f}x")
    print(f"    ley exacta  medido/teorico:  T=10 {cociente10:.3f}   T=20 {cociente20:.3f}   T=30 {cociente30:.3f}")
    print(f"    ES99 a 10a hoy:  con mu=0  {v010[-1]:+.4f}   con mu estimada  {vmu10[-1]:+.4f}")
    print()

    # ---- VEREDICTOS
    print("=" * 76)
    print("VEREDICTOS")
    print("=" * 76)
    hoy = dt.date.today()
    ult5 = None
    if nrev10 >= 5:
        i0 = len(vmu10) - 6
        a = np.diff(vmu10[i0:]) / v010[i0:-1]
        b = np.diff(v010[i0:]) / v010[i0:-1]
        ult5 = a.std(ddof=1) / b.std(ddof=1)

    def emitir(pid, veredicto, detalle_txt):
        print(f"  {pid:5s}  {veredicto:6s}  {detalle_txt}")

    for pr in P["predicciones"]:
        pid = pr["id"]
        fecha = dt.date.fromisoformat(pr["fecha_resolucion"])
        if pid in moot:
            emitir(pid, "MOOT", "precedente anterior al preregistro")
            continue
        if void_media:
            emitir(pid, "VOID", "ruptura detectada en la media: la premisa de mu constante ha caido")
            continue
        if hoy < fecha and pid != "P-2":
            emitir(pid, "ESPERA", f"resuelve el {pr['fecha_resolucion']}"
                                  + (f"  [lectura provisional: razon 5 anos = {ult5:.2f}x]" if pid == "P-1" and ult5 else ""))
            continue
        if pid == "P-1":
            emitir(pid, "PASS" if (ult5 or 0) > C["umbral_impacto_decisional"] else "FAIL",
                   f"razon sobre las 5 ultimas reestimaciones = {ult5:.2f}x  (umbral {C['umbral_impacto_decisional']})")
        elif pid == "P-2":
            ok = all(0.70 <= c <= 1.40 for c in (cociente10, cociente20, cociente30))
            emitir(pid, "PASS" if ok else "FAIL",
                   f"medido/teorico = {cociente10:.3f} / {cociente20:.3f} / {cociente30:.3f}  (banda [0.70, 1.40])")
        elif pid == "P-3":
            emitir(pid, "n/a", "registro sin veredicto POR DISENO — leerlo como confirmacion incumple el protocolo")
        elif pid in ("P-4", "P-6"):
            emitir(pid, "PASS" if dentro else "FAIL",
                   f"H={H_obj:.0f} {'dentro' if dentro else 'FUERA'} de ({H_menos:.2f}, {H_mas:.2f})")
        elif pid == "P-5":
            emitir(pid, "PASS" if (H_mas - H_menos) > 5.0 else "FAIL",
                   f"anchura = {H_mas - H_menos:.2f} anios  (umbral 5.0)")
    print()
    print("  P-2 se evalua siempre: es el control del aparato, no una prediccion sobre el futuro.")
    print("  Si P-2 FALLA, ningun otro veredicto de este protocolo significa nada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
