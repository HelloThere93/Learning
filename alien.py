import pgzrun
import pygame
from random import randint
WIDTH=500  
HEIGHT=500
txt = ""

Alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color = (100,50,180))

    Alien.draw()
    
    screen.draw.text(txt, center = (250, 180), fontsize= 18, color = "silver")

def alienpos():
    Alien.x = randint(20,480)
    Alien.y = randint(20,480)

def on_mouse_down(pos):
    
    global txt
    if Alien.collidepoint(pos):
        txt = "Shot on target"
        alienpos()
    else:
        txt = "Missed "
    

pgzrun.go()
alienpos()