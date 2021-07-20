import numpy as np
import pygame as py
import os

board = [["r","n","b","q","k","b2","n2","r2"],
["p","p2","p3","p4","p5","p6","p7","p8"],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["P","P2","P3","P4","P5","P6","P7","P8"],
["R","N","B","Q","K","B","N","R"]]

def createBoard(screen,size):  
    width, height = size
    fieldW = (height-200)/8
    olive = (66,70,50)
    white = (247,234,223)
    x =0
    y =0
    for i in range(8):
        for g in range(0,8):
            x = 100+g*fieldW
            y=  100+i*fieldW
            bounds = py.Rect(x,y,fieldW,fieldW)
            currFig = board[i][g]
            
            if((i+g)%2): ## draw green rects
                py.draw.rect(screen, olive, bounds)
            else: ## draw white rects
                py.draw.rect(screen, white, bounds)

            ## draw figures
            if(currFig!= ""):
                if (currFig[0].isupper()):    
                    img = py.image.load(os.path.join('Images','b', currFig[0]+'.png'))
                else:
                    img = py.image.load(os.path.join('Images','w', currFig[0]+'.png'))

                img = py.transform.scale(img,(int(fieldW),int(fieldW)))
                screen.blit(img, (x,y,fieldW,fieldW))
    
    img = py.image.load(os.path.join('Images','blank.png'))
    img = py.transform.scale(img,(int(fieldW),int(fieldW)))
    screen.blit(img, (x,y,fieldW,fieldW))
    py.display.update()
    return board

