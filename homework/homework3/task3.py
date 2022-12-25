# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

original_list = [1.1, 1.2, 3.1, 5, 10.01]

def difference_number(my_list):
    max_number = round((my_list[0] % 1), 2)
    min_number = round((my_list[0] % 1), 2)
    for i in range(len(my_list)):
        temp = round((my_list[i] % 1), 2)
        if temp != 0:
            if temp >= max_number:
                max_number = temp
            if temp <= min_number:
                min_number = temp
    return max_number-min_number

print(difference_number(original_list))
