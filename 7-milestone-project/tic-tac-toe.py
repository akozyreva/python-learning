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

def insert_move(player):
    print("Player " + player )
    move_line = int(input('Insert line from 1 to 3 '))
    move_col = int(input('Insert column from 1 to 3 '))
    os.system('clear')
    square[str(move_line)][move_col - 1] = player + '|'
    print_square()

def check_winner(player):
    for key, value in square.items():
        print(len(set(value)))

game = 1
move_count = 0
while game:
    if move_count % 2 == 0:
        insert_move('x')
        check_winner('x')
    else:
        insert_move('0')
    move_count += 1
    if move_count == 5:
        break
#os.system('clear')

#for x in range (0,5):
#    b = "Loading" + "."
#    print(b)
#    move_line = int(input('Insert line from 1 to 3 '))
#    move_col = int(input('Insert column from 1 to 3 '))
#    b = "Loading" + "."  + str(move_line)
#    print (b, end="\r")
#    time.sleep(1)
