"""Planche d'identité Velune — grille 3x3, standard brandkit.

Rendu déterministe en PIL : la typographie est nette et maîtrisée, ce qu'aucun
modèle de diffusion ne garantit sur un livrable de charte.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

from velune_brand import (  # noqa: E402
    IVORY, STONE, ROSE, BURGUNDY, GOLD, INK, MUTED,
    F_SERIF, F_SERIF_B, F_SANS, F_MONO,
    font, moon_icon, tracked, tracked_width,
)

# — Canvas de présentation : charcoal extérieur, panneaux ivoire
BW, BH = 2000, 1500
CHARCOAL = (28, 24, 24)
PAD = 64          # marge extérieure
GUT = 20          # gouttière entre panneaux
COLS, ROWS = 3, 3
PW = (BW - 2 * PAD - (COLS - 1) * GUT) / COLS
PH = (BH - 2 * PAD - (ROWS - 1) * GUT) / ROWS


def panel_box(c, r):
    x0 = PAD + c * (PW + GUT)
    y0 = PAD + r * (PH + GUT)
    return x0, y0, x0 + PW, y0 + PH


def grain(img, amount=0.05, seed=11):
    import random
    rnd = random.Random(seed)
    w, h = img.size
    n = Image.new("L", (w // 2, h // 2))
    n.putdata([rnd.gauss(128, 12) for _ in range((w // 2) * (h // 2))])
    n = n.resize((w, h), Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.4))
    return Image.blend(img, Image.merge("RGB", (n, n, n)), amount)


board = Image.new("RGB", (BW, BH), CHARCOAL)
d = ImageDraw.Draw(board)

# — En-tête de planche
f_head = font(F_MONO, 17)
d.text((PAD, PAD - 38), "VELUNE — IDENTITÉ DE MARQUE", font=f_head, fill=(150, 138, 134))
lab = "01 — SYSTÈME"
d.text((BW - PAD - d.textlength(lab, font=f_head), PAD - 38), lab, font=f_head, fill=(120, 108, 104))


def panel(c, r, fill=IVORY):
    x0, y0, x1, y1 = panel_box(c, r)
    p = Image.new("RGB", (int(x1 - x0), int(y1 - y0)), fill)
    return p, ImageDraw.Draw(p), (int(x0), int(y0))


def paste(p, pos, textured=True):
    board.paste(grain(p) if textured else p, pos)


def caption(pd, w, h, s):
    """Micro-label de panneau, en bas à gauche."""
    pd.text((28, h - 34), s, font=font(F_MONO, 13), fill=MUTED)


# ─────────────────────────── 1. Couverture logo
p, pd, pos = panel(0, 0)
w, h = p.size
m = moon_icon(56, GOLD)
pd_x = 44
p.paste(m, (pd_x, int(h / 2) - 78), m)
f_word = font(F_SERIF, 74)
pd.text((pd_x - 4, h / 2 - 10), "Velune", font=f_word, fill=BURGUNDY)
f_tag = font(F_MONO, 14)
tracked(pd, (pd_x, h / 2 + 92), "LINGERIE SANS ARMATURE", f_tag, MUTED, track=3)
caption(pd, w, h, "01 · WORDMARK")
paste(p, pos)

# ─────────────────────────── 2. Construction du symbole
p, pd, pos = panel(1, 0)
w, h = p.size
cx, cy, R = w / 2, h / 2 - 8, 82
pd.ellipse([cx - R - 42, cy - R - 42, cx + R + 42, cy + R + 42], outline=STONE, width=1)
for gx in range(int(cx - R - 42), int(cx + R + 43), 21):
    pd.line([(gx, cy - R - 42), (gx, cy + R + 42)], fill=(233, 226, 218), width=1)
pd.line([(cx - R - 60, cy), (cx + R + 60, cy)], fill=STONE, width=1)
pd.line([(cx, cy - R - 60), (cx, cy + R + 60)], fill=STONE, width=1)
pd.ellipse([cx - R, cy - R, cx + R, cy + R], fill=BURGUNDY)
off = R * 0.40
pd.ellipse([cx - R + off, cy - R, cx + R + off, cy + R], fill=IVORY)
pd.ellipse([cx - R + off, cy - R, cx + R + off, cy + R], outline=STONE, width=1)
pd.text((28, 30), "Deux cercles. Un décalage de 0,40 R.",
        font=font(F_SERIF, 19), fill=INK)
caption(pd, w, h, "02 · CONSTRUCTION")
paste(p, pos)

# ─────────────────────────── 3. Application numérique
p, pd, pos = panel(2, 0)
w, h = p.size
bx0, by0, bx1, by1 = 34, 54, w - 34, h - 96
pd.rounded_rectangle([bx0, by0, bx1, by1], radius=10, fill=(255, 253, 250), outline=STONE, width=1)
pd.rounded_rectangle([bx0, by0, bx1, by0 + 38], radius=10, fill=(238, 232, 224))
pd.rectangle([bx0, by0 + 28, bx1, by0 + 38], fill=(238, 232, 224))
for i, cc in enumerate([(224, 116, 112), (226, 190, 120), (168, 196, 158)]):
    pd.ellipse([bx0 + 16 + i * 18, by0 + 13, bx0 + 26 + i * 18, by0 + 23], fill=cc)
pd.rounded_rectangle([bx0 + 84, by0 + 10, bx1 - 20, by0 + 28], radius=9, fill=(250, 247, 243))
pd.text((bx0 + 96, by0 + 13), "velune.fr", font=font(F_MONO, 12), fill=MUTED)
mm = moon_icon(20, GOLD)
p.paste(mm, (int(bx0 + 26), int(by0 + 70)), mm)
pd.text((bx0 + 54, by0 + 64), "Velune", font=font(F_SERIF, 26), fill=BURGUNDY)
pd.line([(bx0 + 26, by0 + 116), (bx1 - 26, by0 + 116)], fill=(236, 230, 222), width=1)
pd.text((bx0 + 26, by0 + 136), "Le soutif qui ne ment pas",
        font=font(F_SERIF, 22), fill=INK)
pd.rounded_rectangle([bx0 + 26, by0 + 178, bx0 + 168, by0 + 214], radius=18, fill=BURGUNDY)
pd.text((bx0 + 52, by0 + 188), "Découvrir", font=font(F_SANS, 14), fill=IVORY)
caption(pd, w, h, "03 · APPLICATION WEB")
paste(p, pos)

# ─────────────────────────── 4. Essence / tagline
p, pd, pos = panel(0, 1, fill=BURGUNDY)
w, h = p.size
f_t = font(F_SERIF, 40)
pd.text((44, h / 2 - 62), "Le soutif", font=f_t, fill=IVORY)
pd.text((44, h / 2 - 14), "qui ne ment", font=f_t, fill=IVORY)
pd.text((44, h / 2 + 34), "pas.", font=f_t, fill=GOLD)
pd.text((28, h - 34), "04 · ESSENCE", font=font(F_MONO, 13), fill=(196, 158, 150))
paste(p, pos)

# ─────────────────────────── 5. Palette
p, pd, pos = panel(1, 1)
w, h = p.size
pd.text((28, 30), "Palette", font=font(F_SERIF, 22), fill=INK)
swatches = [("Ivoire", IVORY), ("Rose", ROSE), ("Pierre", STONE),
            ("Or", GOLD), ("Bordeaux", BURGUNDY), ("Encre", INK)]
sw, sh = (w - 56 - 2 * 14) / 3, 92
for i, (name, col) in enumerate(swatches):
    cx0 = 28 + (i % 3) * (sw + 14)
    cy0 = 78 + (i // 3) * (sh + 46)
    pd.rectangle([cx0, cy0, cx0 + sw, cy0 + sh], fill=col, outline=STONE, width=1)
    pd.text((cx0, cy0 + sh + 8), name, font=font(F_SANS, 13), fill=INK)
    pd.text((cx0, cy0 + sh + 24), "#%02X%02X%02X" % col, font=font(F_MONO, 11), fill=MUTED)
caption(pd, w, h, "05 · COULEUR")
paste(p, pos)

# ─────────────────────────── 6. Typographie
p, pd, pos = panel(2, 1)
w, h = p.size
pd.text((28, 26), "Aa", font=font(F_SERIF_B, 76), fill=BURGUNDY)
pd.text((150, 44), "DejaVu Serif", font=font(F_SANS, 17), fill=INK)
pd.text((150, 68), "Titres · chiffres · wordmark", font=font(F_SANS, 13), fill=MUTED)
pd.line([(28, 130), (w - 28, 130)], fill=STONE, width=1)
pd.text((28, 148), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", font=font(F_SERIF, 17), fill=INK)
pd.text((28, 174), "abcdefghijklmnopqrstuvwxyz", font=font(F_SERIF, 17), fill=INK)
pd.text((28, 200), "0123456789 — % € ,.", font=font(F_SERIF, 17), fill=MUTED)
pd.line([(28, 234), (w - 28, 234)], fill=STONE, width=1)
tracked(pd, (28, 252), "LABELS EN CAPITALES", font(F_SANS, 13), GOLD, track=5)
pd.text((28, 278), "— étude M&S, 2025", font=font(F_MONO, 13), fill=MUTED)
caption(pd, w, h, "06 · TYPOGRAPHIE")
paste(p, pos)

# ─────────────────────────── 7. Application physique — étiquette
p, pd, pos = panel(0, 2)
w, h = p.size
lx0, ly0, lx1, ly1 = w / 2 - 92, h / 2 - 108, w / 2 + 92, h / 2 + 96
sh_img = Image.new("RGBA", p.size, (0, 0, 0, 0))
ImageDraw.Draw(sh_img).rounded_rectangle([lx0 + 4, ly0 + 10, lx1 + 4, ly1 + 10],
                                         radius=8, fill=(60, 40, 40, 46))
p.paste(Image.alpha_composite(p.convert("RGBA"),
                              sh_img.filter(ImageFilter.GaussianBlur(12))).convert("RGB"), (0, 0))
pd = ImageDraw.Draw(p)
pd.rounded_rectangle([lx0, ly0, lx1, ly1], radius=8, fill=(253, 250, 246), outline=STONE, width=1)
mm = moon_icon(22, GOLD)
p.paste(mm, (int(w / 2 - 11), int(ly0 + 30)), mm)
f_l = font(F_SERIF, 25)
tw = pd.textlength("Velune", font=f_l)
pd.text((w / 2 - tw / 2, ly0 + 62), "Velune", font=f_l, fill=BURGUNDY)
pd.line([(lx0 + 34, ly0 + 106), (lx1 - 34, ly0 + 106)], fill=(232, 226, 218), width=1)
for i, ln in enumerate(["TAILLE  M", "SANS ARMATURE", "COTON / ÉLASTHANNE"]):
    lw = tracked_width(pd, ln, font(F_MONO, 11), 2)
    tracked(pd, (w / 2 - lw / 2, ly0 + 128 + i * 22), ln, font(F_MONO, 11), MUTED, track=2)
caption(pd, w, h, "07 · ÉTIQUETTE")
paste(p, pos)

# ─────────────────────────── 8. Direction d'image
p, pd, pos = panel(1, 2, fill=(232, 214, 208))
w, h = p.size
for i in range(90):
    t = i / 90
    yy = h * 0.30 + i * 2.4
    col = tuple(int(a * (1 - t * 0.55)) for a in (236, 206, 198))
    pd.line([(0, yy), (w, yy - 26)], fill=col, width=3)
pd.ellipse([w * 0.60, h * 0.13, w * 0.60 + 74, h * 0.13 + 74], fill=(246, 232, 226))
ov = Image.new("RGBA", p.size, (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for yy in range(0, h, 4):
    od.line([(0, yy), (w, yy)], fill=(255, 255, 255, 22), width=1)
p = Image.alpha_composite(p.convert("RGBA"), ov).convert("RGB")
pd = ImageDraw.Draw(p)
tracked(pd, (28, 28), "MATIÈRE · PEAU · LUMIÈRE RASANTE", font(F_MONO, 12), (120, 74, 74), track=3)
pd.text((28, h - 34), "08 · DIRECTION D'IMAGE", font=font(F_MONO, 13), fill=(150, 104, 100))
paste(p, pos)

# ─────────────────────────── 9. Détails du système
p, pd, pos = panel(2, 2)
w, h = p.size
pd.text((28, 26), "Système", font=font(F_SERIF, 22), fill=INK)
pd.line([(28, 66), (w - 28, 66)], fill=GOLD, width=2)
pd.text((28, 82), "Filet d'accent · 2 px", font=font(F_SANS, 12), fill=MUTED)
pd.line([(28, 118), (w - 28, 118)], fill=STONE, width=1)
pd.text((28, 132), "Filet de séparation · 1 px", font=font(F_SANS, 12), fill=MUTED)
for i, (lb, cl) in enumerate([("01 / 03", MUTED), ("02 / 03", MUTED), ("03 / 03", GOLD)]):
    pd.text((28 + i * 78, 176), lb, font=font(F_MONO, 14), fill=cl)
pd.text((28, 202), "Index de série", font=font(F_SANS, 12), fill=MUTED)
mm = moon_icon(15, GOLD)
p.paste(mm, (28, 240), mm)
pd.text((52, 236), "Velune", font=font(F_SERIF, 17), fill=BURGUNDY)
pd.text((28, 268), "Signature de pied", font=font(F_SANS, 12), fill=MUTED)
caption(pd, w, h, "09 · DÉTAILS")
paste(p, pos)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "velune_brand_board.png")
board.save(out)
print("saved", out, board.size)
