# maximum=0
# number = int(input("Введите число"))
# while number > 0:
#    if number%10>maximum:
#        maximum = number % 10
#        number = number // 10
#        print(maximum)

number = int(input("Введите число"))
maximum=0
while maximum <= number %10:
    if number %10 >= maximum:
        maximum = number%10
        number = number//10
print(maximum)