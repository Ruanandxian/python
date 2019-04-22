name = ['admin', 'Shen', 'while']


def normalize(name):
    return name.capitalize()


L = list(map(normalize, name))

print(L)
