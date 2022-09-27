import random

n = int(input("Сколько множеств сгенерировать?"))
print("Сгенерированные множества:")
for j in range(1,n+1):
    # a = {i for i in range(1,9)}
    a = {i for i in range(1, random.randint(1,10))}
    print (j,a)
    print(type(a))
    print(type(j))
    for k in range(1,j):
        if k%3 == 3:
            print(k)
    print()