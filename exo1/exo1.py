"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""

def trouver_nombres_pairs():
   
    p = []  
    for i in range(101):  
        if i % 2 == 0:  
            p.append(i)  
    return p  

def trouver_multiples_de_7():
   
    m = [] 
    for i in range(101):  
        if i % 7 == 0:  
            m.append(i)  
    return m  


nombres_pairs = trouver_nombres_pairs()
multiples_de_7 = trouver_multiples_de_7()

print("Nombres pairs entre 0 et 100 :", nombres_pairs)
print("Multiples de 7 entre 0 et 100 :", multiples_de_7)

