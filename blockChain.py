# A global blockchain variable as a list structure
blockChain = []

# To add a value to the block chain List 
def add_transactions(new_block_transaction, former_block_transaction = [1]):
    """ It adds a new transaction to the new block,
        as well as adding the previous transaction from the former block
        in the blockchain.
        
        Parameters:
            :transaction_amount:  A value entered by user to indicate the amount of
                                  cryptocurrency to be transacted 
                                  which should be included in the current block.
                                  h
            :former_block_transaction:    Values of the prevous transactions in the former block
                                  which is entered into the current block.
    """
    if former_block_transaction == None:
        former_block_transaction = [1]
    blockChain.append([former_block_transaction, new_block_transaction])


def get_last_block_transactions():
    """ It returns the last value of the current block in the blockchain."""
    if len(blockChain) < 1:
        return None
    return blockChain[-1]


def get_currency_amount():
    """ It prompts users to enter cryptocurrency values,
        which is used in making transactions.
     """
    user_input = float(input('Kindly enter amount of coins to be transferred: '))
    return user_input


def get_user_choice():
    user_choice = input('Your choice: ')
    return user_choice


def display_each_block():
    # Displaying each block in the blockchain
    if blockChain:
        for block in blockChain:
            print('Displaying Block')
            print(block)
    else:
        print("BlockChain is empty")
    
    print(blockChain)



while True:
    print('Please choose', end='\n')
    print('1: Add a new transaction', end='\n')
    print('2: Display each block in the blockchain', end='\n')
    print('3: Manipulate the chain', end='\n')
    print('4: Quit blockchain application', end='\n')
    
    user_choice = get_user_choice()
    
    if user_choice == '1':
        transferred_amount = get_currency_amount()
        add_transactions(transferred_amount, get_last_block_transactions())
    elif user_choice == '2':
        display_each_block()
    elif user_choice == '3':
        if len(blockChain) >= 1:
            blockChain[0] = [2]
            print("Blockchain first value has been changed to 2")
    elif user_choice == '4':
        break
    else:
        print('Input was invalid, please pick a value from the list!')
    

print('Done!')
