import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from velune_brand import (  # noqa: E402
    W, MARGIN, COL_GAP, COL_W,
    BURGUNDY, GOLD, INK, MUTED, STONE,
    F_SERIF, F_SERIF_B, F_SANS,
    font, base_canvas, label_caps, rule, vrule, wrap_to_width,
)

img, draw = base_canvas(index="02 / 03")

# — Titre : une seule idée forte, en serif large
f_hook = font(F_SERIF_B, 62)
y = 150
for line in wrap_to_width(draw, "On t'a dit que serrer, c'était maintenir.", f_hook, W - 2 * MARGIN):
    draw.text((MARGIN, y), line, font=f_hook, fill=BURGUNDY)
    y += 78

y += 26
rule(draw, MARGIN, y, W - MARGIN, GOLD, 2)
y += 62

# — Deux colonnes, séparées par un filet. Pas de carte, pas d'ombre.
COL_TOP = y
COL_BOTTOM = 800
x_left = MARGIN
x_right = MARGIN + COL_W + COL_GAP
vrule(draw, W / 2, COL_TOP - 10, COL_BOTTOM, STONE, 1)

f_item = font(F_SERIF, 30)


def column(x, label, label_color, items, item_color):
    label_caps(draw, (x, COL_TOP), label, fill=label_color, size=20, track=5)
    yy = COL_TOP + 62
    for it in items:
        for line in wrap_to_width(draw, it, f_item, COL_W - 30):
            draw.text((x, yy), line, font=f_item, fill=item_color)
            yy += 40
        yy += 30


column(
    x_left, "La norme", MUTED,
    ["Que serrer = maintenir",
     "Que la marque rouge, c'est normal",
     "Que le confort, c'est pour plus tard"],
    MUTED,
)

column(
    x_right, "Ça devrait être", GOLD,
    ["Un tissu qui suit sans comprimer",
     "Une bretelle qui reste où tu la mets",
     "Un soutif que t'oublies à 18h"],
    INK,
)

# — Question de clôture, en italique serif sous un filet
rule(draw, MARGIN, COL_BOTTOM + 24, W - MARGIN, STONE, 1)
f_q = font(F_SERIF, 29)
draw.text((MARGIN, COL_BOTTOM + 56),
          "Tu te reconnais dans laquelle des deux colonnes ?",
          font=f_q, fill=GOLD)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_j2_avant_apres.png")
img.save(out)
print("saved", out)
