def f(v, i):
    v.append(1)
    i += 2
    print("f", locals())


def g(v, i):
    print(id(i), "is address of i")
    v.append(2)
    i += 3
    f(v, i)
    print("g",locals())
    print(id(i), "is address of i")



def main():
    v = []
    i = 0
    print(id(i), "is address of i")
    g(v, i)
    print("main", locals())


if __name__ == '__main__':
    main()
