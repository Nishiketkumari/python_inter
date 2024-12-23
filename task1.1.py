import os
import random
import time

WIDTH = 40
HEIGHT = 20
HEAD = "O"
BODY = "o"
FOOD = "*"
EMPTY = " "
BORDER = "@"

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    return [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

def place_food(board):
    while True:
        x = random.randint(1, HEIGHT - 2)
        y = random.randint(1, WIDTH - 2)
        if board[x][y] == EMPTY:
            return (x, y)

def draw_board(board, snake, food):
    clear_screen()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) == snake[0]:
                print(HEAD, end="")
            elif (i, j) in snake:
                print(BODY, end="")
            elif (i, j) == food:
                print(FOOD, end="")
            elif i == 0 or i == HEIGHT - 1 or j == 0 or j == WIDTH - 1:
                print(BORDER, end="")
            else:
                print(EMPTY, end="")
        print()

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    delta_x, delta_y = direction
    new_head = (head_x + delta_x, head_y + delta_y)
    snake.insert(0, new_head)
    return new_head

def main():
    board = create_board()
    snake = [(HEIGHT // 2, WIDTH // 2)]  
    food = place_food(board)
    direction = RIGHT

    while True:
        draw_board(board, snake, food)
        print("Use W (up), S (down), A (left), D (right) to move.")
        print("Press Q to quit.")
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'w':
                    direction = UP
                elif key == 's':
                    direction = DOWN
                elif key == 'a':
                    direction = LEFT
                elif key == 'd':
                    direction = RIGHT
                elif key == 'q':
                    break
        
        

        new_head = move_snake(snake, direction)
        if new_head in snake[1:] or new_head[0] in (0, HEIGHT - 1) or new_head[1] in (0, WIDTH - 1):
            print("Game Over!")
            break
        if new_head == food:
            food = place_food(board)  
        else:
            snake.pop()  

        time.sleep(0.1)  
if __name__ == "__main__":
    main()
