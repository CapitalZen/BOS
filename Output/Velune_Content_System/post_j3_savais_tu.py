import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from velune_brand import (  # noqa: E402
    W, MARGIN,
    BURGUNDY, GOLD, INK, MUTED, STONE,
    F_SERIF, F_SERIF_B, F_SANS, F_MONO,
    font, base_canvas, label_caps, rule, wrap_to_width,
)

img, draw = base_canvas(index="03 / 03")

label_caps(draw, (MARGIN, 168), "Le savais-tu", fill=GOLD, size=20, track=5)

# — Chiffre héros : une seule idée, très grande
f_num = font(F_SERIF_B, 260)
draw.text((MARGIN - 12, 226), "51%", font=f_num, fill=BURGUNDY)

y = 520
rule(draw, MARGIN, y, W - MARGIN, GOLD, 2)
y += 46

f_body = font(F_SERIF, 36)
for line in wrap_to_width(
    draw,
    "des femmes placent le confort avant tout le reste au moment d'acheter un soutien-gorge.",
    f_body, W - 2 * MARGIN,
):
    draw.text((MARGIN, y), line, font=f_body, fill=INK)
    y += 50

y += 34
f_src = font(F_MONO, 17)
draw.text((MARGIN, y), "— étude M&S, 2025", font=f_src, fill=MUTED)

y += 76
f_turn = font(F_SERIF, 34)
for line in wrap_to_width(
    draw, "Et pourtant, le marché continue de vendre du serrage.", f_turn, W - 2 * MARGIN
):
    draw.text((MARGIN, y), line, font=f_turn, fill=BURGUNDY)
    y += 48

rule(draw, MARGIN, 886, W - MARGIN, STONE, 1)
f_q = font(F_SERIF, 29)
draw.text((MARGIN, 918), "Toi aussi tu choisis le confort en premier ?", font=f_q, fill=GOLD)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_j3_savais_tu.png")
img.save(out)
print("saved", out)
