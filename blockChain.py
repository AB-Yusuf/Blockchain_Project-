# A global blockchain variable as a list structure
blockChain = []

# To add a value to the block chain List 
def add_transaction_amount(transaction_amount, last_transaction = [1]):
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
    if last_transaction == None:
        last_transaction = [1]
    blockChain.append([last_transaction, transaction_amount])


def get_last_blockchain_value():
    """ It returns the last value of the current block in the blockchain."""
    if len(blockChain) < 1:
        return None
    return blockChain[-1]


def get_transaction_value():
    """ It prompts users to enter cryptocurrency values,
        which is used in making transactions.
     """
    user_input = float(input('Kindly enter amount to be transferred: '))
    return user_input


def get_user_choice():
    user_choice = input('Your choice: ')
    return user_choice


def print_blockchain_elements():
    # Displaying each block in the blockchain
    for block in blockChain:
        print('Displaying Block')
        print(block)



while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Display each block in the blockchain')
    print('3: Manipulate the chain')
    print('4: Quit blockchain application')
    user_choice = get_user_choice()
    
    if user_choice == '1':
        transferred_amount = get_transaction_value()
        add_transaction_amount(transferred_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == '3':
        if len(blockChain) >= 1:
            blockChain[0] = [2]
            print("Blockchain first value has been changed to 2")
    elif user_choice == '4':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    

print('Done!')
