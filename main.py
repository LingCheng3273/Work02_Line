from display import *
from draw import *

screen = new_screen()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
white = [255, 255, 255]

for i in range(6):
    draw_line(0, 0, 500, i*100, screen, red)
    draw_line(0, 0, i*100, 500, screen, red)
    draw_line(500, 500, 0, i*100, screen, blue)
    draw_line(500, 500, i*100, 0, screen, blue)
    draw_line(500, 0, i*100, 500, screen, green)    
    draw_line(500, 0, 0, i*100, screen, green)
    draw_line(0, 500, i*100, 0, screen, white)
    draw_line(0, 500, 500, i*100, screen, white)
    
display(screen)
save_extension(screen, 'img.png')
