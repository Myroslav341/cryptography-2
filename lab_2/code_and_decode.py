import json


def text_to_numbers(text_to_code: str) -> list:
    """
    first split text by spaces and the code every word
    code like code_param + ascii code of symbol and concatenate
    :param text_to_code: text which need be coded in numbers
    :return: list of numbers (every element is coded word)
    """
    coded = []
    for word in text_to_code.split():
        word_coded = ''
        for c in word:
            word_coded += str(ord(c) + code_param)
        print(f'{word} -> {word_coded}')
        coded.append(word_coded)
    return coded


def numbers_to_text(numbers_to_decode: list) -> str:
    """
    opposite to text_to_numbers
    :param numbers_to_decode: coded words
    :return: decoded text
    """
    words = []
    for word in numbers_to_decode:
        word_decoded = ''
        while not word == 0:
            word_str = str(word)
            word_decoded += chr(int(word_str[:4]) - code_param)
            if len(word_str) > 4:
                word = int(word_str[4:])
            else:
                word = 0
        words.append(word_decoded)
    return ' '.join(words)


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
    return decoded_words


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
