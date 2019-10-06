import random


def f(victims):
    while victims:
        target = random.choice(victims)
        victims.remove(target)
        print(target)


v = "1000 2000 3000 4000 5000".split()
print("before", v)
f(v)
print("after", v)
