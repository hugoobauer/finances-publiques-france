"""Generate the « Mille milliards » logo: 9 × 9 grid, filled from the bottom,
6 full rows minus 2 squares on the right; 3 × 3 version (2 rows minus 1) under 24 px.
Spec: fr/conception/03-identite-visuelle.md §2. Usage: python3 research/scripts/make_logo.py"""

def grid(n, filled, css=True, small=False):
    cell, gap = (8.4, 1.4) if small else (2.6, 0.6)
    off = (32 - (n * cell + (n - 1) * gap)) / 2
    rx = 1.2 if small else 0.45
    sw_white = 0.7 if small else 0.3
    fixed = {'b': '#0055A4', 'w': '#FFFFFF', 'r': '#EF4135', 'e': '#E6E4DD', 'wl': '#A9A79F'}
    out = []
    for rb in range(n):            # row counted from the bottom
        for c in range(n):
            on = rb * n + c < filled
            band = 'brw'[0] if c < n // 3 else ('w' if c < 2 * n // 3 else 'r')
            band = 'b' if c < n // 3 else band
            x = off + c * (cell + gap)
            y = off + (n - 1 - rb) * (cell + gap)
            k = band if on else 'e'
            sw = sw_white if k == 'w' else 0   # inset stroked cells so all gaps stay equal
            attrs = f'x="{x + sw/2:.2f}" y="{y + sw/2:.2f}" width="{cell - sw:.2f}" height="{cell - sw:.2f}" rx="{rx}"'
            if css:
                out.append(f'<rect class="lg-{k}" {attrs}/>')
            else:
                fill = fixed[k]
                stroke = f' stroke="{fixed["wl"]}" stroke-width="{sw}"' if sw else ''
                out.append(f'<rect fill="{fill}"{stroke} {attrs}/>')
    return ''.join(out)

LOGO = grid(9, 6 * 9 - 2)
SMALL = grid(3, 2 * 3 - 1, small=True)

def svg(inner, size, css=True):
    a = ' aria-hidden="true"' if css else ' xmlns="http://www.w3.org/2000/svg"'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 32 32"{a}>{inner}</svg>'

CSS = (".lg-b{fill:var(--f-bleu)}.lg-r{fill:var(--f-rouge)}.lg-e{fill:var(--empty)}"
       ".lg-w{fill:var(--f-blanc);stroke:var(--f-blanc-line);stroke-width:.3}")

if __name__ == '__main__':
    open('site/public/favicon.svg', 'w').write(svg(grid(3, 5, css=False, small=True), 32, css=False) + '\n')
    open('site/public/logo.svg', 'w').write(svg(grid(9, 52, css=False), 32, css=False) + '\n')
    print('ok')
