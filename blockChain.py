blockChain = [1]


#To add a value to the block chain List
def add_value():
    blockChain.append([blockChain[-1], 5.3])
    print(blockChain)
    
    
  
add_value()
add_value()
add_value()
print([blockChain[0]])

