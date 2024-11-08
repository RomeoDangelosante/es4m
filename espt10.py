#Crea una classe Frazione che rappresenta una frazione matematica. La classe deve avere i seguenti attributi:

#numeratore: il numeratore della frazione
#denominatore: il denominatore della frazione
#Implementa i seguenti magic methods per la classe Frazione:

#__add__ per sommare due frazioni.
#__sub__ per sottrarre due frazioni.
#__mul__ per moltiplicare due frazioni.
#__str__ per restituire una rappresentazione leggibile della frazione.
#importante:

#Supponi che il denominatore sia sempre lo stesso.
#In una versione piu avanzata puoi provare a sommare frazioni con denominatore diverso

class Frazione:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, altro):
        return Frazione(self.x * altro.y + altro.x * self.y, self.y * altro.y)

    def __sub__(self, altro):
        return Frazione(self.x * altro.y - altro.x * self.y, self.y * altro.y)

    def __mul__(self, altro):
        return Frazione(self.x * altro.x, self.y * altro.y)

    def __str__(self):
        return f"Frazione({self.x}, {self.y})"


f1 = Frazione(3, 4)
f2 = Frazione(2, 4)

f3 = f1 + f2
print(f3)  

f4 = f1 - f2
print(f4)  

f5 = f1 * f2
print(f5) 

print(f1)  