from GUI.board import createBoard
import sys
import pygame as py
## animate moving an piece on board
def movePiece(screen,board,startPos,EndPos):
    for x in range(100):                   #animate 100 frames
        screen.blit(background, position, position) #erase
        position = position.move(2, 0)     #move player
        screen.blit(player, position)      #draw new player
        py.display.update()            #and show it all
        py.time.delay(100)   
## capture a piece
def capturePiece(screen, board,startPos,EndPos):
    pass

class  actionListner:
    def __init__(self):
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
                ## mouse moving
                if event.type == py.MOUSEMOTION:
                    #py.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                    #posx = event.pos[0]
                    pass
                ## mouse release
                if event.type == py.MOUSEBUTTONDOWN:
                    pass
                
        sys.exit()

