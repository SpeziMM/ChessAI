from GUI.board import createBoard
import pygame as py
import sys



def main():
    py.init()
    infoObject = py.display.Info()
    running = True
    width, height = infoObject.current_w, infoObject.current_h
    screen = py.display.set_mode((width,height),py.RESIZABLE)
    py.display.update()
    createBoard(screen,(width, height))

    while running:
        ## bei einem pygame event: ...
        for event in py.event.get():
            if event.type == py.QUIT:
                ##setup board
                running = False
                break
            if  event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False
                    break
            
    sys.exit()
                
if __name__ == '__main__':
    main()