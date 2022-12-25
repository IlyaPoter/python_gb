# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

def product_number(work_list):
    result_list=[]
    for i in range(round((len(work_list))/2+0.1)):
        result = work_list[i]*work_list[len(work_list)-i-1]
        result_list.append(result)
    return result_list
print(product_number(my_list))