# Дана последовательность чисел. Получить список уникальных элементов заданной  последовательности
# Пример:
# [1,2,3,5,1,5,3,10] => [2,10]

from random import *
my_list = [randint(1,10) for i in range(8)]
print("Исходная строка: ", my_list, '\n')
result1 = list(filter(lambda x: my_list.count(x)==1, my_list))
result2 = [i for i in my_list if my_list.count(i)==1]
result3 = list(set(my_list))

print(result1)
print(result2)
print(result3)