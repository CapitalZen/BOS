import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from velune_brand import (
    W, H, BURGUNDY, GOLD, CHARCOAL, WHITE, ROSE_DEEP,
    F_BOLD, F_ITAL, F_SANS, font, wrap_to_width, draw_multiline_centered,
    card, footer_prompt, base_canvas,
)

img, draw = base_canvas()

f_hook = font(F_BOLD, 54)
hook = "Sillons rouges, oppression thoracique, lourdeur en fin de journée."
lines = wrap_to_width(draw, hook, f_hook, W - 160)
y = 150
y = draw_multiline_centered(img, draw, lines, f_hook, y, CHARCOAL, line_gap=8)

f_sub = font(F_ITAL, 34)
sub = "On t'a appris que c'était normal. Ça ne devrait pas l'être."
sub_lines = wrap_to_width(draw, sub, f_sub, W - 200)
y = draw_multiline_centered(img, draw, sub_lines, f_sub, y + 18, BURGUNDY, line_gap=6) + 10

col_w = (W - 140 - 30) / 2
col_h = 430
y0 = y + 20
left = (70, y0, 70 + col_w, y0 + col_h)
right = (70 + col_w + 30, y0, 70 + col_w + 30 + col_w, y0 + col_h)

img = card(img, left, radius=36, fill=WHITE)
img = card(img, right, radius=36, fill=(250, 234, 224))
draw = ImageDraw.Draw(img)

f_label = font(F_BOLD, 30)
f_item = font(F_SANS, 26)

def draw_column(xy, label, label_color, items, mark, mark_color):
    x0, y0, x1, y1 = xy
    pad = 36
    lb = draw.textbbox((0, 0), label, font=f_label)
    draw.text((x0 + pad, y0 + 30), label, font=f_label, fill=label_color)
    yy = y0 + 30 + (lb[3] - lb[1]) + 34
    for it in items:
        draw.ellipse([x0 + pad, yy + 4, x0 + pad + 34, yy + 38], outline=mark_color, width=3)
        mb = draw.textbbox((0, 0), mark, font=f_item)
        draw.text((x0 + pad + 17 - (mb[2] - mb[0]) / 2 - mb[0], yy + 21 - (mb[3] - mb[1]) / 2 - mb[1]),
                   mark, font=f_item, fill=mark_color)
        it_lines = wrap_to_width(draw, it, f_item, (x1 - x0) - pad * 2 - 50)
        ty = yy
        for ln in it_lines:
            draw.text((x0 + pad + 50, ty), ln, font=f_item, fill=CHARCOAL)
            ty += 34
        yy = ty + 22

draw_column(left, "ON T'A DIT", BURGUNDY,
            ["Que serrer = maintenir", "Que la marque rouge, c'est normal", "Que le confort, c'est pour plus tard"],
            "x", BURGUNDY)

draw_column(right, "ÇA DEVRAIT ÊTRE", GOLD,
            ["Un tissu qui suit sans comprimer", "Une bretelle qui reste où tu la mets", "Un soutif que t'oublies à 18h"],
            "✓", GOLD)

footer_prompt(img, draw, "Tu te reconnais dans laquelle des deux colonnes aujourd'hui ?")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_j2_avant_apres.png")
img.save(out)
print("saved", out)
