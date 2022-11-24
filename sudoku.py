import pygame,os
import requests
import numpy as np
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
default_number_color=(255,165,0)
BLACK=(0,0,0)
WHITE=(255,255,255)
CYAN=(80,100,100)
RED=(255,0,0)
GREEN=(0,255,0)

ONE=1073741913
NINE=1073741921

#BOARD
ans=[]
response=requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
""" board=[[1]*9 for i in range(9)] #for testing purposes
board[0][0]=0 """

board=response.json()['board']

""" board= [
  [ 0, 0, 0,  0, 7, 0,  0, 8, 0 ],
  [ 2, 7, 4,  9, 0, 8,  0, 0, 5 ], 
  [ 0, 0, 5,  0, 1, 0,  2, 7, 0 ],

  [ 0, 0, 0,  4, 0, 0,  0, 6, 7 ],
  [ 0, 0, 2,  0, 8, 0,  0, 5, 4 ],
  [ 7, 4, 0,  5, 0, 0,  9, 0, 0 ],

  [ 5, 0, 9,  1, 4, 0,  0, 0, 8 ],
  [ 3, 0, 1,  8, 9, 0,  0, 4, 2 ],
  [ 0, 8, 0,  3, 0, 2,  1, 9, 6 ],
] """
org_board=[[board[x][y] for y in range(9)] for x in range(9)]

def verify():
    for i in range(0,len(ans)):
        if np.array_equal(board,ans[i]):
            return True
    return False

def solve():
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == 0:
                for number in range(1,10):
                    if checker(row, column, number):
                        board[row][column] = number
                        solve()
                        board[row][column] = 0

                return
      
    #print(np.matrix(board))
    ans.append(np.matrix(board))
    #print("More possible Solutions")
class Button():
    def __init__(self,x,y,image,Scale):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image, (int(width*Scale), int(height*Scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
        
    def draw(self):
        #get the mouse position
        #draw button on screen
        WINDOW.blit(self.image,(self.rect.x,self.rect.y))
        pygame.display.update()

submit_btn_img=pygame.image.load(os.path.join('images','submit_btn.png'))
submit_btn_img.convert_alpha()
submit_button = Button(210,540,submit_btn_img,0.65)

def checker(x,y,q):
    for i in range(0,9):
        if i==y:
            continue
        if board[x][i]==q:
            return False
    for i in range(0,9):
        if i==x:
            continue
        if board[i][y]==q:
            return False
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if i==x and j==y:
                continue
            if board[i][j]==q:
                return False
    return True

def playerInput(Xpos,Ypos):
    i,j=Ypos-1,Xpos-1
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    return
            if event.type==pygame.KEYDOWN:
                #default value condition
                if(org_board[i][j]!=0):
                    return
                
                #0 value condition, Fill with empty tile
                if(event.key==pygame.K_0 or event.key==pygame.K_KP0):
                    board[i][j]=int(event.unicode)
                    pygame.draw.rect(WINDOW, WHITE, (25+Xpos*tile_width+5,Ypos*tile_width+5
                                                     ,50-border-5,50-border-5))
                    pygame.display.update()
                    
                #1<=x<=9 Input:
                if(ONE<=event.key<=NINE or 0<event.key-48<10):
                    pygame.draw.rect(WINDOW, WHITE, (25+Xpos*tile_width+5,Ypos*tile_width+5
                                                     ,50-border-5,50-border-5))
                    board[i][j]=int(event.unicode)
                    #check if the placed number is valid?
                    if checker(i,j,board[i][j]):
                        data=font.render(event.unicode,True, BLACK)
                    else:
                        data=font.render(event.unicode,True, RED)
                    
                    WINDOW.blit(data,(42+Xpos*tile_width,Ypos*tile_width+5))
                    pygame.display.update()
                    return
                return

def fillBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                continue
            #Background Colour
            """ pygame.draw.rect(WINDOW, (4,71,100), (75+j*tile_width+2.5,i*tile_width+50+3
                                                     ,50-2.5,50-3.5)) """
            data=font.render(str(board[i][j]), True, GREEN ,None)
            WINDOW.blit(data,((j+1)*tile_width+42,(i+1)*tile_width+5))
    pygame.display.update()
                    
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
        
    
    pygame.display.update()

def drawText(text,x,y,color):
    data=font.render(text, True, color ,None)
    WINDOW.blit(data,(x,y))
    pygame.display.update()

#Game Main Function
def main():
    pygame.init()
    clock=pygame.time.Clock()
    run=True
    drawBoard()
    fillBoard(board)
    solve()
    while(run):
        clock.tick(FPS)
        submit_button.draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=pygame.mouse.get_pos()
                if submit_button.rect.collidepoint((x,y)):
                    print("CLICKED")
                    count=sum([i.count(0) for i in board])
                    print(count)
                    if count==0:
                        WINDOW.fill(WHITE)
                        if verify():
                            drawText("YOU WON!!",180,275,BLACK)
                        else:
                            #result=[ans[0][i][j] for j in range(9) for i in range(9)]
                            result=ans[0].tolist().copy()
                            #print("---",board)
                            drawBoard()
                            fillBoard(result)
                            #drawText("Wrong Answer!",180,510,BLACK)
                            drawText("BETTER LUCK NEXT TIME!",90,545,BLACK)
                        
                        while True:
                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    run=False
                                    break
                            else:
                                continue
                            break                        
                else:
                    if y>=52 and x>=75 and y<=500 and x<=525:
                        playerInput((x-25)//tile_width,(y)//tile_width)
            
        
    pygame.quit()

if __name__=="__main__":
    main()