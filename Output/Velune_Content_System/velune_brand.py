"""Socle visuel Velune — mode éditorial « Luxury / Beauty » (standard brandkit).

Principes appliqués : aplat + grain d'impression (pas de dégradé décoratif),
grille explicite, filets fins comme système d'alignement (pas de cartes ni
d'ombres), typographie serif sparse, micro-labels, respiration large.
"""
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1080

# Palette — un dominant, deux accents, des neutres. Rien d'autre.
IVORY = (247, 242, 236)        # aplat de fond
STONE = (214, 203, 194)        # neutre froid, filets secondaires
ROSE = (232, 205, 202)
BURGUNDY = (94, 38, 46)        # accent principal (texte fort)
GOLD = (176, 137, 92)          # accent secondaire (filets, labels)
INK = (46, 38, 38)             # texte courant
MUTED = (132, 118, 114)        # texte tertiaire, sources

# Serifs TrueType exploitables par PIL (Charter n'existe qu'en Type1 → illisible ici)
F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
F_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
F_ITAL = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"

# Grille : marges larges, une gouttière centrale
MARGIN = 110
COL_GAP = 64
COL_W = (W - 2 * MARGIN - COL_GAP) / 2


def font(path, size):
    return ImageFont.truetype(path, size)


def text_size(draw, s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0], b[3] - b[1], b


def paper_ground(seed=7):
    """Aplat ivoire + grain fin. Remplace dégradé + vignette."""
    img = Image.new("RGB", (W, H), IVORY)
    rnd = random.Random(seed)
    noise = Image.new("L", (W // 2, H // 2))
    noise.putdata([rnd.gauss(128, 11) for _ in range((W // 2) * (H // 2))])
    noise = noise.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(0.4))
    grain = Image.merge("RGB", (noise, noise, noise))
    return Image.blend(img, grain, 0.055)


def rule(draw, x0, y, x1, color=STONE, width=1):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def vrule(draw, x, y0, y1, color=STONE, width=1):
    draw.line([(x, y0), (x, y1)], fill=color, width=width)


def tracked(draw, xy, s, f, fill, track=6):
    """Texte avec interlettrage manuel — PIL ne gère pas le letter-spacing."""
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        cw = draw.textlength(ch, font=f)
        x += cw + track
    return x - track


def tracked_width(draw, s, f, track=6):
    if not s:
        return 0
    return sum(draw.textlength(c, font=f) for c in s) + track * (len(s) - 1)


def label_caps(draw, xy, s, fill=GOLD, size=21, track=6):
    """Petite capitale espacée — label de section."""
    return tracked(draw, xy, s.upper(), font(F_SANS, size), fill, track)


def para(draw, x, y, text, f, fill, max_w, leading):
    """Paragraphe aligné à gauche. Retourne le y final."""
    for line in wrap_to_width(draw, text, f, max_w):
        draw.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def wrap_to_width(draw, text, f, max_width):
    lines, cur = [], ""
    for w in text.split():
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=f) <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def moon_icon(size=13, color=GOLD):
    s = size * 4
    icon = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(icon)
    d.ellipse([0, 0, s - 1, s - 1], fill=color + (255,))
    cut = int(s * 0.40)
    d.ellipse([cut, -1, cut + s, s], fill=(0, 0, 0, 0))
    return icon.resize((size, size), Image.LANCZOS)


def brand_header(img, draw):
    """Monogramme + wordmark serif, discret, aligné sur la marge gauche."""
    m = moon_icon(17, GOLD)
    img.paste(m, (MARGIN, MARGIN - 46), m)
    f = font(F_SERIF, 22)
    draw.text((MARGIN + 28, MARGIN - 50), "Velune", font=f, fill=BURGUNDY)


def footer_mark(img, draw, index=None):
    """Filet de pied + micro-label. Le « page-number detail » de brandkit."""
    y = H - MARGIN + 26
    rule(draw, MARGIN, y, W - MARGIN, STONE, 1)
    f = font(F_MONO, 15)
    draw.text((MARGIN, y + 16), "VELUNE", font=f, fill=MUTED)
    if index:
        w = draw.textlength(index, font=f)
        draw.text((W - MARGIN - w, y + 16), index, font=f, fill=MUTED)


def base_canvas(index=None):
    img = paper_ground()
    draw = ImageDraw.Draw(img)
    brand_header(img, draw)
    footer_mark(img, draw, index)
    return img, draw
