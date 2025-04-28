import pgzrun
import random
WIDTH = 1000
HEIGHT = 800
CENTREX = WIDTH/2
CENTERY = HEIGHT/2
CENTER = (CENTREX,CENTERY)
FINLEVEL = 6
STARTSPEED = 10

ITEMS = ["paperbag", "plasticbag", "bottle", "glass", "tire","battery" ]
gameover = False
gamecomplete = False
currentlevel = 1
ITEMS2 = []
Anims = []

def draw():
    global gameover, currentlevel, gamecomplete, ITEMS2
    screen.clear()
    screen.blit("backroundrecycle", (0,0))

    if gameover:
        displaymessage("you lost", "get better")
    elif gamecomplete:
        displaymessage("nice", "you did it")

    for i in ITEMS2:
        i.draw()

def update():
    global ITEMS2
    if len(ITEMS2) == 0:
        ITEMS2 = make_items(currentlevel)    

def getoptiontotake(extraitems):
    ITEMS2CREATE =["paperbag"]
    for i in range(0,extraitems):
        randomoption = random.choice(ITEMS)
        ITEMS2CREATE.append(randomoption)
    return ITEMS2CREATE
def createitems(ITEMS2CREATE):
    newitems = []
    for i in ITEMS2CREATE:
        newitems.append(Actor(i))
    return newitems

def layoutitems(ITEMS2LAYOUT):
    gap = len(ITEMS2LAYOUT) + 1
    gapsize = WIDTH/gap 
    random.shuffle(ITEMS2LAYOUT)
    for i, item in enumerate(ITEMS2LAYOUT):
        newx = (i + 1)*gapsize
        item.x = newx

def animitems(ITEM2ANIMATE):
    global Anims
    for i in Anims:
        duration = STARTSPEED - currentlevel
        i.anchor = ("center","bottom")
        anim = animate(i,duration = duration, on_finished = handle_gameover, y = HEIGHT)
        Anims.append(anim)
def handle_gameover():
    global gameover
    gameover = True	

def make_items(numitems):
    itemcreate = getoptiontotake(numitems)
    newitem = createitems(itemcreate)
    layoutitems(newitem)
    animitems(newitem)
    return newitem


def on_mouse_down(pos):
    global ITEMS, currentlevel
    for i in ITEMS:
        if i.collidepoint(pos):
            if "paperbag" in i.image:
                handle_gamecomplete()
            else:
                handle_gameover()

def handle_gamecomplete():
    global currentlevel, ITEMS, Anims, gamecomplete
    stopanimations(Anims)
    if currentlevel == FINLEVEL:
        gamecomplete = True
    else:
        currentlevel += 1
        ITEMS.truncate()
        Anims.truncate()

def stopanimations(anim):
    for i in anim:
        if i.running:
            i.stop()
def displaymessage(heading, subheading):
    screen.draw.text(heading, fontsize = 20, color = "black", center = CENTER)
    screen.draw.text(subheading, fontsize = 14, color = "white", center = (CENTREX, CENTERY + 20))

pgzrun.go()
