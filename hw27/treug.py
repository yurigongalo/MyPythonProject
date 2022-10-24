import math
def PlTreug(a, b, c):
    pl = (a+b+c)/2
    return math.sqrt(pl * (pl-a) * (pl-b) * (pl-c))