import pgzrun
from random import randint
Bullet = Actor("ufo")
WIDTH = 1200
HEIGHT = 500
ship = Actor("shootership")
EBug = Actor("bug")
Speed = 5
ship.pos = (WIDTH/2, HEIGHT - 50)
score = 0
Bullets = []
EBugs = []
direction = 1
ship.dead = False
ship.countdown = 90

def spawn_bug():

    for x in range(8):
        for y in range(4):
            
            bug = Actor("bug")
            EBugs.append(bug)
        
            EBugs[-1].x = 100 + 50 * x
            
            
            EBugs[-1].y = 100+50 *y
spawn_bug()


def GameOver():
    screen.draw.text("GAME OVER", (WIDTH/2, HEIGHT/2), fontsize = 100)
    
def on_key_down(key):
    
    if ship.dead == False:

        if key == keys.SPACE:
            Bullets.append(Bullet)
            Bullets[-1].x = ship.x
            Bullets[-1].y = ship.y-10
   
def update():
    global score, direction
    movedown = False
    if ship.dead == False:
        if keyboard.left:
            ship.x = ship.x - Speed
            if ship.x <= 0:
                ship.x = 0
        if keyboard.right:
            ship.x = ship.x + Speed
            if ship.x >= 1200:
                ship.x = 1200
    for b in Bullets:
        if b.y <= 0:
            Bullets.remove(b)
        else:
            b.y -= 7

    if len(EBugs) == 0:
        GameOver()
    
    if len(EBugs) > 0 and (EBugs[-1].x > WIDTH - 100 or EBugs[0].x < 100):
        movedown = True
        direction = direction * -1
        for bug in EBugs:
            bug.x = 5 * direction
            if movedown == True:
                bug.y += 50
            if bug.y > HEIGHT:
                EBugs.remove(bug)
            for bullet in Bullets:
                if bug.colliderect(bullet):
                    score += 1
                    Bullets.remove(bullet)
                    EBugs.remove(bug)
                    if len(EBugs) == 0:
                        GameOver()
            if bug.colliderect(ship):
                ship.dead = True
        if ship.dead:
            ship.countdown -= 1
        if ship.countdown == 0:
            ship.dead = False
            ship.countdown = 90
            

def draw():
    screen.clear()
    screen.fill("gray")
    screen.draw.text(str(score), (10,10), fontsize = 30, color ="white")
    for i in Bullets:
        i.draw()
    for v in EBugs:
        v.draw()
        
    if ship.dead == False:
        ship.draw()
    
    if len(EBugs):
        GameOver()


    
pgzrun.go()
