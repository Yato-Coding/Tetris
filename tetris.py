import pygame
import time

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

window_x = 300
window_y = 600
clock = pygame.time.Clock()
fps = 15
current_turn = 0

pygame.init()
pygame.joystick.init()
pygame.display.set_caption('Tetris')
game_window = pygame.display.set_mode((window_x, window_y))

I_BLOCK = [[window_x // 2, window_y // 2], [window_x // 2, (window_y // 2)-30], [window_x // 2, (window_y // 2)-60], [window_x // 2, (window_y // 2)-90]]

J_BLOCK = [[window_x //2, window_y //2], [(window_x // 2)-30, window_y // 2], [(window_x //2)+30, window_y // 2], [(window_x // 2)-30, (window_y // 2)-30]]

L_BLOCK = [[window_x //2, window_y //2], [(window_x // 2)-30, window_y // 2], [(window_x //2)+30, window_y // 2], [(window_x // 2)+30, (window_y // 2)-30]]

O_BLOCK = [[window_x // 2, window_y // 2], [(window_x // 2)+30, window_y // 2], [window_x // 2, (window_y // 2)-30], [(window_x // 2)+30, (window_y // 2)-30]]

S_BLOCK = [[window_x // 2, window_y // 2],[(window_x // 2)-30, window_y // 2],[window_x // 2, (window_y // 2)-30],[(window_x // 2)+30, (window_y // 2)-30]]

T_BLOCK = [[window_x // 2, window_y // 2], [(window_x // 2)+30, window_y // 2], [(window_x // 2)-30, window_y // 2], [window_x // 2, (window_y // 2)-30]]

Z_BLOCK = [[window_x // 2, window_y // 2],[(window_x // 2)+30, window_y // 2],[window_x // 2, (window_y // 2)-30],[(window_x // 2)-30, (window_y // 2)-30]]


direction = ' '
running = True


def draw_I_Block(current_state):
    for i in current_state:
        pygame.draw.rect(game_window, BLUE, (i[0], i[1], 30, 30)) 
def draw_T_Block(current_state):
    for i in current_state:
        pygame.draw.rect(game_window, BLUE, (i[0], i[1], 30, 30)) 
def draw_J_Block(current_state):
    for i in current_state:
        pygame.draw.rect(game_window, BLUE, (i[0], i[1], 30, 30)) 
def draw_O_Block(current_state):
    for i in current_state:
        pygame.draw.rect(game_window, BLUE, (i[0], i[1], 30, 30)) 
def draw_S_Block(current_state):
    for i in current_state:
        pygame.draw.rect(game_window, BLUE, (i[0], i[1], 30, 30)) 
def draw_Z_Block(current_state):
    for i in current_state:
        pygame.draw.rect(game_window, BLUE, (i[0], i[1], 30, 30)) 

def Turn():
    global direction
    global current_turn
    print(current_turn)
    current_piece = 2
    current_state = I_BLOCK
#I BLOCK
    if current_piece == 0:
        if direction == 'UP':
            current_turn += 1
            direction = ' '
        if direction == ' ':
            if current_turn == 0:
                current_state = I_BLOCK
                draw_I_Block(current_state)
            if current_turn == 1:
                current_state = [[window_x//2, window_y//2], [(window_x//2)+30, window_y//2], [(window_x//2)+60, window_y//2], [(window_x//2)+90, window_y//2]]
                draw_I_Block(current_state)
            if current_turn == 2:
                current_turn = 0
                Turn()
# T BLOCK
    if current_piece == 1:
        if direction == 'UP':
            current_turn += 1
            direction = ' '
        if direction == ' ':
            if current_turn == 0:
                current_state = T_BLOCK
                draw_T_Block(current_state)
            if current_turn == 1:
                current_state = [[window_x//2, window_y//2], [window_x//2, (window_y//2)-30], [window_x//2, (window_y//2)+30], [(window_x//2)+30, window_y//2]]
                draw_T_Block(current_state)
            if current_turn == 2:
                current_state = [[window_x // 2, window_y // 2], [(window_x // 2)+30, window_y // 2], [(window_x // 2)-30, window_y // 2], [window_x // 2, (window_y // 2)+30]]
                draw_T_Block(current_state)
            if current_turn == 3:
                current_state = [[window_x//2, window_y//2], [window_x//2, (window_y//2)-30], [window_x//2, (window_y//2)+30], [(window_x//2)-30, window_y//2]]
                draw_T_Block(current_state)
            if current_turn == 4:
                current_turn = 0
                Turn()
#J BLOCK
    if current_piece == 2:
        if direction == 'UP':
            current_turn += 1
            direction = ' '
        if direction == ' ':
            if current_turn == 0:
                current_state = J_BLOCK
                draw_J_Block(current_state)
            if current_turn == 1:
                current_state = [[window_x //2, window_y //2], [(window_x // 2)-30, window_y // 2], [(window_x //2)+30, window_y // 2], [(window_x // 2)-30, (window_y // 2)-30]]
                draw_J_Block(current_state)
            if current_turn == 2:
                current_state = [[window_x //2, window_y //2], [(window_x // 2)-30, window_y // 2], [(window_x //2)+30, window_y // 2], [(window_x // 2)+30, (window_y // 2)-30]]
                draw_J_Block(current_state)
            if current_turn == 3:
                current_state = [[window_x //2, window_y //2], [(window_x // 2)-30, window_y // 2], [(window_x //2)+30, window_y // 2], [(window_x // 2)-30, (window_y // 2)-30]]
                draw_J_Block(current_state)
            if current_turn == 4:
                current_turn = 0
                Turn()
#S BLOCK
    if current_piece ==3:
        if direction == 'UP':
            current_turn += 1
            direction = ' '
        if direction == ' ':
            if current_turn == 0:
                current_state = J_BLOCK
                draw_J_Block(current_state)
            if current_turn == 1:
                current_state = 
                draw_J_Block(current_state)
            if current_turn == 2:
                current_state =               
                draw_J_Block(current_state)
            if current_turn == 3:
                current_state =
                draw_J_Block(current_state)
            if current_turn == 4:
                current_turn = 0
                Turn()
#Z BLOCK
    if current_piece == 4:
        if direction == 'UP':
            current_turn += 1
            direction = ' '
        if direction == ' ':
            if current_turn == 0:
                current_state = J_BLOCK
                draw_J_Block(current_state)
            if current_turn == 1:
                current_state = 
                draw_J_Block(current_state)
            if current_turn == 2:
                current_state =               
                draw_J_Block(current_state)
            if current_turn == 3:
                current_state =
                draw_J_Block(current_state)
            if current_turn == 4:
                current_turn = 0
                Turn()




while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        buttons = joystick.get_numbuttons()
        for i in range(buttons):
            time.sleep(0.02)
            button = joystick.get_button(i)
            if i == 1:
                if button == 1:
                    direction = 'UP'
                if button == 0:
                    direction = ' '
    game_window.fill(BLACK)
    Turn()
    pygame.display.update()
