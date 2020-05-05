import json


def text_to_numbers(text_to_code: str) -> list:
    coded = []
    while True:
        part = text_to_code[:split_param]

        part_coded = ''
        for c in part:
            part_coded += str(ord(c) + code_param)

        print(f'{part} -> {part_coded}')

        coded.append(part_coded)

        text_to_code = text_to_code[split_param:]
        if len(text_to_code) == 0:
            break

    return coded


def numbers_to_text(numbers_to_decode: list) -> str:
    words = []

    for part in numbers_to_decode:
        part_decoded = ''

        while not part == 0:
            part_str = str(part)
            part_decoded += chr(int(part_str[:4]) - code_param)

            if len(part_str) > 4:
                part = int(part_str[4:])
            else:
                part = 0
        words.append(part_decoded)
    return ''.join(words)


def code_text(words: list) -> list:
    """
    RSA coding of message
    :param words: list of numbers (words)
    :return: list of coded words
    """
    coded = []
    for word in words:
        coded.append(pow(int(word), public_keys[0], public_keys[1]))
    return coded


def decode(coded_words: list) -> list:
    """
    RSA decoding of message
    :param coded_words: list of coded numbers (words)
    :return: list of decoded numbers
    """
    decoded_words = []
    for word in coded_words:
        decoded_words.append(pow(word, private_keys[0], private_keys[1]))

    print(decoded_words)

    return decoded_words


def load_keys():
    f = open('../lab_2/keys.json', 'r')

    data = json.load(f)

    return data['public'], data['private']


public_keys, private_keys = load_keys()
code_param = 1000
split_param = 50


def main():
    text = input('print your message:\n')

    coded_text_to_numbers = text_to_numbers(text)

    rsa_coded_text = code_text(coded_text_to_numbers)

    print(f'coded text -> {rsa_coded_text}')

    print(f'\ndecoded -> {numbers_to_text(decode(rsa_coded_text))}')


if __name__ == '__main__':
    main()
