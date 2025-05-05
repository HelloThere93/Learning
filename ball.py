import pgzrun

WIDTH = 500
HEIGHT = 500

ball = Rect((150,400), (30,30))
bat = Rect((200,480), (60, 20))
speedx = 2
speedy = 2

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(bat, "gray")

def update():
    global speedx, speedy
    ball.x += speedx
    ball.y += speedy
    if ball.colliderect(bat):
        speedy = -speedy
    if ball.right > WIDTH or ball.left < 0:
        speedx = -speedx
    if ball.top < 0:
        speedy = -speedy
    if ball.bottom > HEIGHT:
        exit()
    if (keyboard.right):
        bat.x += 2
    if (keyboard.left):
        bat.x -= 2

pgzrun.go()
