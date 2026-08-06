from PIL import Image, ImageDraw, ImageFont

W = H = 1080
bg = (232, 205, 202)   # dusty rose blush
fg = (109, 42, 52)     # deep burgundy
gold = (183, 141, 92)  # muted rose-gold for the moon

img = Image.new("RGB", (W, H), bg)
draw = ImageDraw.Draw(img)

# subtle vignette: slightly darker soft radial edge for depth
overlay = Image.new("L", (W, H), 0)
odraw = ImageDraw.Draw(overlay)
odraw.ellipse([-200, -200, W + 200, H + 200], fill=40)
odraw.ellipse([120, 120, W - 120, H - 120], fill=0)
dark = Image.new("RGB", (W, H), (60, 30, 30))
img = Image.composite(dark, img, overlay)
draw = ImageDraw.Draw(img)

# crescent moon: filled gold circle, minus offset bg-colored circle
moon_r = 95
moon_cx, moon_cy = W // 2, 390
moon = Image.new("RGBA", (W, H), (0, 0, 0, 0))
mdraw = ImageDraw.Draw(moon)
mdraw.ellipse([moon_cx - moon_r, moon_cy - moon_r, moon_cx + moon_r, moon_cy + moon_r], fill=gold + (255,))
cut_r = 88
cut_off = 42
mdraw.ellipse([moon_cx - cut_r + cut_off, moon_cy - cut_r, moon_cx + cut_r + cut_off, moon_cy + cut_r], fill=(0, 0, 0, 0))
img.paste(moon, (0, 0), moon)
draw = ImageDraw.Draw(img)

# wordmark
font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf", 128)
text = "Velune"
bbox = draw.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
tx = (W - tw) / 2 - bbox[0]
ty = 560
draw.text((tx, ty), text, font=font, fill=fg)

# thin rule under wordmark
rule_y = ty + th + 55
rule_w = 130
draw.line([(W/2 - rule_w, rule_y), (W/2 + rule_w, rule_y)], fill=gold, width=3)

img.save("velune_logo.png")
print("done", img.size)
