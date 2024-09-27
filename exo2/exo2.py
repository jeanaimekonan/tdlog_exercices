"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
class NombrePremier:
    def __init__(self):
       
        self.premiers = []

    def est_premier(self, n):
       
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generer_premiers(self, max_n):
        
        self.premiers = [num for num in range(2, max_n + 1) if self.est_premier(num)]
        return self.premiers

    def afficher_premiers(self):
       
        if not self.premiers:
            print("Aucun nombre premier n'a été généré.")
        else:
            print(f"Nombres premiers générés : {self.premiers}")

nombre_premier = NombrePremier()


nombre_premier.generer_premiers(100)


nombre_premier.afficher_premiers()


nombre = 29
if nombre_premier.est_premier(nombre):
    print(f"{nombre} est un nombre premier.")
else:
    print(f"{nombre} n'est pas un nombre premier.")
