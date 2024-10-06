# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab7A.py
import pygame, sys
from pygame.locals import *
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
sRed, sGreen, sBlue = 0, 0, 0
increase = True
while True:
    if (sRed, sGreen, sBlue)==(255,255,255):
        increase = False
    if increase:
        sRed += 1 if sRed!=255 else 0
        sGreen += 1 if sGreen!=255 and sRed==255 else 0
        sBlue += 1 if sBlue!=255 and sGreen==255 else 0
    else:
        sRed -= 1 if sRed!=0 else 0
        sGreen -= 1 if sGreen!=0 and sRed==0 else 0
        sBlue -= 1 if sBlue!=0 and sGreen==0 else 0
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    screen.fill(color=(sRed, sGreen, sBlue))
    pygame.display.flip()
    clock.tick(60)