def f(v, i):
    v.append(1)
    i += 2
    print("f", locals())


def g(v, i):
    v.append(2)
    i += 3
    f(v, i)
    print("g",locals())


def main():
    v = []
    i = 0
    g(v, i)
    print("main", locals())


if __name__ == '__main__':
    main()
