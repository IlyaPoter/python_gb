# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
os.system('cls')


def correct_check():
    while True:
        try:
            num = str(float(input("Введите вещественное число: ")))
            return num
        except ValueError:
            print("Введено некорректное значение, попробуйте еще раз")


number = correct_check()
result = 0
for i in range(len(number)):
    if number[i] != ".":
        result += int(number[i])
print(result)
