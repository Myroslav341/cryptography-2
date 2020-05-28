import json
import os
import hashlib
import random
from typing import Callable

path_to_chain = os.curdir + '/chains/'
users = ['Init', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'O']
SENDER = 'sender'
RECEIVER = 'receiver'
AMOUNT = 'amount'
TRANSACTIONS = 'transactions'
NONCE = 'nonce'
PREVIOUS_HASH = 'previous_hash'

max_amount = 100000
max_transaction = 50


def init_users_money():
    transactions = []

    for i in range(len(users) - 1):
        sender = users[0]
        receiver = users[i + 1]
        amount = random.randint(10000, max_amount)

        transaction = {
            SENDER: sender,
            RECEIVER: receiver,
            AMOUNT: amount
        }

        transactions.append(transaction)

    data = {
        TRANSACTIONS: transactions,
        NONCE: 0,
        PREVIOUS_HASH: 0,
    }

    with open(path_to_chain + '0', 'w') as file:
        json.dump(data, file, indent=4)


def get_hash(block_file):
    chain_file = open(path_to_chain + block_file, 'rb').read()

    return hashlib.sha256(chain_file).hexdigest()


def check_block_chain():
    chain_files = os.listdir(path_to_chain)
    chain_files = sorted([int(i) for i in chain_files])

    for chain_file in chain_files[1:]:
        chain_data = open(path_to_chain + str(chain_file))
        hash = json.load(chain_data)[PREVIOUS_HASH]

        previous_file = str(chain_file - 1)
        actual_hash = get_hash(previous_file)

        if hash == actual_hash:
            print(f'block {previous_file} is ok')
        else:
            print(f'block {previous_file} with errors')


def save_chain(transactions):
    chain_files = os.listdir(path_to_chain)
    chain_files = sorted([int(i) for i in chain_files])

    last_file = chain_files[-1]
    prev_hash = get_hash(str(last_file))

    new_chain_file = str(last_file + 1)

    data = {
        TRANSACTIONS: transactions,
        NONCE: 0,
        PREVIOUS_HASH: prev_hash,
    }

    with open(path_to_chain + new_chain_file, 'w') as file:
        json.dump(data, file, indent=4)

    while not str(get_hash(new_chain_file)).startswith('000'):
        data[NONCE] = random.randint(100000, 100000000000000)

        with open(path_to_chain + new_chain_file, 'w') as file:
            json.dump(data, file, indent=4)


def generate_transactions(max_count):
    transactions = []

    for i in range(max_count):
        sender = users[random.randint(1, len(users) - 1)]
        receiver = sender

        while receiver == sender:
            receiver = users[random.randint(1, len(users) - 1)]

        wallet = check_user_amount(sender)

        if wallet > 0:
            transaction = {
                SENDER: sender,
                RECEIVER: receiver,
                AMOUNT: random.randint(1, wallet // 10)
            }

            transactions.append(transaction)

    return transactions


def mine_blocks(size):
    for i in range(0, size):
        transactions = generate_transactions(random.randint(10, max_transaction))

        save_chain(transactions)


def check_user_amount(username):
    chain_files = os.listdir(path_to_chain)
    chain_files = sorted([int(i) for i in chain_files])
    wallet = 0

    for chain in chain_files:
        chain_data = open(path_to_chain + str(chain))
        chain_data = json.load(chain_data)

        for transaction in chain_data[TRANSACTIONS]:
            if transaction[SENDER] == username:
                wallet -= transaction[AMOUNT]
            if transaction[RECEIVER] == username:
                wallet += transaction[AMOUNT]

    return wallet


def get_users_wallets_info(filename):
    for username in users[1:]:
        chain_files = os.listdir(path_to_chain)
        chain_files = sorted([int(i) for i in chain_files])

        wallet = 0
        for chain in chain_files[:filename + 1]:
            chain_data = open(path_to_chain + str(chain))
            chain_data = json.load(chain_data)

            for transaction in chain_data[TRANSACTIONS]:
                if transaction[SENDER] == username:
                    wallet -= transaction[AMOUNT]
                if transaction[RECEIVER] == username:
                    wallet += transaction[AMOUNT]

        print(f'{username} : {wallet}')


def search_transactions_by_condition(value, condition: Callable[[int, int], bool]):
    """
    search all transactions smaller or bigger some amount
    :param value:
    :param condition:
    :return:
    """
    chain_files = os.listdir(path_to_chain)
    chain_files = sorted([int(i) for i in chain_files])

    for chain in chain_files:
        chain_data = open(path_to_chain + str(chain))
        chain_data = json.load(chain_data)

        for transaction in chain_data[TRANSACTIONS]:
            if condition(transaction[AMOUNT], value):
                print(f'Chain: {chain}: {transaction[SENDER]} -> {transaction[RECEIVER]} {transaction[AMOUNT]}')


if __name__ == '__main__':
    # init_users_money()
    # mine_blocks(5)
    # search_transactions_condition(10000, lambda x, y: x > y)
    # get_users_wallets_info(1)
    # print(check_user_amount(users[1]))
    check_block_chain()
