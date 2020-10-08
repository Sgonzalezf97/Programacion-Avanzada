import random

from Violin import Violin
from Guitarra import Guitarra
from Persona import Persona
from Bajo import Bajo
from Instrumento import Instrumento


class Banda():
    """def __init__(self, nombre,instrumento):
        self.nombre= nombre
        self.instrumento = instrumento"""

    def agregarm(self):
        numero = random.randint(1, 3)
        if (numero == 1):
            i = Guitarra()
            print(i.afinar())
            print(i.tocar())
            print (i.tocarEn())
        elif (numero == 2):
            i = Bajo()
            print (i.afinar())
            print (i.tocar())
            print (i.tocarEn())
        else:
            i = Violin()
            print (i.afinar())
            print (i.tocar())
            print (i.tocarEn())


p = Persona("Andres")
print(p.presentar())
b=Banda()
print(b.agregarm())

