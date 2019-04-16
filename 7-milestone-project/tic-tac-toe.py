import time
import os

square = {
    '1': [' |', ' |', ' |'],
    '2': [' |', ' |', ' |'],
    '3': [' |', ' |', ' |']
}

def print_square():
    print("   1 2 3")
    for key, value in square.items():
        print(key, end=' ')
        for i in value:
            print(i, end='')
        print('\n')

def input_move(player):
    move_line = int(input('Insert line from 1 to 3 '))
    move_col = int(input('Insert column from 1 to 3 '))
    move = square[str(move_line)][move_col - 1]
    return move_line, move_col, move

def insert_move(player):
    global move_count
    print("Player " + player )
    move_line, move_col, move = input_move(player)
    # check, that ceil isn't empty
    while move == 'x|' or move == '0|':
        print("Ceil is not empty. Choose another one")
        move_line, move_col, move = input_move(player)
        os.system('clear')
        print_square()
    square[str(move_line)][move_col - 1] = player + '|'
    os.system('clear')
    print_square()
    if move_count >= 5:
        check_winner(player)

def check_winner(player):
    # check lines
    for key, values in square.items():
        occur_player = values.count(player + '|')
        # if whole line is occured
        if occur_player == 3:
            print_winner(player)

    # check occurence in columns
    for i in range(3):
        if square['1'][i] == square['2'][i] == square['3'][i] == player + '|':
            print_winner(player)

    # check diagonales
    if (square['1'][0] == square['2'][1] == square['3'][2] == player + '|')\
    or (square['3'][0] == square['2'][1] == square['1'][2] == player + '|'):
        print_winner(player)


def print_winner(player):
    global game
    game = 0
    print("player "+ player + " won")

game = 1
move_count = 1
print_square()
while game:
    if move_count % 2 != 0:
        insert_move('x')
    else:
        insert_move('0')
    if move_count == 8:
        print("Dead heat")
        break
    move_count += 1
