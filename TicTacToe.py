import pygame
import math
import time

pygame.init()

# Game window
width = 400
height = 500
line_color = (120,100,150)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic Tac Toe")

# Board 400x400
board_width = 400
board_height = 400
bw3 = board_width/3
bh3 = board_height/3

# Elements
line_weight = 5
mark_weight = 3
mark_color = (0,255,0)
font = pygame.font.SysFont("Arial", 15)
font2 = pygame.font.SysFont("Arial", 50, bold=True)

# initializations
win = False
draw = False
current_player = 1
click = 1
n_clicks = 0
cell_array = []
for x in range(3):
    row = [0]*3
    cell_array.append(row)

# Grid draw
def draw_grid():
    for x in range (1,3):
        vline = pygame.draw.line(screen, line_color ,(x*bw3, 15),(x*bw3, board_height-15),line_weight)
        hline = pygame.draw.line(screen,line_color, (15, x*bh3),(board_width-15, x*bh3),line_weight)

def draw_x(row,col):
    pygame.draw.line(screen, mark_color,(col*bw3 + 20, row*bh3 + 20), ((col+1)*bw3 - 20, (row+1)*bh3 - 20), mark_weight)
    pygame.draw.line(screen, mark_color,(col*bw3 + 20,(row+1)*bh3 - 20), ((col+1)*bw3 - 20, row*bh3 + 20), mark_weight )

def draw_o(row,col):
    pygame.draw.circle(screen, mark_color, (col*bw3 + bw3/2, row*bh3 + bh3/2), 0.4*bw3, mark_weight)

def cell_update(pos):
    global click
    global n_clicks
    if pos[1]>board_height:
        global current_player
        current_player *= -1
        return
    else:
        # find row, col
        row = math.floor(pos[1]/(bh3))
        col = math.floor(pos[0]/(bw3))
        # update cell array
        
        if cell_array[row][col] == 0:
            cell_array[row][col] = click
            if click == 1:
                draw_x(row,col)
            else:
                draw_o(row,col)
            click *= -1
            n_clicks += 1
        else: 
            print('try again')
   
def game_status():
    global current_player
    global win, draw
    main_diagonal_sum = 0
    sec_diagonal_sum = 0
    for i in range(3):
        main_diagonal_sum = main_diagonal_sum + cell_array[i][i]
        sec_diagonal_sum = sec_diagonal_sum + cell_array[i][3-1-i]
    
    if (abs(main_diagonal_sum) == 3):
        pygame.draw.line(screen, (255,0,0), (15,15),(board_width-15, board_height-15), 6)
        win = True
                
    elif abs(sec_diagonal_sum) == 3:
        pygame.draw.line(screen, (255,0,0), (board_width-15,15),(15, board_height-15), 6)
        win = True
        
    for col in range(3):
        col_sum = 0
        for row in range(3):
            col_sum = col_sum + cell_array[row][col]
            row_sum = sum(cell_array[row][:])
            
            if abs(row_sum) == 3:
                pygame.draw.line(screen, (255,0,0), (15,(2*(row+1)-1)*bh3/2),(board_width-15,(2*(row+1)-1)*bh3/2), 6)
                win = True
            elif abs(col_sum) == 3:
                pygame.draw.line(screen, (255,0,0), ((2*(col+1)-1)*bw3/2, 15),((2*(col+1)-1)*bw3/2,board_height-15), 6)
                win = True
                    
    if n_clicks >= 9:
        draw = True
  
def player_turn(current_player, win):
    global font
    
    if win or draw:
        
        return 
    else:
        pygame.draw.rect(screen, (0,0,0), (0, board_height,width,height-board_height))
        if current_player == 1:
            
            # player 1 - bold
            font.set_bold(True)
            player1 = font.render('Player X', True, (0,255,0))
            position1 = (15, board_height+20)
            text = screen.blit(player1, position1)
            
            # player 2 - faint
            font.set_bold(False)
            player2 = font.render('Player O', True, (0,255,0))
            position2 = (15, board_height+50)  
            screen.blit(player2, position2)
        else:
            # player 2 - bold
            font.set_bold(True)
            player2 = font.render('Player O', True, (0,255,0))
            position2 = (15, board_height+50)
            screen.blit(player2, position2)
            # player 1 - faint
            font.set_bold(False)
            player1 = font.render('Player x', True, (0,255,0))
            position1 = (15, board_height+20)
            screen.blit(player1, position1)
    
def game_result(current_player):
    global font2, win, draw
    pygame.draw.rect(screen, (0,0,0), (0, board_height,width,height-board_height))
    if win:
        if current_player == 1:
            text = font2.render("Player X wins!", True, (0,255,0))
            position = (30, 395)
            screen.blit(text, position)
            
        else:
            text = font2.render("Player O wins!", True, (0,255,0))
            position = (30, 395)
            screen.blit(text, position)
        
    elif draw:
        text = font2.render("Game Draw!", True, (255,0,0))
        position = (50, 395)
        screen.blit(text, position)
        
    
    return win, draw

def restart_game():
    global win, draw, current_player, click, n_clicks, cell_array
    # initializations
    time.sleep(3)
    screen = pygame.display.set_mode((width,height))
    win = False
    draw = False
    current_player = 1
    click = 1
    n_clicks = 0
    cell_array = []
    for x in range(3):
        row = [0]*3
        cell_array.append(row)
    
    
    draw_grid()
    player_turn(current_player,win)

draw_grid()
player_turn(current_player,win)
# Game loop
run = True
while run:
        
    # Event handllers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cell_update(pos)
                      
        if event.type == pygame.MOUSEBUTTONUP:
            game_status()
            game_result(current_player)
            if win or draw:
                pygame.display.update()
                restart_game()
            else:
                current_player *= -1
                player_turn(current_player,win)

    pygame.display.update()
pygame.quit()