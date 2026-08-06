"""Système de template partagé pour les visuels Velune — cohérence de marque sur tous les posts."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1080
CREAM = (251, 239, 233)
ROSE = (232, 205, 202)
ROSE_DEEP = (216, 178, 176)
BURGUNDY = (109, 42, 52)
GOLD = (183, 141, 92)
CHARCOAL = (58, 46, 46)
WHITE = (255, 250, 247)

F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_ITAL = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
F_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap_to_width(draw, text, f, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=f)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_multiline_centered(img, draw, lines, f, y, fill, line_gap=14):
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=f)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text((W / 2 - w / 2 - bbox[0], y), line, font=f, fill=fill)
        y += h + line_gap
    return y


def gradient_bg(top=CREAM, bottom=ROSE):
    base = Image.new("RGB", (1, H), top)
    d = ImageDraw.Draw(base)
    for y in range(H):
        t = y / H
        r = int(top[0] * (1 - t) + bottom[0] * t)
        g = int(top[1] * (1 - t) + bottom[1] * t)
        b = int(top[2] * (1 - t) + bottom[2] * t)
        d.point((0, y), fill=(r, g, b))
    return base.resize((W, H))


def add_vignette(img, strength=30):
    overlay = Image.new("L", (W, H), 0)
    od = ImageDraw.Draw(overlay)
    od.ellipse([-260, -260, W + 260, H + 260], fill=strength)
    od.ellipse([90, 90, W - 90, H - 90], fill=0)
    overlay = overlay.filter(ImageFilter.GaussianBlur(140))
    dark = Image.new("RGB", (W, H), (45, 22, 24))
    return Image.composite(dark, img, overlay)


def moon_icon(size=40, color=GOLD):
    s = size * 2
    icon = Image.new("RGBA", (int(s * 1.4), s), (0, 0, 0, 0))
    d = ImageDraw.Draw(icon)
    d.ellipse([0, 0, s, s], fill=color + (255,))
    cut = int(s * 0.42)
    d.ellipse([cut, 0, cut + s, s], fill=(0, 0, 0, 0))
    return icon


def brand_header(img, draw, dark_on_light=True):
    color = GOLD
    m = moon_icon(15, color)
    f = font(F_SANS, 26)
    text = "V E L U N E"
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    total_w = m.width + 14 + tw
    x0 = W / 2 - total_w / 2
    img.paste(m, (int(x0), 58), m)
    draw.text((x0 + m.width + 14, 66), text, font=f, fill=color)


def shadow_for(xy, radius, blur=28, opacity=60, offset=(0, 16)):
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    x0, y0, x1, y1 = xy
    sd.rounded_rectangle(
        [x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]],
        radius=radius, fill=(50, 24, 24, opacity),
    )
    return sh.filter(ImageFilter.GaussianBlur(blur))


def card(img, xy, radius=44, fill=WHITE, shadow=True):
    if shadow:
        sh = shadow_for(xy, radius)
        img.paste(Image.alpha_composite(img.convert("RGBA"), sh).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(xy, radius=radius, fill=fill)
    return img


def footer_prompt(img, draw, text):
    f = font(F_ITAL, 34)
    lines = wrap_to_width(draw, text, f, W - 220)
    y = H - 130 - (len(lines) - 1) * 46
    draw_multiline_centered(img, draw, lines, f, y, BURGUNDY, line_gap=10)


def base_canvas():
    img = gradient_bg()
    img = add_vignette(img)
    draw = ImageDraw.Draw(img)
    brand_header(img, draw)
    return img, draw
