def mystery(v, n):
    n = n + 1
    v[1] = n


def main():
    v = [1, 2]
    n = 4
    mystery(v, n)
    print(v, n)


main()
