# Реализуйте RLE алгоритм: реализуйте модуль ВОССТАНОВЛЕНИЯ данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# 9W3B24W1B14W
# WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW

f = open('task_HW5_2.txt', 'r')
data = f.read()
f.close()

word =[]
number = []
result = []
for i in data:
    if i.isalpha():
        if not word or not last_isalpha:
            word.append(i)
        else:
            word[-1] += i
    else:
        if not number or last_isalpha:
            number.append(i)
        else:
            number[-1] += i
    last_isalpha = i.isalpha()

for i in range(len(word)):
    result.append(int(number[i])*word[i])
print(result)
result= "".join(map(str, result))
print(result)
with open('task_HW5_3.txt', 'w') as data:
    data.write(result)