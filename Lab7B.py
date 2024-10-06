# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Lab7B.py
import pygame, sys
from pygame.locals import *
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
sRed, sGreen, sBlue = 0, 0, 0
screen.fill(color=(sRed, sGreen, sBlue))
tlRect, trRect, blRect, brRect, midRect = pygame.Rect(0, 0, 60, 60), pygame.Rect(540, 0, 60, 60), pygame.Rect(0, 540, 60, 60), pygame.Rect(540, 540, 60, 60), pygame.Rect(270, 270, 60, 60)
surf1, surf2, surf3, surf4, surf5 = pygame.Surface((tlRect.width, tlRect.height)), pygame.Surface((tlRect.width, tlRect.height)), pygame.Surface((tlRect.width, tlRect.height)), pygame.Surface((tlRect.width, tlRect.height)), pygame.Surface((tlRect.width, tlRect.height))
rectColor = (255, 0, 0)
surf1.fill((rectColor))
surf2.fill((rectColor))
surf3.fill((rectColor))
surf4.fill((rectColor))
surf5.fill((rectColor))
screen.blit(surf1, (tlRect.x, tlRect.y))
screen.blit(surf2, (trRect.x, trRect.y))
screen.blit(surf3, (blRect.x, blRect.y))
screen.blit(surf4, (brRect.x, brRect.y))
screen.blit(surf5, (midRect.x, midRect.y))
pygame.display.flip()
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
    clock.tick(60)