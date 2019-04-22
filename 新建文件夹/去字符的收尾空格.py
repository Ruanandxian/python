def m(zifu):
    if zifu[0] == ' ':
        zifu = zifu[1:]
        zifu = m(zifu)
    elif zifu[-1] == ' ':
        zifu = zifu[:-1]
        zifu = m(zifu)
    return zifu


print(m(zifu=input()))
