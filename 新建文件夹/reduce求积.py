from functools import reduce
L=[3,4,5,6,7,8]
def cj(x,y):
    return x*y

y=reduce(cj,L)

print(y)