# a=2
# b="q"
# try:
#     c=a+int(b)
# except ValueError:
#     print("Вводить разрешено только числа")
# except ZeroDivisionError:
#     print("На 0 делить нельзя")
# except TypeError:
#     print("Разные типы данных использовать нельзя")
# else:
#     print(c)
a=2
b="2"
try:
    c=a+b
except ValueError:
    print("Вводить разрешено только числа")
except ZeroDivisionError:
    print("На 0 делить нельзя")
except TypeError:
    print("Разные типы данных использовать нельзя")
else:
    print(c)


