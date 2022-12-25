# Реализуйте алгоритм перемешивания списка.

from random import randint
import os
os.system('cls')

my_list = [0, 2, 3, -1, 5, 15, 977, -7]
print(f"Исходный список: {my_list}.")

new_list = []
for i in range(len(my_list)):
    index = randint(0, len(my_list)-1)
    new_list.append(my_list[index])
    my_list.pop(index)
print(f"Перемешанный список: {new_list}.")
