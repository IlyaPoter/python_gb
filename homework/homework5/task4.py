# Реализуйте RLE алгоритм: реализуйте модуль СЖАТИЯ данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# 9W3B24W1B14W

f = open('task_HW5.txt', 'r')
data = f.read()
f.close()

print(data)

result_list = []
temp = data[0]
count = 0
for i in range(len(data)):
    if temp == data[i]:
        count += 1
    else:
        result_list.append(count)
        result_list.append(data[i-1])
        temp = data[i]
        count = 1
result_list.append(count)
result_list.append(data[-1])
result_list = result_list
result_list = "".join(map(str, result_list))
print(result_list)
with open('task_HW5_2.txt', 'w') as data:
    data.write(result_list)
