# max = 0
# for i in range(5):
#     num = int(input(f"Введите число {i+1}: "))
#     if num>max:
#         max=num
# print(max)

# list = []
# max = 0
# for i in range(5):
#     i = int(input("Введите число: "))
#     list.append(i)
#     if i > max:
#         max = i
# print(list)
# print(max)

# number = int(input("Введите N: "))
# list = range(-number, number)
# print(*list)

# Напишите программу, которая будет принимать на вход дробь и показывать первую чифрц дробной части числа
# 6,78 -> 7
# 5 -> нет

number = float(input("Введите число: "))
if number%1==0:
    print("нет")
else:
    print(int(number*10%10))