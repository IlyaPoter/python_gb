# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math
import os
os.system('cls')

def correct_check():
    while True:
        try:
            num = int(input("Введите вещественное число: "))
            return num
        except ValueError:
            print("Введено некорректное значение, попробуйте еще раз")

number = correct_check()
result = []
for i in range(1,number+1):
    result.append(math.factorial(i))

print(result)
