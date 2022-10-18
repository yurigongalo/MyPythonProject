import random
n = int(input("Введите кол-во элементов массива:"))#По условиям задачи не ясно сколько раз
def func(niz,verh):
    for i in range(n):
       a[i] = random.randint(niz,verh)# Рандомим числа  из диапазона
a = [0] * n # Делаем список и заполняем его нолями
p = int(input("Введите нижний предел диапазона:"))
q = int(input("Введите верхний предел диапазона:"))
func(p,q)
print(a)




# from random import random
# N = 10
# def func(a,mn,mx):
#     for i in range(N):
#         a[i] = int(random() * (mx-mn+1)) + mn
#         print(a[i])
#         # print(type(a[i]))
#         # print(a)
#         # print(i)
#         print("****")
# a = [0] * N
# # print(a)
# p = int(input("Введите нижний диапазон"))
# q = int(input("Введите верхний диипазон"))
# func(a,p,q)
# print(a)
