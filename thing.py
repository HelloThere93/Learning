import pgzrun
import pygame
from random import randint

WIDTH = 500  
HEIGHT = 500

txt = "Click the Alien first!"

Alien = Actor("alien")
Lightsaber = Actor("lightsaber")

current_target = "alien"

def draw():
    screen.clear()
    screen.fill(color=(100, 50, 180))
    Alien.draw()
    Lightsaber.draw()
    screen.draw.text(txt, center=(250, 180), fontsize=18, color="silver")

def alienpos():
    Alien.x = randint(20, 480)
    Alien.y = randint(20, 480)

def saberpos():
    Lightsaber.x = randint(20, 480)
    Lightsaber.y = randint(20, 480)

def on_mouse_down(pos):
    global txt, current_target
    if current_target == "alien" and Alien.collidepoint(pos):
        txt = "Now click the Lightsaber!"
        alienpos()
        current_target = "lightsaber"
    elif current_target == "lightsaber" and Lightsaber.collidepoint(pos):
        txt = "Well done! Now start again."
        saberpos()
        current_target = "alien"
    else:
        txt = "Missed! Try again."

pgzrun.go()
alienpos()
saberpos()
