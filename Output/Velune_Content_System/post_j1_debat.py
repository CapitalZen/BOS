import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from velune_brand import (
    W, H, BURGUNDY, GOLD, CHARCOAL, WHITE, ROSE_DEEP,
    F_BOLD, F_ITAL, font, wrap_to_width, draw_multiline_centered,
    card, footer_prompt, base_canvas,
)

img, draw = base_canvas()

# Hook
f_hook = font(F_BOLD, 66)
hook = "Le pire ennemi du soutif, c'est lequel pour toi ?"
lines = wrap_to_width(draw, hook, f_hook, W - 160)
y = 175
y = draw_multiline_centered(img, draw, lines, f_hook, y, CHARCOAL, line_gap=10)

options = [
    ("A", "L'armature qui pique"),
    ("B", "La bretelle qui glisse toute la journée"),
    ("C", "La marque rouge qui reste le soir"),
]

card_w = W - 140
card_h = 118
gap = 26
start_y = y + 55
badge_r = 34

f_badge = font(F_BOLD, 34)
f_opt = font(F_BOLD, 36)

for i, (letter, opt_text) in enumerate(options):
    y0 = start_y + i * (card_h + gap)
    x0 = 70
    x1 = x0 + card_w
    y1 = y0 + card_h
    img = card(img, (x0, y0, x1, y1), radius=32, fill=WHITE)
    draw = ImageDraw.Draw(img)

    bx = x0 + 70
    by = y0 + card_h / 2
    draw.ellipse([bx - badge_r, by - badge_r, bx + badge_r, by + badge_r], fill=BURGUNDY)
    bb = draw.textbbox((0, 0), letter, font=f_badge)
    draw.text((bx - (bb[2] - bb[0]) / 2 - bb[0], by - (bb[3] - bb[1]) / 2 - bb[1]), letter, font=f_badge, fill=WHITE)

    tx = bx + badge_r + 34
    ob = draw.textbbox((0, 0), opt_text, font=f_opt)
    max_w = x1 - tx - 40
    opt_lines = wrap_to_width(draw, opt_text, f_opt, max_w)
    if len(opt_lines) == 1:
        ty = by - (ob[3] - ob[1]) / 2 - ob[1]
        draw.text((tx, ty), opt_text, font=f_opt, fill=CHARCOAL)
    else:
        ty = by - (len(opt_lines) * 40) / 2
        for ln in opt_lines:
            draw.text((tx, ty), ln, font=f_opt, fill=CHARCOAL)
            ty += 40

footer_prompt(img, draw, "Dis-moi lequel — et si j'en ai oublié un pire, je veux le savoir.")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_j1_debat.png")
img.save(out)
print("saved", out)
