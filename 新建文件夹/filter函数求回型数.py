def hui(n):
    return str(n)==str(n)[::-1]
#后一个表示将数字反过来，与原数字比较是否相等

L=list(filter(hui,range(1,1000)))

print(L)