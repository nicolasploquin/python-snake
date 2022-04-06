# Snake Tutorial Python

import math
import random
import pygame

from tkinter import messagebox, Tk

class Cube(object):
    def __init__(self,start,color=(255,0,0)):
        pass

    def draw(self, eyes=False):
        pass
 
class Snake(object):

    def __init__(self, color, pos, dir=(0,1) ):
        pass

    def move(self):
        pass
 
    def reset(self, pos):
        pass
 
    def draw(self):
        pass
 
def drawGrid():
    
    pygame.draw.line(surface, (255,255,255), (0,25), (500,25) )
    pygame.draw.line(surface, (255,255,255), (0,50), (500,50) )

    for num in range(20):
        pygame.draw.line(surface, (255,255,255), (0,num*25), (500,num*25) )
        pygame.draw.line(surface, (255,255,255), (num*25,0), (num*25,500) )
    
 
def redrawWindow():

    drawGrid()
    pygame.display.update()
 
def randomSnack():
    pass
 
def message_box(subject, content):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
 
def main():
    global surface

    pygame.init()
    pygame.display.set_caption('Snake Python')
    
    surface = pygame.display.set_mode((500,500)) #(width, height)

    running = True

    clock = pygame.time.Clock()
    
    while running:
        clock.tick(10)
        redrawWindow()
        
 
main()