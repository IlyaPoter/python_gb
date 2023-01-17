# Создайте программу для игры в ""Крестики-нолики"".

# Function to print the Tic-Tac-Toe Design
import random
import os

def mytictactoe(val):
    os.system('cls')
    print("\n")
    print(' _________________')
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(val[0], val[1], val[2]))
    print('|_____|_____|_____|')

    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(val[3], val[4], val[5]))
    print('|_____|_____|_____|')

    print("|     |     |     |")

    print("|  {}  |  {}  |  {}  |".format(val[6], val[7], val[8]))
    print('|_____|_____|_____|')

    print("\n")

def check(val,user):
    if val[0] == 'X' and val[1] == 'X' and val[2] == 'X':
        return True
    if val[3] == 'X' and val[4] == 'X' and val[5] == 'X':
        return True
    if val[6] == 'X' and val[7] == 'X' and val[8] == 'X':
        return True
    if val[0] == 'X' and val[3] == 'X' and val[6] == 'X':
        return True
    if val[1] == 'X' and val[4] == 'X' and val[7] == 'X':
        return True
    if val[2] == 'X' and val[5] == 'X' and val[8] == 'X':
        return True
    if val[0] == 'X' and val[4] == 'X' and val[8] == 'X':
        return True
    if val[2] == 'X' and val[4] == 'X' and val[6] == 'X':
        return True
    if val[0] == 'O' and val[1] == 'O' and val[2] == 'O':
        return True
    if val[3] == 'O' and val[4] == 'O' and val[5] == 'O':
        return True
    if val[6] == 'O' and val[7] == 'O' and val[8] == 'O':
        return True
    if val[0] == 'O' and val[3] == 'O' and val[6] == 'O':
        return True
    if val[1] == 'O' and val[4] == 'O' and val[7] == 'O':
        return True
    if val[2] == 'O' and val[5] == 'O' and val[8] == 'O':
        return True
    if val[0] == 'O' and val[4] == 'O' and val[8] == 'O':
        return True
    if val[2] == 'O' and val[4] == 'O' and val[6] == 'O':
        return True
    return False


first_user = input('Введите имя: ')
second_user = input('Введите имя: ')
list_users = [first_user, second_user]
list_symbol = ['X', 'O']
first_move = random.choice(list_users)
symbol = random.choice(list_symbol)

print(f'!!! Жеребьевка. Первым ход делает {first_move} символом {symbol}')

def games(user, val, symbol):
    mytictactoe(val)
    move = int(
        input(f'Ход делает {user}, символ {symbol} (введите цифру на поле): '))
    for i in range(0, 9):
        if val[i] == move:
            val[i] = symbol
    if check(val,user):
        mytictactoe(val)
        return print(f'Конец игры! Выиграл {user}')
    if user == first_user:
        user = second_user
    else:
        user = first_user
    if symbol == "O":
        symbol = "X"
    else:
        symbol = "O"
    games(user, val, symbol)

games(first_move, [1, 2, 3, 4, 5, 6, 7, 8, 9], symbol)
