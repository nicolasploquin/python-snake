# Snake Tutorial Python

# Step 1 - Draw grid

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
 
# Grid definition

# square screen 500x500
screen_height = 500
rows_count = 20
row_height = screen_height // rows_count

class Cube(object):
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
 
       
    def move(self, dirnx, dirny):
        pass
 
    def draw(self, surface, eyes=False):
        pass
 
 
class Snake(object):

    def __init__(self, color, pos):
        pass
 
    def move(self):
        pass
 
    def reset(self, pos):
        pass
 
    def addCube(self):
        pass
 
    def draw(self, surface):
        pass
 
def drawGrid():
    x = 0
    y = 0
    for l in range(rows_count):
        x = x + row_height
        y = y + row_height

        pygame.draw.line(surface, (96,96,96), (x, 0), (x, screen_height))
        pygame.draw.line(surface, (96,96,96), (0, y), (screen_height, y))
 
def redrawWindow():
    surface.fill((0,0,0))
    drawGrid()
    pygame.display.update()
 
def randomSnack(rows, item):
 
    pass
 
 
def message_box(subject, content):
    pass
 
 
def main():
    global surface, snake

    pygame.init()
    pygame.display.set_caption('Snake Python')
    
    surface = pygame.display.set_mode((screen_height, screen_height)) #(width, height)
    snake = Snake((0,0,255), (10,10))
    running = True

    clock = pygame.time.Clock()
    
    while running:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow()
 
main()