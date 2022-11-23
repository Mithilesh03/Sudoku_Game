import pygame,os
#SCREEN VARIABLES
FPS=60
WIDTH,HEIGHT=600,650
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")

#FONTS and MARGINS
pygame.font.init()
font=pygame.font.SysFont("Times New Roman",35)
tile_width=50
margin_left=75
margin_top=50
default_number_color=(0,0,80)

#BOARD
board=[[1]*9 for i in range(9)]



def fillBoard():
    for i in range(9):
        for j in range(9):
            data=font.render(str(board[i][j]), True, default_number_color ,None)
            WINDOW.blit(data,((j+1)*tile_width+42,(i+1)*tile_width+5))        
def drawBoard():
    WINDOW.fill((255,255,255))
    for i in range(10):
        if i%3==0:
            #Individual Square borders
            pygame.draw.line(WINDOW, (0,0,0), (margin_left+tile_width*i,margin_top), 
                         (margin_left+tile_width*i,500), width=4)
            pygame.draw.line(WINDOW, (0,0,0), (margin_left,tile_width*i+margin_top), 
                         (525,margin_top+tile_width*i), width=4)
    
        pygame.draw.line(WINDOW, (0,0,0), (margin_left+tile_width*i,margin_top), 
                         (margin_left+tile_width*i,500), width=2)
        pygame.draw.line(WINDOW, (0,0,0), (margin_left,tile_width*i+margin_top), 
                         (525,margin_top+tile_width*i), width=2)
        
    fillBoard()
    
    pygame.display.update()

def main():
    clock=pygame.time.Clock()
    run=True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        drawBoard()
    pygame.quit()

if __name__=="__main__":
    main()