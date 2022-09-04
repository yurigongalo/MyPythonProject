a="2"
b="0"
try:
    c=int(a)/b
except ValueError:
    print("Вводить разрешено только числа")
except ZeroDivisionError:
    print("На 0 делить нельзя")
except TypeError:
    print("Разные типы данных использовать нельзя")
else:
    print(c)

