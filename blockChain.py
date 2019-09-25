blockChain = [1]


def get_last_blockchain_value():
    return blockChain[-1]


# To add a value to the block chain List
def add_value(transaction_amount):
    blockChain.append([get_last_blockchain_value(), transaction_amount])


add_value(2)
add_value(3)
add_value(4)

print(blockChain)
