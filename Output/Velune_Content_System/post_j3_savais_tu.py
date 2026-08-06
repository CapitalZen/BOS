import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from velune_brand import (
    W, H, BURGUNDY, GOLD, CHARCOAL, WHITE, ROSE_DEEP,
    F_BOLD, F_ITAL, F_SANS, font, wrap_to_width, draw_multiline_centered,
    card, footer_prompt, base_canvas,
)

img, draw = base_canvas()

f_label = font(F_BOLD, 40)
label = "LE SAVAIS-TU ?"
lb = draw.textbbox((0, 0), label, font=f_label)
draw.text((W / 2 - (lb[2] - lb[0]) / 2 - lb[0], 175), label, font=f_label, fill=BURGUNDY)

# big stat card
card_xy = (100, 275, W - 100, 640)
img = card(img, card_xy, radius=44, fill=WHITE)
draw = ImageDraw.Draw(img)

f_stat = font(F_BOLD, 190)
stat = "51%"
sb = draw.textbbox((0, 0), stat, font=f_stat)
draw.text((W / 2 - (sb[2] - sb[0]) / 2 - sb[0], 320), stat, font=f_stat, fill=GOLD)

f_capt = font(F_SANS, 30)
capt = "des femmes placent le confort avant tout le reste au moment d'acheter un soutien-gorge"
capt_lines = wrap_to_width(draw, capt, f_capt, (card_xy[2] - card_xy[0]) - 120)
y = 530
y = draw_multiline_centered(img, draw, capt_lines, f_capt, y, CHARCOAL, line_gap=8)

f_src = font(F_ITAL, 22)
src = "— étude M&S, 2025"
sb2 = draw.textbbox((0, 0), src, font=f_src)
draw.text((W / 2 - (sb2[2] - sb2[0]) / 2 - sb2[0], 595), src, font=f_src, fill=GOLD)

f_comment = font(F_BOLD, 42)
comment = "Et pourtant, le marché continue de vendre du serrage."
c_lines = wrap_to_width(draw, comment, f_comment, W - 200)
y = draw_multiline_centered(img, draw, c_lines, f_comment, 700, CHARCOAL, line_gap=8)

footer_prompt(img, draw, "Toi aussi tu choisis le confort en premier, ou pas encore ?")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "v2_j3_savais_tu.png")
img.save(out)
print("saved", out)
