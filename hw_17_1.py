a = [1,2,3,4,5,6]
print(a,type(a))
a.remove(a[3])
a.remove(a[3])
a.remove(a[3])
print(a,type(a))
a = tuple(a)
print(a,type(a))