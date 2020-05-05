from lab_2.helpers import euclid
from sympy import isprime
import json
from lab_1 import Rand


bit_size = 2048
r = Rand(487234832358375345534469089274872389478564726576557634567436575)
#  4872348723847283753453448927487238947856472657656357634567436575

while True:
    p = r.next_int(bit_size, prime=True)
    q = r.next_int(bit_size, prime=True)
    print(f'p = {p}:{isprime(p)}, q = {q}:{isprime(p)}')

    n = q * p
    print(f'n = {n}')

    phi = (q - 1) * (p - 1)

    e = r.next_int(2, phi - 1)
    print(e)

    x, y, g = euclid(e, phi)
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
