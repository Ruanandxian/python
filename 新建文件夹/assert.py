#assert断言，表达式n！=0应该为TRUE，否则，'error'
def foo(s):
    n = int(s)
    assert n != 0, 'error'
    return 10 / n


def main():
    foo(2)
#-O可以关闭断言