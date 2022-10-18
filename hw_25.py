def razr(n):
    a = 0
    while n > 0:
        n = n//10
        a += 1
    return a
num = int(input('Введите число: '))
print('Количество разрядов:', razr(num))
