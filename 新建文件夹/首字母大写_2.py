name = ['admin', 'Shen', 'while']


def normalize(name):
    return name[:1].upper()+name[1:].lower()


L = list(map(normalize, name))

print(L)
