n = int(input("Факториал какого числа нужно вычислить? "))

factorial = 1
while n > 1:
    factorial = factorial*n
    n = n-1

print(factorial)