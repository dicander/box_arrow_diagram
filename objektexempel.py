class A:
    def __init__(self):
        self.count = 0
    
    def inc(self):
        self.count += 1
        # Diagram här innan vi återvänder


def main():
    a = A()
    a.inc()


if __name__ == '__main__':
    main()
