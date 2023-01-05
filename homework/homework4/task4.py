# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
degree = int(input("Введите натуральную степень: "))
result = [0, "="]
result.append(random.randint(0, 100))

for num in range(1, degree+1):
    result.append("+")
    num1 = random.randint(0, 100)
    result.append(f"{num1}*x^{num}")

my_list_reverse = list(reversed(result))
my_result = "".join(map(str, my_list_reverse))
print(my_result)
with open('task4.txt', 'w') as data:
    data.write(my_result)
