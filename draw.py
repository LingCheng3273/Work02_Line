from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    #first quadrant
    if x1 >= x0 and y1 >= y0:
        if y1 - y0 <= x1 - x0:   #first octant
            draw_line_1(x0, y0, x1, y1, screen, color)
        else:   #second octant
            draw_line_2(x0, y0, x1, y1, screen, color)
    #second quadrant
    elif x1 <= x0 and y1 >= y0:
        if y1 - y0 >= x1 - x0:   #third octant
            draw_line_7(x1, y1, x0, y0, screen, color)
        else:   #fourth octant
            draw_line_8(x1, y1, x0, y0, screen, color)
    #third quadrant
    elif x1 <= x0 and y1 <= y0:   
        if x1 - x0 >= y1 - y0:   #fifth octant
            draw_line_1(x1, y1, x0, y0, screen, color)
        else:   #sixth octant
            draw_line_2(x1, y1, x0, y0, screen, color)
    #fourth quadrant
    else:
        if x1 - x0 <= y1 - y0: #seventh octant
            draw_line_7( x0, y0, x1, y1, screen, color )
        else: #eighth octant
            draw_line_8( x0, y0, x1, y1, screen, color )
    


#draws in octant 1
def draw_line_1( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2 * A + B
    B = 2 * B
    A = 2 * A
    while (x < x1):
        plot(screen, color, x, y)
        if d > 0:
            y = y + 1
            d = d + B
        x = x + 1
        d = d + A

#draws in octant 2
#midpoint (x+.5, y+1)
def draw_line_2( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = A + 2 * B
    B = 2 * B
    A = 2 * A
    while (y < y1):
        plot(screen, color, x, y)
        if d < 0:
            x = x + 1
            d = d + A
        y = y + 1
        d = d + B

#draws in octant 7
#midpoint (x+.5, y-1)
def draw_line_7( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = A - 2 * B
    B = 2 * B
    A = 2 * A
    while (y > y1):
        plot(screen, color, x, y)
        if d > 0:
            x = x + 1
            d = d + A
        y = y - 1
        d = d - B

#draws in octant 8
#(x+.5, y-1)
def draw_line_8( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    d = 2 * A + B
    B = 2 * B
    A = 2 * A
    while (x < x1):
        plot(screen, color, x, y)
        if d < 0:
            y = y - 1
            d = d - B
        x = x + 1
        d = d + A
