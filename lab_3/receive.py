import json


def load_keys(path: str):
    f = open(path, 'r')

    data = json.load(f)

    return data['public'], data['private']



def check_signature(text: str, signature) -> bool:
    signature_calculated = generate_signature(signature)

    try:
        return text == numbers_to_text(signature_calculated)
    except Exception:
        return False


def generate_signature(text: str) -> str:
    return str(pow(int(text), public_key_sender[0], public_key_sender[1]))


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


def decode(coded_words: str) -> str:
    return str(pow(int(coded_words), private_key_receiver[0], private_key_receiver[1]))


code_param = 100
public_key_sender, private_key_sender = load_keys('../lab_2/keys.json')
public_key_receiver, private_key_receiver = load_keys('../lab_3/keys_receiver.json')

file = open('message_and_sign.txt', 'r')
message_received, signature_received = file.read().split('\n')

message_received_decoded = numbers_to_text(decode(message_received))
print(f'message: {message_received_decoded}\n'
      f'signature: {check_signature(message_received_decoded, signature_received)}')
