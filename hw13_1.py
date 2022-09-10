fib1 = fib2 = 1

n = int(input("Сколько элементов ряда Фибоначи вывести на экран?"))

print(fib2, end=' ')

for i in range(1, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')