import pygame,os
#SCREEN VARIABLES
FPS=60
WIDTH,HEIGHT=600,650
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

#FONTS, MARGINS & COLORS
pygame.font.init()
font=pygame.font.SysFont("Times New Roman",35)
border=10
tile_width=50
margin_left=75
margin_top=50
default_number_color=(0,0,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
ONE=1073741913
NINE=1073741921
#BOARD
board=[[1]*9 for i in range(9)]

def playerInput(Xpos,Ypos):
    i,j=Ypos-1,Xpos-1
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    return
            if event.type==pygame.KEYDOWN:
                #default value condition
                
                if(event.key==pygame.K_0 or event.key==pygame.K_KP0):
                    board[i][j]=int(event.unicode)
                    pygame.draw.rect(WINDOW, WHITE, (25+Xpos*tile_width+5,Ypos*tile_width+5
                                                     ,50-border-5,50-border-5))
                    pygame.display.update()
                if(ONE<=event.key<=NINE):
                    print("between 0 and 1")
                    pygame.draw.rect(WINDOW, WHITE, (25+Xpos*tile_width+5,Ypos*tile_width+5
                                                     ,50-border-5,50-border-5))
                    data=font.render(event.unicode,True, BLACK)
                    WINDOW.blit(data,(42+Xpos*tile_width,Ypos*tile_width+5))
                    board[i][j]=int(event.unicode)
                    pygame.display.update()
                    return
                return

def fillBoard():
    for i in range(9):
        for j in range(9):
            data=font.render(str(board[i][j]), True, default_number_color ,None)
            WINDOW.blit(data,((j+1)*tile_width+42,(i+1)*tile_width+5))        
def drawBoard():
    WINDOW.fill((WHITE))
    for i in range(10):
        if i%3==0:
            #Individual Square borders
            pygame.draw.line(WINDOW, BLACK, (margin_left+tile_width*i,margin_top), 
                         (margin_left+tile_width*i,500), width=4)
            pygame.draw.line(WINDOW, BLACK, (margin_left,tile_width*i+margin_top), 
                         (525,margin_top+tile_width*i), width=4)
    
        pygame.draw.line(WINDOW, BLACK, (margin_left+tile_width*i,margin_top), 
                         (margin_left+tile_width*i,500), width=2)
        pygame.draw.line(WINDOW, BLACK, (margin_left,tile_width*i+margin_top), 
                         (525,margin_top+tile_width*i), width=2)
        
    fillBoard()
    
    pygame.display.update()

#Game Main Function
def main():
    pygame.init()
    clock=pygame.time.Clock()
    run=True
    drawBoard()
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=pygame.mouse.get_pos()
                playerInput((x-25)//tile_width,y//tile_width)
        
    pygame.quit()

if __name__=="__main__":
    main()