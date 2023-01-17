# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# б) Добавьте игру против бота с "интеллектом"

import random
first_user = input('Введите имя: ')
print('Вы играете с ботом Себастьяном')
second_user = 'бот Себастьян'
list_users = [first_user, second_user]
first_move = random.choice(list_users)
print(f'!!! Жеребьевка. Первым ход делает {first_move}')

def games(user, sweets):
    print(f'Конфет на столе: {sweets}')
    if user == first_user:
        move = int(input(f'Сколько конфет берет игрок {user} (не более 28): '))
    else:
        if sweets<=28:
            move = 28
        else:
            temp = 1
            while ((sweets-temp)%5)!=0:
                temp+=1
            move = temp
        print(f'Бот Себастьян взял {move} конфет')
    sweets = sweets-move
    if sweets<=0:
        return print(f'Выиграл {user}')
    if user == first_user:
        user = second_user
    else: user = first_user
    games(user, sweets)
    
games(first_move, 2021)
