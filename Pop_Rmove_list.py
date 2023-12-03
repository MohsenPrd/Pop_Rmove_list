## Mohsen Pourdehghan

products = ['TV #1', 'Monitor Display #2', 'Keyboard #3', 'Mouse #4', 'Midi Controller #5', 'Amplifier #6']
print(products)

x = int(input('\nwhich methode you wanna use? 1 for pop(), 2 for remove()'))

while x != 1 and x != 2 :
    
    x = int(input('AGAIN!!! which methode you wanna use? 1 for pop(), 2 for remove()'))
    
if x ==1 :
    prod_to_pop= int(input('enter your product number for pop: '))
    
    while 0 >= prod_to_pop or prod_to_pop > len(products):
        
             prod_to_pop= int(input('AGAIN!!! enter your product number for pop: '))
              
    print(f'\n{products.pop(prod_to_pop - 1)} has been removed!')

    print(f'\nUpdated list :\n {products}')
    
elif x ==2 :
    
    prod_to_remove= input('enter your product name for remove: ')
    
    while prod_to_remove not in products :
        
        prod_to_remove= input('AGAIN!!! enter your product name for remove: ')

    products.remove(prod_to_remove)
    print(f'\nUpdated list : \n{products}')
