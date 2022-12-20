# типы данных и переменные
# int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(value)

# s = "hello \n'world'"
# print(s)  # вывод строки

# print(a, '---', b, '---', s)

# print('{} --- {} --- {}'.format(a, b, s))
# print('{1} --- {2} --- {0}'.format(a, b, s))
# print(f'{a} --- {b} --- {s}')

# f = True
# print(f)
# list = ['1', '2', '3', 1,2,4.5,True]
# print(list)

# Ввод и вывод данных
# print, input

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(f'a = {a}, b = {b}. Сумма равна {a+b}')

# Арифметические операции
# +, -, *, /, %, //, **
# **,
# (), Сокращенные операции
# a = 3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, is not, in, not in
# gen

# f = [1,2,3,4]

# print(f)
# print(not 2 in f)

# is_odd = not f[0]%2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Ура, это же Марина!')
# elif username=='Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ',username)

# original = 239
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original%10)
#     original//=10
# else:
#     print('Пожалуй хватит')
# print(inverted)

# Управляющие конструкции:
# for
# for i in 'qwe - rty':
#     print(i)

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 2
print(f(arg))
