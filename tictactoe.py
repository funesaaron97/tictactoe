def print_board(game_data):
    print()
    print('', game_data[6], '|', game_data[7], '|', game_data[8], '       7 | 8 | 9 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[3], '|', game_data[4], '|', game_data[5], '       4 | 5 | 6 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[0], '|', game_data[1], '|', game_data[2], '       1 | 2 | 3 ')
    print()

import random

player_symbol = '0'
computer_symbol ='1'
player_assign = input('Would you like to be x or o?')

while True:
    if player_assign == 'x':
        player_symbol ='x'
        computer_symbol ='o'  
        break
    elif player_assign == 'o':
        player_symbol = 'o'
        computer_symbol = 'x'
        break
    else:
        player_assign = input('Please choose either x or o!')
        continue


game_data = [' '] * 9   # initialize game data to an empty array
whose_turn = []
order = input('Would you like to go first? yes or no?')
while True:
    if order == 'yes':
        whose_turn = ['player', 'computer', 'player', 'computer', 'player', 'computer', 'player', 'computer', 'player' ]
        break
    elif order == 'no':
        whose_turn = ['computer', 'player', 'computer', 'player', 'computer', 'player', 'computer', 'player', 'computer']
        break
    else:
        order = input('Please write either yes or no!')
        continue


spots_on_board = [1,2,3,4,5,6,7,8,9]
print_board(game_data)
for i in whose_turn:
    if i == 'computer':
        print('The CPU will go now')
        opp_turn = int(random.choice(spots_on_board))
        game_data[opp_turn - 1] = computer_symbol
        print_board(game_data)
        spots_on_board.remove(opp_turn)
        if game_data[0] == computer_symbol and game_data[1] == computer_symbol and game_data[2] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[3] == computer_symbol and game_data[4] == computer_symbol and game_data[5] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[6] == computer_symbol and game_data[7] == computer_symbol and game_data[8] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[0] == computer_symbol and game_data[3] == computer_symbol and game_data[6] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[1] == computer_symbol and game_data[4] == computer_symbol and game_data[7] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[2] == computer_symbol and game_data[5] == computer_symbol and game_data[8] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[2] == computer_symbol and game_data[4] == computer_symbol and game_data[6] == computer_symbol:
            print('CPU wins!')
            break
        elif game_data[0] == computer_symbol and game_data[4] == computer_symbol and game_data[8] == computer_symbol:
            print('CPU wins!')
            break
    elif i == 'player':
        selection = int(input('Where would you like to go (1-9)? '))
        while True:
            if selection in spots_on_board:
                break
            else:
                print()
                print_board(game_data)
                print()
                print('Please choose an open spot on the board')
                print()
                selection = int(input('Where would you like to go (1-9)? '))
                continue
        game_data[selection - 1] = player_symbol
        print_board(game_data)
        spots_on_board.remove(selection)
        if game_data[0] == player_symbol and game_data[1] == player_symbol and game_data[2] == player_symbol:
            print('You win!')
            break
        elif game_data[3] == player_symbol and game_data[4] == player_symbol and game_data[5] == player_symbol:
            print('You win!')
            break
        elif game_data[6] == player_symbol and game_data[7] == player_symbol and game_data[8] == player_symbol:
            print('You win!')
            break
        elif game_data[0] == player_symbol and game_data[3] == player_symbol and game_data[6] == player_symbol:
            print('You win!')
            break
        elif game_data[1] == player_symbol and game_data[4] == player_symbol and game_data[7] == player_symbol:
            print('You win!')
            break
        elif game_data[2] == player_symbol and game_data[5] == player_symbol and game_data[8] == player_symbol:
            print('You win!')
            break
        elif game_data[2] == player_symbol and game_data[4] == player_symbol and game_data[6] == player_symbol:
            print('You win!')
            break
        elif game_data[0] == player_symbol and game_data[4] == player_symbol and game_data[8] == player_symbol:
            print('You win!')
            break
    if len(spots_on_board) == 0:
        print('Draw!')
        break
