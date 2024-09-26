"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""


class NombreUtils:
    

    def __init__(self):
        
        self.nombres_pairs = self.trouver_nombres_pairs()
        self.multiples_de_7 = self.trouver_multiples_de_7()

    def trouver_nombres_pairs(self):
       
        p = [] 
        for i in range(101):  
            if i % 2 == 0: 
                p.append(i)  
        return p  

    def trouver_multiples_de_7(self):
        
        m = []  
        for i in range(101):  
            if i % 7 == 0:  
                m.append(i)  
        return m  
    def __getitem__(self, index):
        
        if index == 0:
            return self.nombres_pairs  # Retourner la liste des nombres pairs
        elif index == 1:
            return self.multiples_de_7  # Retourner la liste des multiples de 7
        else:
            raise IndexError("Index out of range. Use 0 for pairs and 1 for multiples of 7.")


nombre_utils = NombreUtils()


nombres_pairs = nombre_utils[0]  
multiples_de_7 = nombre_utils[1] 

print("Nombres pairs entre 0 et 100 :", nombres_pairs)
print("Multiples de 7 entre 0 et 100 :", multiples_de_7)
