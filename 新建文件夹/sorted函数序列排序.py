L=[('csdf',75),('bvdfg',92),('Edg',88)]



#KEY接收一个函数，以对sorted函数前半部分操作
def by_name(t):
    return t[0].lower()

print(sorted(L,key=by_name))



def by_score(t):
    return t[1]

print(sorted(L,key=by_score))