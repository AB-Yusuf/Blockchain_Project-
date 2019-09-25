blockChain = []


def get_last_blockchain_value():
    return blockChain[-1]


# To add a value to the block chain List
def add_value(transaction_amount, last_transaction = [1]):
    blockChain.append([last_transaction, transaction_amount])


add_value(2)
add_value(3, get_last_blockchain_value())
add_value(4, get_last_blockchain_value())

print(blockChain)
