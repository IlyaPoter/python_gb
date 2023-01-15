# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие
# А[i] - 1 = A[i - 1]

# f = open('task_semi5.txt', 'r')
# data = f.read().split()
# f.close()

# data = list(map(int, data))

# for i, el in enumerate(data[:-1]):
#     if el != data[i+1]-1:
#         print(el+1)

# print(data)

# my_list=[1,2,3,4,5,6,8,9]
# print([el-1 for i,el in enumerate(my_list[1:]) if el!=my_list[i]+1])

# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
#  [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# my_list = list(map(int,my_list))
# new_list = []
# new_list.append(my_list[0])
# counter = 0
# for i,el in enumerate(my_list[:-1]):
#     if new_list[counter] < el:
#         new_list.append(el)
#         counter+=1
# print(new_list)

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# my_list = list(map(int,my_list))
# new_list = []
# new_list.append(my_list[0])
# for i,el in enumerate(my_list[:-1]):
#     if new_list[-1] < el:
#         new_list.append(el)
# print(new_list)


# Напишите программу, удаляющую из текста все слова, содержащие "абв"

# my_list = 'абв дшиш щшошщ щшт абв щшабвошщ шшт абв шгтшг'
# my_list1 = my_list.split()
# result_list = [my_list[i] for i in range(len(my_list)) if my_list[i]!='абв']

# result_list = [el for i, el in enumerate(my_list) if el!='абв']
# print(' '.join(result_list))

# result_list = list(filter(lambda el: 'абв' not in el, my_list.split())) ####### вот самый НОРМ
# print(' '.join(result_list))

