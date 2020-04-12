import json


def load_keys():
    f = open('../lab_2/keys.json', 'r')

    data = json.load(f)

    return data['public'], data['private']


def check_signature(text: str, signature) -> bool:
    signature_calculated = generate_signature(signature)

    print(signature_calculated)

    return text == numbers_to_text(signature_calculated)


def generate_signature(text: str) -> str:
    return str(pow(int(text), public_key[0], public_key[1]))


def numbers_to_text(numbers_to_decode: str) -> str:
    """
    opposite to text_to_numbers
    :param numbers_to_decode: coded words
    :return: decoded text
    """
    text = ''

    for i in range(0, len(numbers_to_decode), 3):
        text += chr(int(numbers_to_decode[i: i + 3]) - code_param)

    return text


code_param = 100
public_key, private_key = load_keys()

file = open('message_and_sign.txt', 'r')
message_received, signature_received = file.read().split('\n')

print(f'message: {message_received}\nsignature: {check_signature(message_received, signature_received)}')
