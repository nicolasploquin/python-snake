# Snake Tutorial Python

# Step 2 - Snake movements

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
    def __init__(self,start,color=(255,0,0)):
        self.pos = start
        self.color = color

       
    # def move(self, dirnx, dirny):
    #     pass
 
    def draw(self, eyes=False):
        (col,row) = self.pos
        pygame.draw.rect(surface, self.color, (col*row_height+1, row*row_height+1, row_height-1, row_height-1))
 
 
class Snake(object):
    body = []

    def __init__(self, color, pos, dir=(0,1) ):
        self.color = color
        self.head = Cube(pos)
        self.body.insert(0, self.head)
        self.dir = dir

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dir = (-1,0)
                elif keys[pygame.K_RIGHT]:
                    self.dir = (1,0)
                elif keys[pygame.K_UP]:
                    self.dir = (0,-1)
                elif keys[pygame.K_DOWN]:
                    self.dir = (0,1)
 
        (i,j) = self.body[0].pos
        i = (i + self.dir[0]) % rows_count
        j = (j + self.dir[1]) % rows_count

        head = Cube((i,j))
        self.body.insert(0, head)
        del self.body[-1]
 
    def reset(self, pos):
        pass
 
    def addCube(self):
        pass
 
    def draw(self):
        for i,cube in enumerate(self.body):
            if i == 0:
                cube.draw(True)
            else:
                cube.draw()
 
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
    snake.draw()
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
        snake.move()
        redrawWindow()
 
main()