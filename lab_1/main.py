import random
from matplotlib import pyplot as plt


class Rand:
    def __init__(self, seed):
        self.__seed = seed
        self.__register_seed = [x for x in format(self.__seed, 'b')]
        self.__register = []

    def next_int(self, *args, prime=False) -> int:
        if len(args) == 1:
            if not prime:
                return self.__int_by_bit_size(args[0])

            while True:
                rand = self.__int_by_bit_size(args[0])

                if self.__miller_rabin(rand):
                    return rand
        else:
            if not prime:
                return self.__int_from_range(args[0], args[1])

            while True:
                rand = self.__int_from_range(args[0], args[1])

                if self.__miller_rabin(rand):
                    return rand

    def __int_by_bit_size(self, bit_size: int) -> int:
        if len(self.__register) < bit_size:
            self.__init_register(bit_size)

        random = self.__next__()

        return random

    def __int_from_range(self, a, b) -> int:
        d = abs(b - a)
        bits = len(format(d, 'b'))
        differ = self.__int_by_bit_size(bits)

        while differ > d:
            differ = self.__int_by_bit_size(bits)

        return min(a, b) + differ

    def __init_register(self, size):
        self.__register = [0 for _ in range(size)]
        j = 0

        for i in range(size):
            self.__register[i] = self.__register_seed[j]
            j += 1

            if j == len(self.__register_seed):
                j = 0

    def __miller_rabin(self, n, k=1):
        s = 0
        t = n - 1

        while t % 2 == 0:
            t = t // 2
            s += 1

        for i in range(k):
            a = random.randint(2, n - 1)

            x = pow(a, t, n)
            if x == 1 or x == n - 1:
                continue
            else:
                return False

            # ok = False
            # for j in range(s - 1):
            #     x = x ** 2 % n
            #     if x == 1:
            #         return False
            #     if x == n - 1:
            #         ok = True
            #         break
            # if ok:
            #     continue
            # else:
            #     return False
        return True

    def __next__(self):
        new = int(self.__register[-1] != self.__register[-2])

        self.__register = [str(new)] + self.__register[:-1]

        return self.__int__()

    def __int__(self):
        return int(''.join(self.__register), 2)

    def __iter__(self):
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(int(''.join(self.__register), 2))

    def __eq__(self, other):
        return self.__int__() == other


def test_bit_size():
    bit_size = 256

    r = Rand(324823748234)

    rand_first = r.next_int(bit_size)
    k = 1
    s = [rand_first]

    while True:
        rand = r.next_int(bit_size)
        k += 1
        # print(f'r = {rand}, bits = {len(format(rand, "b"))}')
        if rand == rand_first:
            break
        s.append(rand)
    print(f'sequence size = {k}')

    print(f'min:{min(s)}, max:{max(s)}')

    h = (max(s) - min(s)) / 20

    m = min(s)
    cnt = []
    for i in range(20):
        cnt.append(0)
        for x in s:
            if m + h * i <= x < m + h * (i + 1):
                cnt[i] += 1

    plt.bar([i for i in range(20)], cnt)
    plt.show()


def test_by_range():
    r = Rand(34028349234972)

    a = r.next_int(256)
    b = r.next_int(256)

    print(f'a = {a}, b = {b}')

    rand_first = r.next_int(a, b)
    k = 1
    s = [rand_first]

    while True:
        rand = r.next_int(a, b)
        k += 1
        # print(f'r = {rand}, bits = {len(format(rand, "b"))}')
        if rand == rand_first:
            break
        s.append(rand)
    print(f'sequence size = {k}')

    print(f'min:{min(s)}, max:{max(s)}')

    h = (max(s) - min(s)) / 20

    m = min(s)
    cnt = []
    for i in range(20):
        cnt.append(0)
        for x in s:
            if m + h * i <= x < m + h * (i + 1):
                cnt[i] += 1

    plt.bar([i for i in range(20)], cnt)
    plt.show()


if __name__ == '__main__':
    import time

    start_time = time.time()
    r = Rand(38748265642572389456656568172501297512750932759175715402395126052645063457634564777232345)
    print(r.next_int(1024, prime=True))
    # print(time.time() - start_time)
    # test_bit_size()
    # test_by_range()
