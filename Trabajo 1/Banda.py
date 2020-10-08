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
            i = Guitarra("DO")
            print(i.afinar())
            print(i.tocar())
            print (i.tocarEn("Do"))
        elif (numero == 2):
            i = Bajo("Do")
            print (i.afinar())
            print (i.tocar())
            print (i.tocarEn("Do"))
        else:
            i = Violin("Do")
            print (i.afinar())
            print (i.tocar())
            print (i.tocarEn("Do"))


p = Persona("Andres")
print(p.presentar())
b=Banda()
print(b.agregarm())

