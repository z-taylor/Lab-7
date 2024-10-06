# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab7C.py
import pygame, sys
from pygame.locals import *
pygame.init()
width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
sRed, sGreen, sBlue = 0, 0, 0
screen.fill((sRed, sGreen, sBlue))
topRect, bottomRect = pygame.Rect(0, 0, 100, 100), pygame.Rect(0, 400, 100, 100)
surf1, surf2 = pygame.Surface((topRect.width, topRect.height)), pygame.Surface((bottomRect.width, bottomRect.height))
surf1.fill((0, 255, 0))
surf2.fill((0, 0, 255))
screen.blit(surf1, (topRect.x, topRect.y))
screen.blit(surf2, (bottomRect.x, bottomRect.y))
pygame.display.flip()
flag = True
while True:
    screen.fill((sRed, sGreen, sBlue))
    if flag:
        topRect = topRect.move(5, 0)
        bottomRect = bottomRect.move(5, 0)
        flag = False if topRect.x==900 else True
    else:
        topRect = topRect.move(-5, 0)
        bottomRect = bottomRect.move(-5, 0)
        flag = True if topRect.x==0 else False
    screen.blit(surf1, (topRect.x, topRect.y))
    screen.blit(surf2, (bottomRect.x, bottomRect.y))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    clock.tick(60)