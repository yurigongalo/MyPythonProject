# n = 80
# if n == 1 or n==21 or n==31 or n==41 or n==51 or n==61 or n==71 or n==81 or n==91:
#     print("Мне"+ " " + str(n) + " " + "год")
# elif n < 5 or 22<=n<=24 or 32<=n<=34 or 42<=n<=44 or 52<=n<=54 or 62<=n<=64 or 72<=n<=74 or 82<=n<=84 or 92<=n<=94 :
#     print("Мне"+ " " + str(n) + " " + "года")
# else: print("Мне"+ " " + str(n) + " " + "лет")
n = "81"
if n[1]==str(1):
    print("Мне" + " " + str(n) + " " + "год")
elif int(n) < 5 or 22<=int(n)<=24 or 32<=int(n)<=34 or 42<=int(n)<=44 or 52<=int(n)<=54 or 62<=int(n)<=64 or 72<=int(n)<=74 or 82<=int(n)<=84 or 92<=int(n)<=94 :
    print("Мне"+ " " + str(n) + " " + "года")
else:
    print("Мне"+ " " + str(n) + " " + "лет")