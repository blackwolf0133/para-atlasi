"""Para Atlası profil resmi (1080x1080): Kuruş maskotu."""
import math, cairo
from engine import draw as D, theme_para as T
from engine.props_para import draw_coin

S = 1080

def bg(ctx):
    ctx.rectangle(0, 0, S, S); ctx.set_source_rgb(*T.EMERALD_2); ctx.fill()
    cx, cy = S / 2, S * 0.45
    for i in range(22):
        a1 = 0.1 + i * 2 * math.pi / 22; a2 = a1 + math.pi / 22
        ctx.move_to(cx, cy); ctx.line_to(cx + math.cos(a1) * 1200, cy + math.sin(a1) * 1200)
        ctx.line_to(cx + math.cos(a2) * 1200, cy + math.sin(a2) * 1200); ctx.close_path()
        ctx.set_source_rgb(*T.EMERALD_3); ctx.fill()
    rg = cairo.RadialGradient(cx, cy, 30, cx, cy, 600)
    rg.add_color_stop_rgba(0, *T.GOLD, 0.35); rg.add_color_stop_rgba(1, *T.GOLD, 0)
    ctx.rectangle(0, 0, S, S); ctx.set_source(rg); ctx.fill()

def ribbon(ctx, text, y):
    D.set_font(ctx, D.CAPTION_FONT, 74, bold=True)
    tw = D.text_width(ctx, text); w = tw + 90; x0 = S / 2 - w / 2
    T.rounded_rect(ctx, x0, y, w, 110, 26); D.stroke_fill(ctx, T.GOLD, T.GOLD_DARK, 6)
    ctx.set_source_rgb(*T.DARK); ctx.move_to(S / 2 - tw / 2, y + 80); ctx.show_text(text)

def make(path, with_text):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, S, S); ctx = cairo.Context(surf); bg(ctx)
    for (x, y, r, ph) in ((170, 250, 55, 0.3), (900, 300, 45, 1.2), (150, 760, 40, 2.0), (930, 740, 60, 0.8)):
        draw_coin(ctx, x, y, r, ph, spin=False)
    scale = 3.0 if with_text else 3.3
    head_y = 400 if with_text else 450
    y = head_y + (D.N_ULEG + D.N_LLEG + D.N_TORSO + D.N_HEAD - 6) * D.GLOBAL_SCALE * scale
    j = D.draw_narrator(ctx, S / 2 - 20, y, scale, D.NARRATOR_POSES["wave"], "wink", 0.5, False, "none", 1.0, 1.0)
    ex, ey = j["eye_l"]
    D.draw_sparkle(ctx, ex - j["head_r"] * 1.0, ey - j["head_r"] * 0.6, 80, 0.15)
    if with_text:
        ribbon(ctx, "PARA ATLASI", 800)
    surf.write_to_png(path)

make("output/profil_para_atlasi_A.png", False)
make("output/profil_para_atlasi_B_yazili.png", True)
