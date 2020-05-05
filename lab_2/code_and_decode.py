import json


def text_to_numbers(text_to_code: str) -> int:
    coded = []

    for word in text_to_code.split():
        word_coded = ''

        for c in word:
            word_coded += str(ord(c) + code_param)

        print(f'{word} -> {word_coded}')

        coded.append(word_coded)

    return int(''.join(coded))


def numbers_to_text(numbers_to_decode: int) -> str:
    words = ''
    numbers_to_decode = str(numbers_to_decode)

    while True:
        word = numbers_to_decode[:4]
        words += chr(int(word) - code_param)

        numbers_to_decode = numbers_to_decode[4:]

        if len(numbers_to_decode) == 0:
            break

    return words


def code_text(words: int) -> int:
    return pow(words, public_keys[0], public_keys[1])


def decode(coded_words: int) -> int:
    return pow(coded_words, private_keys[0], private_keys[1])


def load_keys():
    f = open('../lab_2/keys.json', 'r')

    data = json.load(f)

    return data['public'], data['private']


public_keys, private_keys = load_keys()
code_param = 1000


def main():
    text = input('print your message:\n')

    coded_text_to_numbers = text_to_numbers(text)

    rsa_coded_text = code_text(coded_text_to_numbers)

    print(f'coded text -> {rsa_coded_text}')

    print(f'\ndecoded -> {numbers_to_text(decode(rsa_coded_text))}')


if __name__ == '__main__':
    main()
