# Оптимизировать программу с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number_string = input("Введите числа через пробел: ").split()

def check_number(num_string):
    number_list = []
    for element in num_string:
        number_list.append(int(element))
    return number_list

def main():
    my_list = list(set(check_number(number_string)))
    print(f"Список неповторяющихся элементов: {my_list}")
    
#Оптимизация:   
    res = list(filter(lambda x: number_string.count(x)==1, number_string))
    print(res)
###########################

if __name__ == "__main__":
    main()

