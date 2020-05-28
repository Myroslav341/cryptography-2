import random
import socket
from sympy import isprime


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


def euclid(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y, a


def __generate_public_and_private():
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

    return (e, n), (d, n)


def text_to_numbers(text_to_code: str) -> str:
    """
    first split text by spaces and the code every word
    code like code_param + ascii code of symbol and concatenate
    :param text_to_code: text which need be coded in numbers
    :return: list of numbers (every element is coded word)
    """
    coded = []

    for sign in text_to_code:
        coded.append(str(ord(sign) + code_param))

    return ''.join(coded)


def create_signature(text: str) -> str:
    return str(pow(int(text), my_private[0], my_private[1]))


def code_text(words: int) -> str:
    return str(pow(words, receiver_key[0], receiver_key[1]))


def check_signature(text: str, signature_) -> bool:
    signature_calculated = generate_signature(signature_)

    try:
        return text == numbers_to_text(signature_calculated)
    except Exception:
        return False


def generate_signature(text: str) -> str:
    return str(pow(int(text), receiver_key[0], receiver_key[1]))


def numbers_to_text(numbers_to_decode: str) -> str:
    text = ''

    for i in range(0, len(numbers_to_decode), 3):
        text += chr(int(numbers_to_decode[i: i + 3]) - code_param)

    return text


def decode(coded_words: str) -> str:
    return str(pow(int(coded_words), my_private[0], my_private[1]))


def __handle_start_on(port: int):
    sock = socket.socket()

    sock.bind(('', port))
    sock.listen(1)

    conn, address = sock.accept()

    return conn


def __handle_connect_to(port: int):
    sock = socket.socket()

    sock.connect(('localhost', port))

    return sock


def __get_key(key_str: str):
    return int(key_str.split('|')[0]), int(key_str.split('|')[1])


def __get_message(message_: str):
    return message_.split('|')[0], message_.split('|')[1]


bit_size = 1024
code_param = 100
r = Rand(4872348323583753455344690892748723894785645763456743651234564337567567834567897655)
connection = None
receiver_key = None
my_public, my_private = __generate_public_and_private()


while True:
    message = input('message: ')

    if message.startswith('start on'):
        connection = __handle_start_on(int(message.split(' ')[-1]))

        print('waiting connection')

        receiver_key = connection.recv(2048).decode('utf-8')
        receiver_key = __get_key(receiver_key)
        print('public key received')

        connection.send(bytes(str(my_public[0]) + '|' + str(my_public[1]), 'utf-8'))

        print('connection established')

    elif message.startswith('connect to'):
        connection = __handle_connect_to(int(message.split(' ')[-1]))

        connection.send(bytes(str(my_public[0]) + '|' + str(my_public[1]), 'utf-8'))

        print('waiting confirmation')

        receiver_key = connection.recv(2048).decode('utf-8')
        receiver_key = __get_key(receiver_key)

        print('connection established')

        coded_message, signature = __get_message(connection.recv(2048).decode('utf-8'))

        decoded = numbers_to_text(decode(coded_message))
        print('he: ' + decoded)
        print(f'signature: {check_signature(decoded, signature)}')

    elif connection is not None:
        coded_message, signature = code_text(int(text_to_numbers(message))), create_signature(text_to_numbers(message))

        connection.send(bytes(str(coded_message) + '|' + str(signature), 'utf-8'))

        print('waiting...')

        coded_message, signature = __get_message(connection.recv(2048).decode('utf-8'))

        decoded = numbers_to_text(decode(coded_message))
        print('he: ' + decoded)
        print(f'signature: {check_signature(decoded, signature)}')
