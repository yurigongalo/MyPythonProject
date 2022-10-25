def decorator(func):
    def hello(n):
        print("привет,",n)
        func()
        print(n.upper())
    return (hello)
m = input("Введите имя:")
@decorator
def helloUPPER():
    print("привет,", end=' ')
helloUPPER(m)
