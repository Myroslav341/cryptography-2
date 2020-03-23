from lab_1 import Rand


r = Rand(7467465736573456)


def random_prime(bit_size):
    a = r.next_int(bit_size)

    if a % 2 == 0:
        a += 1

    while not miller_rabin(a):
        a = r.next_int(bit_size)

        if a % 2 == 0:
            a += 1

    return a


def miller_rabin(n, k=10):
    s = 0
    t = n - 1
    while t % 2 == 0:
        t = t // 2
        s += 1

    for i in range(k):
        a = r.next_int(2, n - 1)
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue
        ok = False
        for j in range(s - 1):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == n - 1:
                ok = True
                break
        if ok:
            continue
        else:
            return False
    return True


def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y, a
