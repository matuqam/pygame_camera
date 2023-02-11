from typing import List, Dict, Tuple

import pygame
from pygame.locals import *

import engine
from engine import *


SCREEN_SIZE = (800, 600)
DISPLAY_SIZE = (600, 450)

pygame.init()
display = pygame.display.set_mode(SCREEN_SIZE)
camera = Camera(display)
engine.camera = camera

# Protagonist is controlled
protagonist = Entity(Rect(0,0, 16, 16), color=(250,250,250))
statics = []
for i in range(20):
    statics.append(Entity(Rect(i*20,i*20, 16, 16), parallax=0.5, color=(250,150,150)))

elements = statics + [protagonist]

def main_loop():
    while True:
        for event in pygame.event.get():
            EventManager.manage_event(event, protagonist)
        
        camera.move()
        camera.shake()
        protagonist.move()

        display.fill(color=(150,150,150))

        for element in sorted(elements, key=lambda e: e.parallax, reverse=False):
            pygame.draw.rect(camera.surface, color=element.color, rect=camera_draw(camera, element.rect, element.parallax))

        pygame.display.update()


main_loop()
