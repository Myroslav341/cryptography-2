import json


def load_keys(path: str):
    f = open(path, 'r')

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
    return str(pow(int(text), private_key_sender[0], private_key_sender[1]))


def code_text(words: int) -> str:
    return str(pow(words, public_key_receiver[0], public_key_receiver[1]))


code_param = 100
public_key_sender, private_key_sender = load_keys('../lab_2/keys.json')
public_key_receiver, private_key_receiver = load_keys('../lab_3/keys_receiver.json')

message = input('your message: ')

f = open('message_and_sign.txt', 'w')
f.write('\n'.join([code_text(int(text_to_numbers(message))), create_signature(text_to_numbers(message))]))
