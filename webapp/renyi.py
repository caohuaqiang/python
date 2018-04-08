def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()
        print(kwargs)


def outer():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    return inner



if __name__ == '__main__':
    # myfunc3(1, 2, 3)
    # myfunc3(a=10, b=20, c=30)
    myfunc3(1, 2, 3, a=10, b=20, c=30)
    # i = outer()
    # i()
