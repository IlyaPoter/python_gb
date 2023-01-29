# Оптимизировать программу с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

first_list = [2, 3, 5, 9, 3]

# Первоначальная версия:
def summ_number(my_list):
    result = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            result += my_list[i]
    return result
print(summ_number(first_list))

# Оптимизация:
def summ_number2(my_list):
    result = 0
    for i, el in enumerate(my_list):
        if i % 2 != 0:
            result += el
    return result
print(summ_number2(first_list))
