# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
import os
os.system('cls')
index_position = [0, 2, 3]

def correct_check():
    while True:
        try:
            num = int(input("Введите число N: "))
            return num
        except ValueError:
            print("Введено некорректное значение, попробуйте еще раз")

number = correct_check()
my_list = []
for i in range(number):
    my_list.append(randint(-number, number))

result = 1
for i in range(len(index_position)):
    result = result*my_list[index_position[i]]
print(
    f"Произведение элементов {my_list} расположенные на позициях {index_position} равно {result}")
