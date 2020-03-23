import json


def text_to_numbers(text_to_code: str):
    coded = []
    for word in text_to_code.split():
        word_coded = ''
        for c in word:
            word_coded += str(ord(c) + 3)
        print(f'{word} -> {word_coded}')
        coded.append(word_coded)
    return coded


def numbers_to_text(numbers_to_decode: list):
    words = []
    for word in numbers_to_decode:
        word_decoded = ''
        while not word == 0:
            word_str = str(word)
            word_decoded += chr(int(word_str[:3]) - 3)
            if len(word_str) > 3:
                word = int(word_str[3:])
            else:
                word = 0
        words.append(word_decoded)
    return words


def code_text(words: list):
    coded = []
    for word in words:
        coded.append(pow(int(word), public_keys[0], public_keys[1]))
    return coded


def decode(coded_words: list):
    decoded_words = []
    for word in coded_words:
        decoded_words.append(pow(word, private_keys[0], private_keys[1]))
    return decoded_words



f = open('../lab_2/keys.json', 'r')

data = json.load(f)
public_keys = data['public']
private_keys = data['private']

text = input('print your message:\n')

text_numbers = text_to_numbers(text)

coded_text = code_text(text_numbers)

print(f'coded text -> {coded_text}')

print(f'decoded -> {numbers_to_text(decode(coded_text))}')
