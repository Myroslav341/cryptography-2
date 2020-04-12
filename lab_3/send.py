import json


def load_keys():
    f = open('../lab_2/keys.json', 'r')

    data = json.load(f)

    return data['public'], data['private']


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
    return str(pow(int(text), private_key[0], private_key[1]))


code_param = 100
public_key, private_key = load_keys()

message = input('your message: ')

f = open('message_and_sign.txt', 'w')
f.write('\n'.join([message, create_signature(text_to_numbers(message))]))
