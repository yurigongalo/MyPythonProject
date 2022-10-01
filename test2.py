import random
a = set()
# print(type(a))
n = int(input("Введите колличество множеств:"))
m = int(input("Введите колличество элементов каждого множества:"))
A = []
for i in range(n):
    A1 = []
    for j in range(m):
        A1.append(random.randint(-50,50))
    A.append(A1)
    print('A1: ',A1)
print('А: ',A)
B = []
for i in range(n):
    B1 = []
    for j in range(m):
        if A[i][j]%3 == 0:
            B1.append(A[i][j])
        B.append(B1)
    print('B1:',B1)
print('B:',B)
rest1 = set().union(A[0])
print('Первое множество: ',rest1)
rest = set().union(*B)
print('rest: ',rest)
# print(rest-rest1)
# print(rest.difference(rest1))