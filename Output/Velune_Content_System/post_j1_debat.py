import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from velune_brand import (  # noqa: E402
    W, MARGIN,
    BURGUNDY, GOLD, INK, MUTED, STONE,
    F_SERIF, F_SERIF_B, F_MONO,
    font, base_canvas, label_caps, rule, wrap_to_width,
)

img, draw = base_canvas(index="01 / 03")

label_caps(draw, (MARGIN, 168), "Le débat", fill=GOLD, size=20, track=5)

f_hook = font(F_SERIF_B, 60)
y = 226
for line in wrap_to_width(draw, "Le pire ennemi du soutif, c'est lequel pour toi ?", f_hook, W - 2 * MARGIN):
    draw.text((MARGIN, y), line, font=f_hook, fill=BURGUNDY)
    y += 76

y += 30
rule(draw, MARGIN, y, W - MARGIN, GOLD, 2)
y += 58

# — Options : la lettre en mono comme repère, pas de pastille ni de carte
f_letter = font(F_MONO, 22)
f_opt = font(F_SERIF, 36)

for letter, opt in [
    ("A", "L'armature qui pique"),
    ("B", "La bretelle qui glisse toute la journée"),
    ("C", "La marque rouge qui reste le soir"),
]:
    draw.text((MARGIN, y + 8), letter, font=f_letter, fill=GOLD)
    yy = y
    for line in wrap_to_width(draw, opt, f_opt, W - 2 * MARGIN - 74):
        draw.text((MARGIN + 74, yy), line, font=f_opt, fill=INK)
        yy += 46
    y = yy + 74

rule(draw, MARGIN, 886, W - MARGIN, STONE, 1)
f_q = font(F_SERIF, 29)
draw.text((MARGIN, 918), "Dis-moi lequel — ou si j'en ai oublié un pire.", font=f_q, fill=GOLD)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_j1_debat.png")
img.save(out)
print("saved", out)
