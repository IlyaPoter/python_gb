# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def factors(num):
    my_list = []
    delitel = 2
    while delitel * delitel <= num:
        if num % delitel == 0:
            my_list.append(delitel)
            num //= delitel
        else:
            delitel += 1
    if num > 1:
        my_list.append(num)
    return my_list

def main():
    import os
    os.system("cls")
    number = int(input("Задайте натуральное число N: "))
    result = factors(number)
    print(f"Список простых множителей числа {number}: {result}")
if __name__ == "__main__":
    main()
