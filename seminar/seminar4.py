# number_string = input("Введите числа через пробел: ").split()
# print(number_string)

# number_list=[]
# for element in number_string:
#     number_list.append(int(element))
# print(number_list)
# print(max(number_list))
# print(min(number_list))

# max_number = int(number_string[0])
# min_number = int(number_string[0])

# for element in number_string:
#     element = int(element)
#     if element > max_number:
#         max_number = element
#     if element < min_number:
#         min_number = element
# print(max_number, min_number)

# print(list(map(int, number_string)))

import os
os.system('cls')
number_a = int(input("Введите значение a: "))
number_b = int(input("Введите значение b: "))
number_c = int(input("Введите значение c: "))
disc = number_b**2-4*number_a*number_c
if disc<0:
    print("Решений уравнение не имеет")
else:
    number_x1=(-number_b+disc**0.5)/(2*number_a)
    number_x2=(-number_b-disc**0.5)/(2*number_a)
    print(f"X1 = {number_x1}; x2 = {number_x2}")
