from lab_2.helpers import random_prime, bezout
from sympy import isprime
import json
from lab_1 import Rand


bit_size = 64
r = Rand(23843824623634736)

while True:
    p, q = random_prime(bit_size), random_prime(bit_size)
    print(f'p = {p}:{isprime(p)}, q = {q}:{isprime(p)}')

    n = q * p
    print(f'n = {n}')

    phi = (q - 1) * (p - 1)

    e = r.next_int(2, phi - 1)
    print(e)

    x, y, g = bezout(e, phi)
    print(f'g = {g}')

    d = (x % phi + phi) % phi

    if g == 1:
        break

print(f'public key = ({e},{n})')
print(f'private key = ({d},{n})')

f = open('keys.json', 'w')

data = dict(
    public=(e, n),
    private=(d, n)
)

json.dump(data, f)
