# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file1 = 'task4.txt'
file2 = 'task4_2.txt'

def read_polinom(file): # чтение многочлена с файла
    with open(str(file), 'r') as data:
        polinom = data.read()
    return polinom

def extraction_number(my_list):
    number_part = my_list.replace('=0', '')  # откидываем часть "=0"
    # разделяем строку и создаем массив строк
    list_part = number_part.split('+')
    new_list = []  # новый массив без ИКСОВ
    for i in range(len(list_part)-1):
        # оставляем в строках только значения
        new_list.append((list_part[i])[0:2])
        # удаляем "*", если числа перед ИКС менее 10
        new_list[i] = new_list[i].replace('*', ' ')

    last_element = number_part[-2::1]  # последнее число многочлена
    # добавляем в массив чисел последнее чило многочлена
    new_list.append(last_element)
    new_list = new_list[::-1]  # "переворачиваем" массив чисел
    new_list2 = map(int, new_list)
    return list(new_list2)

my_list1 = read_polinom(file1)
my_list2 = read_polinom(file2)

koef1 = extraction_number(my_list1)
koef2 = extraction_number(my_list2)

sum_num = map(sum, zip(
    koef1 + [0,]*(len(koef2)-len(koef1)), koef2 + [0,]*(len(koef1)-len(koef2))))
sum_num2 = list(sum_num)
result = [0, "=", sum_num2[0]]
count = 1
for i in range(1, len(sum_num2)):
    result.append("+")
    result.append(f"{sum_num2[i]}*x^{count}")
    count += 1

result = result[::-1]
my_result = "".join(map(str, result))
print(f'Первый многочлен: {my_list1}')
print(f'Второй многочлен: {my_list2}')
print(f'Сумма многочленов: {my_result}')
with open('task5.txt', 'w') as data:
    data.write(my_result)
