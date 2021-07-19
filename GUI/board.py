import numpy as np
import pygame as py

board = np.zeros((8,8))

def createBoard(screen,size):  
    for i in range(8):
        for b in range(8):
            bounds = py.Rect(i*50,b*50,50,50)
            py.draw.rect(screen, py.Color("red"), bounds)
    py.display.update()
