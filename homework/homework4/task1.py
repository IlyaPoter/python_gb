# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


import random
import math


def number_accuracy(num):
    count = 0
    while num < 1:
        num = num*10
        count += 1
    return count

def main():
    original_number = float(input("Введите заданную точность: "))
    number = random.uniform(0, 100)
    accuracy = number_accuracy(original_number)
    print(f"Случайное число с заданной точностью: {round(number,accuracy)}")

if __name__ == "__main__":
    main()
