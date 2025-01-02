import pygame
import math

pygame.init()

# Game window
width = 400
height = 500
line_color = (120,100,150)
screen = pygame.display.set_mode((width,height))

# Board 400x400
board_width = 400
board_height = 400
bw3 = board_width/3
bh3 = board_height/3

# Elements
line_weight = 5
mark_weight = 3
mark_color = (0,255,0)
# initializations
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
    main_diagonal_sum = 0
    sec_diagonal_sum = 0
    for i in range(3):
        main_diagonal_sum = main_diagonal_sum + cell_array[i][i]
        sec_diagonal_sum = sec_diagonal_sum + cell_array[i][3-1-i]
    
    if (abs(main_diagonal_sum) == 3):
        pygame.draw.line(screen, (255,0,0), (15,15),(board_width-15, board_height-15), 6)
        return print('player wins')
        
    elif abs(sec_diagonal_sum) == 3:
        pygame.draw.line(screen, (255,0,0), (board_width-15,15),(15, board_height-15), 6)
        return print('player wins')

    for col in range(3):
        col_sum = 0
        for row in range(3):
            col_sum = col_sum + cell_array[row][col]
            row_sum = sum(cell_array[row][:])
            
            if abs(row_sum) == 3:
                pygame.draw.line(screen, (255,0,0), (15,(2*(row+1)-1)*bh3/2),(board_width-15,(2*(row+1)-1)*bh3/2), 6)
                return print('player wins')
            elif abs(col_sum) == 3:
                pygame.draw.line(screen, (255,0,0), ((2*(col+1)-1)*bw3/2, 15),((2*(col+1)-1)*bw3/2,board_height-15), 6)
                return print('player wins')
    
    if n_clicks >= 9:
        return print('player wins')

        
draw_grid()

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
            
    pygame.display.update()
pygame.quit()