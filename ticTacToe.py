import pygame, sys
import numpy as np

pygame.init()

width, height = 600, 600
background_colour = (255,255,255)
line_colour = (0,0,0)
square_size = 200
padding = 50
line_width_plus_fifteen = 15
BLACK = (0,0,0)
line_width = 10
circle_radius = 60
circle_width = 15
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('Tic Tac Toe')
screen.fill(background_colour)

board = np.zeros((3,3))


def draw_players():
  for i in range(3):
    for j in range(3):
      if board[i][j] == 1:
        pygame.draw.circle(screen, BLACK,(int(j * 200 + 100),int(i * 200 + 100)),circle_radius,circle_width )
      elif board[i][j] == 2:
        pygame.draw.line(screen, BLACK, (j * square_size + padding, i * square_size + square_size - padding), (j * square_size + square_size -padding, i * square_size +padding), line_width_plus_fifteen)
        pygame.draw.line(screen, BLACK, (j * square_size + padding, i * square_size+ padding), (j * square_size + square_size -padding, i * square_size + square_size -padding), line_width_plus_fifteen)  
          
          
            

def drawLines():
	pygame.draw.line(screen,line_colour,(0,200),(600,200),line_width)
	pygame.draw.line(screen,line_colour,(0,400),(600,400),line_width)
	pygame.draw.line(screen,line_colour,(200,0),(200,600),line_width)
	pygame.draw.line(screen,line_colour,(400,0),(400,600),line_width)

def markSquare(x,y,player):
    board[x][y] = player


def availableSqare(x,y):
  if board[x][y] == 0:
    return True
  else:
    return False 

def isFull():
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        return False
  return True      


def col_win():
    cw = False
      # player one has a col win
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
      pygame.draw.line(screen, BLACK,(100,0), (100,600),line_width_plus_fifteen)
      cw = True
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
      pygame.draw.line(screen, BLACK,(300,0), (300,600),line_width_plus_fifteen)
      cw = True
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
      pygame.draw.line(screen, BLACK,(500,0), (500,600),line_width_plus_fifteen)
      cw = True

    # player two has a col win  
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
      pygame.draw.line(screen, BLACK,(100,0), (100,600),line_width_plus_fifteen)
      cw = True
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
      pygame.draw.line(screen, BLACK,(300,0), (300,600),line_width_plus_fifteen)
      cw = True
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
      pygame.draw.line(screen, BLACK,(500,0), (500,600),line_width_plus_fifteen)
      cw = True
    return cw  


def diag_win():
  dw = False
  if board[0][0] == 1 and board[1][1] == 1 and board[2][2] ==1:
    pygame.draw.line(screen, BLACK, (0,0),(600,600),line_width_plus_fifteen)
    dw = True
  elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] ==2:   
    pygame.draw.line(screen, BLACK, (0,0),(600,600),line_width_plus_fifteen)
    dw = True
  elif board[2][0] == 1 and board[1][1] == 1 and board[0][2] ==1:
    pygame.draw.line(screen, BLACK, (0,600),(600,0),line_width_plus_fifteen)   
    dw = True
  elif board[2][0] == 2 and board[1][1] == 2 and board[0][2] ==2:
    pygame.draw.line(screen, BLACK, (0,600),(600,0),line_width_plus_fifteen)   
    dw = True  

  return dw  

def row_win():
    # player one has a row win
    rw = False
    if board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
      pygame.draw.line(screen, BLACK,(0,100), (600,100),line_width_plus_fifteen)
      rw = True
    elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
      pygame.draw.line(screen, BLACK,(0,300), (600,300),line_width_plus_fifteen)
      rw = True
    elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
      pygame.draw.line(screen, BLACK,(0,500), (600,500),line_width_plus_fifteen)
      rw = True

    # player two has a row win  
    elif board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
      pygame.draw.line(screen, BLACK,(0,100), (600,100),line_width_plus_fifteen)
      rw = True
    elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
      pygame.draw.line(screen, BLACK,(0,300), (600,300),line_width_plus_fifteen)
      rw = True
    elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
      pygame.draw.line(screen, BLACK,(0,500), (600,500),line_width_plus_fifteen)
      rw = True
    return rw    





drawLines()


player = 1

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONUP:
      if col_win() or row_win() or diag_win():
        running = False
        break
      pos = event.pos
      print(pos)

      clickedRow = int(pos[1]// square_size)
      clickedCol = int(pos[0] // square_size)
  
      if availableSqare(clickedRow,clickedCol):
        if player == 1:
          markSquare(clickedRow,clickedCol,player)
          player = 2
        elif player == 2:
          markSquare(clickedRow,clickedCol,player)
          player = 1
        draw_players() 

              
  pygame.display.update()

