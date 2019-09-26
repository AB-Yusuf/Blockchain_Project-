# A global blockchain variable as a list structure
blockChain = []

# To add a value to the block chain List 
def add_value(transaction_amount, last_transaction = [1]):
    """ It adds a new transaction to the blockchain,
        as well as adding the previous transaction from the former block
        in the blockchain.
        
        Parameters:
            :transaction_amount:  A value entered by user to indicate the amount of
                                  cryptocurrency to be transacted 
                                  which should be included in the current block.
                                  h
            :last_transaction:    Values of the prevous transactions in the former block
                                  which is entered into the current block.
    """
    blockChain.append([last_transaction, transaction_amount])


def get_last_blockchain_value():
    """ It returns the last value of the current block in the blockchain."""
    return blockChain[-1]


def get_transferred_amount():
    """ It prompts users to enter cryptocurrency values,
        which is used in making transactions.
     """
    return float(input('Kindly enter amount to be transferred: '))


transferred_amount = get_transferred_amount()
add_value(transferred_amount)

transferred_amount = get_transferred_amount()
add_value(transaction_amount = transferred_amount, last_transaction = get_last_blockchain_value())

transferred_amount = get_transferred_amount()
add_value(transaction_amount = transferred_amount, last_transaction = get_last_blockchain_value())


print(blockChain)
