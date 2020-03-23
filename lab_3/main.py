from helpers import random_prime


def hash_function_generator(p, m):

    def my_hash(st: str):
        return int(sum([(ord(c) - 96) * pow(p, i) for i, c in enumerate(st)]) % m)

    return my_hash


hash_function = hash_function_generator(31, random_prime(10))

print(hash_function('hello'))
print(hash_function('hello, you'))
print(hash_function('hello, there'))
print(hash_function('hello, my dear'))
