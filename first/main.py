import mode_1 as m


def foo(a, b):
    return a+b


out = m.moo(5, 5)


class A:
    pass


if __name__ == '__main__':
    print(foo(2, 2))
    print(out)
