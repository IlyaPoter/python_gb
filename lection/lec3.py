# def f(x):
#     x**2

# g = f
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2

# print(f(2))

# def calc1(x):
#     return x+10

# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc2, 10)

# sum = lambda x, y:x+y

# a=sum(2,9)

# print(a)

# list = [i for i in range(1,21) if i%2==0]
# print(list)

# def f(x):
#     return x**3
    
# list2 = [(i, f(i)) for i in range(1,21) if i%2==0]
# print(list2)

# my_list = [1,2,3,5,8,15,23,38]1

# list_result = [(i, f(i)) for i in my_list if i%2==0]
# print(list_result)

# data = list(map(int, input().split()))
# print(data)

# data = [x for x in range(1,21)]
# print(data)
# res = list(filter(lambda x: not x%2, data))
# print(res)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)

data2 = list(enumerate(users))
print(data2)