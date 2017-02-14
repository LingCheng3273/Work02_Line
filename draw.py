from display import *

#draws in octant 1
def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2 * A + B
    B = 2 * B
    A = 2 * A
    while (x <= x1):
        plot(screen, color, x, y)
        if d > 0:
            y = y + 1
            d = d + B
        x = x + 1
        d = d + A

#draws in octant 2
def draw_line_2( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2 * A + B
    B = 2 * B
    A = 2 * A
    while (y <= y1):
        plot(screen, color, x, y)
        if d < 0:
            x = x + 1
            d = d + A
        y = y + 1
        d = d + B
