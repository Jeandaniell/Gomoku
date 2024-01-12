#!/usr/bin/env python3

import numpy as np

def check_line(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(col, col + 5):
            if 0 <= i < len(board[line]):
                if board[line, i] != 0 and board[line, i] != pawn:
                    return False
            else:
                return False
        return True

def check_reverse_line(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(col, col - 5, -1):
            if 0 <= i < len(board[line]):
                if board[line, i] != 0 and board[line, i] != pawn:
                    return False
            else:
                return False
        return True
    return False


def check_column(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(line, line + 5):
            if 0 <= i < len(board):
                if board[i, col] != 0 and board[i, col] != pawn:
                    return False
            else:
                return False
        return True

def check_reverse_column(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(line, line - 5, -1):
            if 0 <= i < len(board):
                if board[i, col] != 0 and board[i, col] != pawn:
                    return False
            else:
                return False
        return True
    return False


def check_left_diagonal(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(0, 5):
            x, y = line + i, col + i
            if 0 <= x < len(board) and 0 <= y < len(board[line]):
                if board[x, y] != 0 and board[x, y] != pawn:
                    return False
            else:
                return False
        return True
    return False

def check_left_diagonal_reverse(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(5):
            x, y = line - i, col - i
            if 4 <= x < len(board) and 4 <= y < len(board[0]):
                if board[x, y] != 0 and board[x, y] != pawn:
                    return False
            else:
                return False
        return True
    return False

def check_right_diagonal(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(0, 5):
            x, y = line + i, col - i
            if 0 <= x < len(board) and 0 <= y < len(board[line]):
                if board[x, y] != 0 and board[x, y] != pawn:
                    return False
            else:
                return False
        return True

def check_right_diagonal_reverse(board, line, col, pawn):
    if board[line, col] == pawn:
        for i in range(0, 5):
            x, y = line - i, col + i
            if 0 <= x < len(board) and 0 <= y < len(board[line]):
                if board[x, y] != 0 and board[x, y] != pawn:
                    return False
            else:
                return False
        return True
    return False

def count_pawn_in_a_line(board, line, col, pawn):
    count = 0
    for i in range (5):
        if (board[line, col + i] == pawn):
            count += 1
            
    return (count)

def define_most_warning_line(board, pawn):
    most_warning_line = 0
    most_warning_col = 0
    max_count = 0
    for line in range(len(board)):
        for col in range(len(board) - 4):
            if (check_line(board, line, col, pawn) == True):
                count = count_pawn_in_a_line(board, line, col, pawn)
                if count > max_count:
                    max_count = count
                    most_warning_line = line
                    most_warning_col = col

    return most_warning_line, most_warning_col, max_count

def count_pawn_in_a_line_reverse(board, line, col, pawn):
    count = 0
    while col >= 4 and board[line, col] == pawn:
        count += 1
        col -= 1
    return count

def define_most_warning_line_reverse(board, pawn):
    most_warning_line, most_warning_col, max_count = 0,0,0
    for line in range(len(board)):
        for col in range (len(board) - 1, 3, -1):
            if (check_reverse_line(board, line, col, pawn)):
                count = count_pawn_in_a_line_reverse(board, line, col, pawn)
                if count > max_count:
                    max_count, most_warning_line, most_warning_col = count, line, col
    
    return most_warning_line, most_warning_col, max_count

def count_pawn_in_a_column(board, line, col, pawn):
    count = 0
    for i in range(5):
        if (board[line + i][col] == pawn):
            count += 1
    return (count)

def define_most_warning_column(board, pawn):
    most_warning_line = 0
    most_warning_col = 0
    max_count = 0
    for line in range(len(board) - 4):
        for col in range(len(board)):
            if (check_column(board, line, col, pawn) == True):
                count = count_pawn_in_a_column(board, line, col, pawn)
                if count > max_count:
                    max_count = count
                    most_warning_line = line
                    most_warning_col = col

    return most_warning_line, most_warning_col, max_count

def count_pawn_in_a_column_reverse(board, line, col, pawn):
    count = 0
    while line >= 4 and board[line, col] == pawn:
        count += 1
        line -= 1
    return count

def define_most_warning_column_reverse(board, pawn):
    most_warning_line, most_warning_col, max_count = 0,0,0
    for line in range(len(board) - 1, 3, -1):
        for col in range(len(board)):
            if (check_reverse_column(board, line, col, pawn) == True):
                count = count_pawn_in_a_column_reverse(board, line, col, pawn)
                if count > max_count:
                    max_count, most_warning_line, most_warning_col = count, line, col

    return most_warning_line, most_warning_col, max_count

def count_pawn_in_a_left_diagonal(board, line, col, pawn):
    count = 0
    for i in range(5):
        if 0 <= line + i < len(board) and 0 <= col + i < len(board) and board[line + i][col + i] == pawn:
            count += 1
    return count

def count_pawn_in_a_left_diagonal_reverse(board, line, col, pawn):
    count = 0
    for i in range(5):
        x, y = line - i, col - i
        if 4 <= x < len(board) and 4 <= y < len(board[0]):
            if board[x, y] == pawn:
                count += 1
    return count

def define_most_warning_left_diagonal(board, pawn):
    most_warning_line = 0
    most_warning_col = 0
    max_count = 0
    for line in range(len(board) - 4):
        for col in range(len(board) - 4):
            if (check_left_diagonal(board, line, col, pawn) == True):
                count = count_pawn_in_a_left_diagonal(board, line, col, pawn)
                if count > max_count:
                    max_count = count
                    most_warning_line = line
                    most_warning_col = col


    return most_warning_line, most_warning_col, max_count

def define_most_warning_left_reverse_diagonal(board, pawn):
    most_warning_line, most_warning_col, max_count = 0,0,0
    for line in range(len(board) - 1, 3, -1):
        for col in range(len(board) - 1, 3, -1):
            if (check_left_diagonal_reverse(board, line, col, pawn) == True):
                count = count_pawn_in_a_left_diagonal_reverse(board, line, col, pawn)
                if count > max_count:
                    max_count, most_warning_line, most_warning_col = count, line, col
    
    return most_warning_line, most_warning_col, max_count

def count_pawn_in_a_right_diagonal(board, line, col, pawn):
    count = 0
    for i in range(5):
        if 0 <= line + i < len(board) and 0 <= col - i < len(board[0]) and board[line + i][col - i] == pawn:
            count += 1
    return count

def count_pawn_in_a_right_diagonal_reverse(board, line, col, pawn):
    count = 0
    for i in range(5):
        if 0 <= line - i < len(board) and 0 <= col + i < len(board[0]) and board[line - i][col + i] == pawn:
            count += 1
    return count

def define_most_warning_right_diagonal(board, pawn):
    most_warning_line = 0
    most_warning_col = 0
    max_count = 0
    for line in range(len(board) - 4):
        for col in range(4, len(board[0])):
            if (check_right_diagonal(board, line, col, pawn) == True):
                count = count_pawn_in_a_right_diagonal(board, line, col, pawn)
                if count > max_count:
                    max_count = count
                    most_warning_line = line
                    most_warning_col = col

    return most_warning_line, most_warning_col, max_count

def define_most_warning_right_diagonal_reverse(board, pawn):
    most_warning_line, most_warning_col, max_count = 0,0,0
    for line in range(len(board) - 1, 3, -1):
        for col in range(len(board) - 4):
            if (check_right_diagonal_reverse(board, line, col, pawn) == True):
                count = count_pawn_in_a_right_diagonal_reverse(board, line, col, pawn)
                if count > max_count:
                    max_count, most_warning_line, most_warning_col = count, line, col

    return most_warning_line, most_warning_col, max_count

def play(board, x, y):
    if (board[x, y] == 0):
        board[x, y] = 2
        print(f"{x},{y}")

    return x,y

def check_values(tuple1, tuple2):
    max_element = max(tuple1 + tuple2)

    if max_element in tuple2:
        position = tuple2.index(max_element)
        return 2, max_element, position
    else:
        position = tuple1.index(max_element)
        return 1, max_element, position
    

def find_zeros_line(board, start_line, start_col):
    zero_indices_line = []
    for i in range(start_col, start_col + 5):
        if board[start_line, i] == 0:
            zero_indices_line.append((start_line, i))
    return zero_indices_line

def find_zeros_line_reverse(board, start_line, start_col):
    zero_indices_line_reverse = []
    for i in range(start_col, start_col - 5, -1):
        if board[start_line, i] == 0:
            zero_indices_line_reverse.append((start_line, i))
    return zero_indices_line_reverse

def find_zeros_col(board, start_line, start_col):
    zero_indices_col = []
    for j in range(start_line, start_line + 5):
        if board[j, start_col] == 0:
            zero_indices_col.append((j, start_col))
    return zero_indices_col

def find_zeros_col_reverse(board, start_line, start_col):
    zero_indices_col_reverse = []
    for j in range(start_line, start_line - 5, -1):
        if board[j, start_col] == 0:
            zero_indices_col_reverse.append((j, start_col))
    return zero_indices_col_reverse

def find_zeros_left_diag(board, start_line, start_col):
    zero_indices_leftdiag = []
    for k in range (5):
        i, j = start_line + k, start_col + k
        if 0 <= i < board.shape[0] and 0 <= j < board.shape[1] and board[i, j] == 0:
            zero_indices_leftdiag.append((i, j))
    return zero_indices_leftdiag

def find_zeros_left_diag_reverse(board, start_line, start_col):
    zero_indices_leftdiag_reverse = []
    for k in range (5):
        i, j = start_line - k, start_col - k
        if 0 <= i < board.shape[0] and 0 <= j < board.shape[1] and board[i, j] == 0:
            zero_indices_leftdiag_reverse.append((i, j))
    return zero_indices_leftdiag_reverse

def find_zeros_right_diag(board, start_line, start_col):
    zero_indices_rightdiag = []
    for k in range (5):
        i, j = start_line + k, start_col - k
        if 0 <= i < board.shape[0] and 0 <= j < board.shape[1] and board[i, j] == 0:
            zero_indices_rightdiag.append((i, j))
    return zero_indices_rightdiag

def find_zeros_right_diag_reverse(board, start_line, start_col):
    zero_indices_rightdiag_reverse = []
    for k in range (5):
        i, j = start_line - k, start_col + k
        if 0 <= i < board.shape[0] and 0 <= j < board.shape[1] and board[i, j] == 0:
            zero_indices_rightdiag_reverse.append((i, j))
    return zero_indices_rightdiag_reverse

def simulate_moves_line(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col  = define_most_warning_line(board_copy, pawn)[0], define_most_warning_line(board_copy, pawn)[1]
    zero_indices_line = find_zeros_line(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_line:
        line, col = position

        board_copy[line, col] = pawn

        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_left_diag = define_most_warning_left_diagonal(board_copy, pawn)[2]
        danger_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_left_diag = define_most_warning_left_reverse_diagonal(board_copy, pawn)[2]

        max_danger = max(danger_col, danger_left_diag, danger_right_diag, danger_rev_line, danger_rev_col, danger_rev_right_diag, danger_rev_left_diag)
        if (max_danger >= contain):
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0 

    return (contain, g_line, g_col)

def simulate_moves_line_reverse(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col  = define_most_warning_line_reverse(board_copy, pawn)[0], define_most_warning_line_reverse(board_copy, pawn)[1]
    zero_indices_line = find_zeros_line_reverse(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_line:
        line, col = position

        board_copy[line, col] = pawn

        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_left_diag = define_most_warning_left_diagonal(board_copy, pawn)[2]
        danger_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_right_diag = define_most_warning_right_diagonal_reverse(board_copy, pawn)[2]
        danger_rev_left_diag = define_most_warning_left_reverse_diagonal(board_copy, pawn)[2]

        max_danger = max(danger_col, danger_left_diag, danger_right_diag, danger_line, danger_rev_col, danger_rev_right_diag, danger_rev_left_diag)
        if (max_danger >= contain):
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0 

    return (contain, g_line, g_col)

def simulate_moves_column(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col, _ = define_most_warning_column(board_copy, pawn)

    zero_indices_col = find_zeros_col(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_col:
        line, col = position

        board_copy[line, col] = pawn

        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_left_diag = define_most_warning_left_diagonal(board_copy, pawn)[2]
        danger_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_left_diag = define_most_warning_left_reverse_diagonal(board_copy, pawn)[2]

        max_danger = max(danger_line, danger_left_diag, danger_right_diag, danger_rev_line, danger_rev_col, danger_rev_left_diag, danger_rev_right_diag)
        if max_danger >= contain:
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0

    return contain, g_line, g_col

def simulate_moves_column_reverse(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col, _ = define_most_warning_column_reverse(board_copy, pawn)

    zero_indices_col = find_zeros_col_reverse(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_col:
        line, col = position

        board_copy[line, col] = pawn

        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_left_diag = define_most_warning_left_diagonal(board_copy, pawn)[2]
        danger_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
        danger_rev_right_diag = define_most_warning_right_diagonal_reverse(board_copy, pawn)[2]
        danger_rev_left_diag = define_most_warning_left_reverse_diagonal(board_copy, pawn)[2]

        max_danger = max(danger_line, danger_left_diag, danger_right_diag, danger_rev_line, danger_col, danger_rev_right_diag, danger_rev_left_diag)
        if max_danger >= contain:
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0

    return contain, g_line, g_col

def simulate_moves_left_diagonal(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col, _ = define_most_warning_left_diagonal(board_copy, pawn)

    zero_indices_left_diag = find_zeros_left_diag(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_left_diag:
        line, col = position

        board_copy[line, col] = pawn

        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_right_diag = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_right_diag = define_most_warning_right_diagonal_reverse(board_copy, pawn)[2]

        max_danger = max(danger_line, danger_col, danger_right_diag, danger_rev_line, danger_rev_col, danger_rev_right_diag)
        if max_danger >= contain:
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0

    return contain, g_line, g_col

def simulate_moves_left_diag_reverse(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col, _ = define_most_warning_left_reverse_diagonal(board_copy, pawn)

    zero_indices_col = find_zeros_left_diag_reverse(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_col:
        line, col = position

        board_copy[line, col] = pawn

        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_right = define_most_warning_right_diagonal(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_right = define_most_warning_right_diagonal_reverse(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
 

        max_danger = max(danger_line, danger_rev_col, danger_right, danger_rev_line, danger_col, danger_rev_right)
        if max_danger >= contain:
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0
        
    return contain, g_line, g_col

def simulate_moves_right_diagonal(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col, _ = define_most_warning_right_diagonal(board_copy, pawn)

    zero_indices_right_diag = find_zeros_right_diag(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_right_diag:
        line, col = position

        board_copy[line, col] = pawn

        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_left_diag = define_most_warning_left_diagonal(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_left_diag = define_most_warning_left_reverse_diagonal(board_copy, pawn)[2]

        max_danger = max(danger_line, danger_col, danger_left_diag, danger_rev_line, danger_rev_col, danger_rev_left_diag)
        if max_danger >= contain:
            contain = max_danger
            g_line, g_col = position

        board_copy[line, col] = 0
        
    return contain, g_line, g_col

def simulate_moves_right_diagonal_reverse(board, pawn):
    contain, g_line, g_col = 0, 0, 0

    board_copy = board.copy()

    most_warning_line, most_warning_col, _ = define_most_warning_right_diagonal_reverse(board_copy, pawn)

    zero_indices_right_diag = find_zeros_right_diag_reverse(board_copy, most_warning_line, most_warning_col)

    for position in zero_indices_right_diag:
        line, col = position

        board_copy[line, col] = pawn

        danger_line = define_most_warning_line(board_copy, pawn)[2]
        danger_col = define_most_warning_column(board_copy, pawn)[2]
        danger_left_diag = define_most_warning_left_diagonal(board_copy, pawn)[2]
        danger_rev_line = define_most_warning_line_reverse(board_copy, pawn)[2]
        danger_rev_col = define_most_warning_column_reverse(board_copy, pawn)[2]
        danger_rev_left_diag = define_most_warning_left_reverse_diagonal(board_copy, pawn)[2]

        max_danger = max(danger_line, danger_col, danger_left_diag, danger_rev_line, danger_rev_col, danger_rev_left_diag)
        if max_danger >= contain:
            contain = max_danger
            g_line, g_col = position

            board_copy[line, col] = 0

    return contain, g_line, g_col


def turn_AI(board):
    player_tuple = (define_most_warning_line(board, 1)[2],
                    define_most_warning_column(board, 1)[2],
                    define_most_warning_right_diagonal(board, 1)[2],
                    define_most_warning_left_diagonal(board, 1)[2],
                    define_most_warning_line_reverse(board, 1)[2],
                    define_most_warning_column_reverse(board, 1)[2],
                    define_most_warning_right_diagonal_reverse(board, 1)[2],
                    define_most_warning_left_reverse_diagonal(board, 1)[2])
    
    ia_tuple = (define_most_warning_line(board, 2)[2],
                    define_most_warning_column(board, 2)[2],
                    define_most_warning_right_diagonal(board, 2)[2],
                    define_most_warning_left_diagonal(board, 2)[2],
                    define_most_warning_line_reverse(board, 2)[2],
                    define_most_warning_column_reverse(board, 2)[2],
                    define_most_warning_right_diagonal_reverse(board, 2)[2],
                    define_most_warning_left_reverse_diagonal(board, 2)[2])    
    
    if (check_values(player_tuple, ia_tuple)[0] == 1):
        if (check_values(player_tuple, ia_tuple)[2] == 0):
            x, y = simulate_moves_line(board, 1)[1], simulate_moves_line(board, 1)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 1):
            x, y = simulate_moves_column(board, 1)[1], simulate_moves_column(board, 1)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 2):
            x, y = simulate_moves_right_diagonal(board, 1)[1], simulate_moves_right_diagonal(board, 1)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 3):
            x, y = simulate_moves_left_diagonal(board, 1)[1], simulate_moves_left_diagonal(board, 1)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 4):
            x, y = simulate_moves_line_reverse(board, 1)[1], simulate_moves_line_reverse(board, 1)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 5):
            x, y = simulate_moves_column_reverse(board, 1)[1], simulate_moves_column_reverse(board, 1)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 6):
            x, y = simulate_moves_right_diagonal_reverse(board, 1)[1], simulate_moves_right_diagonal_reverse(board, 1)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 7):
            x, y = simulate_moves_left_diag_reverse(board, 1)[1], simulate_moves_left_diag_reverse(board, 1)[2]

        if (board[x, y] == 0 and 0 <= x < len(board) and 0 <= y < len(board)):
            play(board, x, y)
        else:
            for line in range (len(board)):
                for col in range (len(board)):
                    if board[line, col] == 0:
                        play(board, line, col)

    elif(check_values(player_tuple, ia_tuple)[0] == 2):
        if (check_values(player_tuple, ia_tuple)[2] == 0):
            x, y = simulate_moves_line(board, 2)[1], simulate_moves_line(board, 2)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 1):
            x, y = simulate_moves_column(board, 2)[1], simulate_moves_column(board, 2)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 2):
            x, y = simulate_moves_right_diagonal(board, 2)[1], simulate_moves_right_diagonal(board, 2)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 3):
            x, y = simulate_moves_left_diagonal(board, 2)[1], simulate_moves_left_diagonal(board, 2)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 4):
            x, y = simulate_moves_line_reverse(board, 2)[1], simulate_moves_line_reverse(board, 2)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 5):
            x, y = simulate_moves_column_reverse(board, 2)[1], simulate_moves_column_reverse(board, 2)[2]

        elif(check_values(player_tuple, ia_tuple)[2] == 6):
            x, y = simulate_moves_right_diagonal_reverse(board, 2)[1], simulate_moves_right_diagonal_reverse(board, 2)[2]
        
        elif(check_values(player_tuple, ia_tuple)[2] == 7):
            x, y = simulate_moves_left_diag_reverse(board, 2)[1], simulate_moves_left_diag_reverse(board, 2)[2]
        
        if (board[x, y] == 0 and 0 <= x < len(board) and 0 <= y < len(board)):
            play(board, x, y)
        else:
            for line in range (len(board)):
                for col in range (len(board)):
                    if board[line, col] == 0:
                        play(board, line, col)