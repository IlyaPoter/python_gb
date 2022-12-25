# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

first_list = [2, 3, 5, 9, 3]

def summ_number(my_list):
    result = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            result += my_list[i]
    return result

print(summ_number(first_list))
