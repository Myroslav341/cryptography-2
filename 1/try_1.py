import random


class Rand:
    def __init__(self, seed):
        self.seed = seed
        self.last = seed

    def __next__(self):
        a = [int(d) for d in str(self.last ** 2)]
        self.last = int(''.join([str(b) for b in a[len(a) // 2 - 2: len(a) // 2 + 2]]))
        return self.last

    def __iter__(self):
        return self


r = Rand(1728)
for x in r:
    print(x)
