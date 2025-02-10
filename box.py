import pgzrun
from random import randint

WIDTH = 1000
HEIGHT = 1000

def draw():
    r = randint(1,255)
    g = 100
    b = randint(50, 150)

    width = WIDTH - (WIDTH/10)
    height = HEIGHT - 20

    for i in range(1000):
        rectangle = Rect((0,0),(width,height))
        rectangle.center = WIDTH/2, HEIGHT/2
        screen.draw.rect(rectangle, (r,g,b))

        r -= 15
        g -= 15
        if r <= 0:
            r = randint(1,255)
        
        if g <= 0:
            g = 100
        width -= 5
        height -= 5

pgzrun.go()
