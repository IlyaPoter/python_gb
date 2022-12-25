# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
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
result = 0
my_list = []
for i in range(1, number+1):
    result += ((1+1/i)**i)
    my_list.append(round(((1+1/i)**i), 2))
print(f"Сумма последовательности чисел {my_list} равна {round(result,2)}")