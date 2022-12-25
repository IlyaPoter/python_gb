# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibbonachi(index):
    if index == 1:
        return 0
    elif index == 2:
        return 1
    return fibbonachi(index-1) + fibbonachi(index-2)

number = int(input("Введите число: "))
lst = [fibbonachi(i) for i in range(1, number+2)]
lst = lst[::-1] + lst[1:]
print(lst)
