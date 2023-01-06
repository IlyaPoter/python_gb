# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
number = int(input("Введите натуральную степень: "))
def polinom(degree):
    result = [0, "="]
    result.append(random.randint(0, 100))

    for num in range(1, degree+1):
        result.append("+")
        num1 = random.randint(0, 100)
        result.append(f"{num1}*x^{num}")

    my_list_reverse = list(reversed(result))
    my_result = "".join(map(str, my_list_reverse))
    return my_result
print(polinom(number))
with open('task4.txt', 'w') as data:
    data.write(polinom(number))

number = int(input("Введите натуральную степень: "))
with open('task4_2.txt', 'w') as data: # второй полином для задачи 5
    data.write(polinom(number))