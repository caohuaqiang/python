class CountFromBy:
    def __init__(self):
        self.val = 100
        self.incr = 20

    def increase(self) -> None:
        self.val += self.incr
        return self.val


if __name__ == '__main__':
    A = CountFromBy()
    print(A.increase())