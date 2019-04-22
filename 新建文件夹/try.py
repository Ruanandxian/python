try:
    r=10/int('2')
    print(r)
except ValueError as e:
    print('except',e)
except ZeroDivisionError as e:
    print('except',e)
else:
    print('no error')
finally:
    print('end')

import logging

def foo(s):
    return 10/int('s')

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally')

def a(s):
    n=int(s)
    if n==0:
        raise ValueError('error')
    return 10/n

def b(s):
    try:
        a('0')
    except ValueError as e:
        print('valueerror')
        raise

