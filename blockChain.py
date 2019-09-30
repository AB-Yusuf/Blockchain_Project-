# A global blockchain variable as a list structure
genesis_block = {
    'previous_hash': '', 
    'index': 0, 
    'transactions': []
                }
blockChain = [genesis_block]
open_transactions = []
owner = 'Abu'

# To add a value to the block chain List


def record_transactions(recipient, sender=owner, amount=1.0):
    """ It adds a new transaction to the new block,
        as well as adding the previous transaction from the former block
        in the blockchain.

        Parameters:
            :sender: The one who sends a particular amount of coins
            :recipient: The one who recieves a particular amount of coins
            :amount: The numeric value of coins to be used in transactions (default = 1.0)
            
    """
    #We want to add a new transaction to our list of open transactions
    new_transaction = {'sender': sender, 'recipent':recipient, 'amount':amount}
    open_transactions.append(new_transaction)
    
    
def mine_new_block():
    last_block = blockChain[-1]
    block = {'previous_hash': 'XYZ', 
             'index':len(blockChain), 
             'transactions': open_transactions
            }
    blockChain.append(block)
    print(blockChain)
    
    
def get_last_block_transactions():
    """ It returns the last value of the current block in the blockchain."""
    if len(blockChain) < 1:
        return None
    return blockChain[-1]


def add_new_transaction():
    """ It prompts users to enter the required details for a transaction, which includes
        name of sender,
        name of recipent,
        amount of coins to be transferred
     """
     
    transaction_recipient = input('Enter the recipent of the transaction: ')
    transaction_amount = float(input('Amount: '))
    return(transaction_recipient, transaction_amount)


def get_user_choice():
    user_choice = input('Your choice: ')
    return user_choice


def display_each_block():
    # Displaying each block in the blockchain
    if blockChain:
        print('Displaying each Block in the Blockchain')
        for block in blockChain:
            print(block)
        else:
            print('- '*20)
    else:
        print('BlockChain is empty')


def verify_chain():
    # block_index = 0
    is_chain_valid = True
    
    for block_index in range(len(blockChain)):
        if block_index == 0:
            continue
        elif blockChain[block_index][0] == blockChain[block_index - 1]:
            is_chain_valid = True
        else:
            is_chain_valid = False
            break
            
    return is_chain_valid
    
    # for block in blockChain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockChain[block_index-1]:
    #         is_chain_valid = True
    #     else:
    #         is_chain_valid = False
    #         break
    #     block_index += 1
    # return is_chain_valid

waiting_for_input = True

while waiting_for_input:
    print('Please choose\n')
    
    print('1: Add a new transaction\n')
    
    print('2: Display each block in the blockchain\n')
    
    print('3: Manipulate the chain\n')
    
    print('4: Quit blockchain application\n')

    user_choice = get_user_choice()

    if user_choice == '1':
        #Get the details of a new transaction
        transaction_data = add_new_transaction()
        recipient, amount = transaction_data
        record_transactions(recipient, amount = amount)
        print(open_transactions)
        mine_new_block()
        
    elif user_choice == '2':
        display_each_block()
        
    elif user_choice == '3':
        print("valid BlockChain")
        print(blockChain, end='\n\n')
        if len(blockChain) >= 1:
            blockChain[0] = [2]
            print('Blockchain first value has been changed to 2')
            print(blockChain, end='\n\n')
           
    elif user_choice == '11':
        verify_chain()
        
    elif user_choice == '4':
        waiting_for_input = False
        
    else:
        print('Input was invalid, please pick a value from the list!')
        
#     if not verify_chain():
#         display_each_block()
#         print('Invalid Blockchain!')
#         break
# else:
#      print('user left!')       
        
        
print('Done!')
