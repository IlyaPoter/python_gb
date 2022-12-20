# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
number_x = bool(input("Введите x: "))
number_y = bool(input("Введите y: "))
number_z = bool(input("Введите z: "))

if (not (number_x or number_y or number_z)) == (not number_x and not number_y and not number_z):
    print("истина")
else:
    print("ложь")
