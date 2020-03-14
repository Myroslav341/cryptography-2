class Rand:
    def __init__(self, seed):
        self.seed = seed
        self.register = [x for x in format(seed, 'b')]

    def __next__(self):
        new = int(self.register[-1] != self.register[-2])
        self.register = [str(new)] + self.register[:-1]
        return self.__str__()

    def __iter__(self):
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(int(''.join(self.register), 2))

    def __eq__(self, other):
        return self.__str__() == other


r = Rand(1000000)
i = 0
start = str(r)
MAX = 10000000
log = []
for x in r:
    i += 1
    log.append(str(r))
    if start == x:
        print(i)
        break
    if i > MAX:
        break

f = open('log.txt', 'w')
for x in log:
    f.write(str(x) + ' ')
f.close()
