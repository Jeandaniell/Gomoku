import numpy as np
import random
import math
from algorithm import turn_AI

def start_command(size):
    game_board = np.zeros((size, size))
    if game_board.size > 5:
        print('OK - everything is good')
    else:
        print('ERROR message - unsupported size or other error')
    return game_board

def begin_command(board):
    x = random.randint(0, 19)
    y = random.randint(0, 19)

    if (board[x, y] == 0):
        board[x, y] = 2
        print(f"{x},{y}")


    return board

def turn_command(x, y, board):
    if (board[x, y] == 0):
        board[x, y] = 1
        return (1)
    else:
        print("ERROR opponents's move [{},{}]".format(x, y))
        return (0)

def end_command():
    exit(1)

def is_integer(value):
    return str(value).isdigit()
   
def process_board_command(board):
    while True:
        coordinates = input()
        if (coordinates == 'DONE'):
            break
        else:
            args = coordinates.split(',')
            num_args = len(args)
            if (num_args == 3 and is_integer(args[0]) and is_integer(args[1])
                and is_integer(args[2]) and 0 <= int(args[0]) < 20 and
                0 <= int(args[1]) < 20 and 1 <= int(args[2]) <= 2):
                board[int(args[0]), int(args[1])] = int(args[2])
            else:
                print('Wrong coordinates')
            continue
    return board            

def main():
    x = None
    y = None
    size = None

    while True:
        cmd = input()
        if cmd.startswith('START'):
            size = int(cmd.split()[1])           
            board = start_command(size)
        elif cmd.startswith('BEGIN'):
            begin_command(board)
        elif cmd.startswith('TURN'):
            x, y = map(int, cmd.split()[1].split(','))
            if (turn_command(x, y, board) == 1):
                turn_AI(board)
        elif cmd.startswith('END'):
            end_command()
        elif cmd.startswith('BOARD'):
            turn_AI(process_board_command(board))

if __name__ == "__main__":
    main()
