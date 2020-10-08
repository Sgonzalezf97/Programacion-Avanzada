import random

from Violin import Violin
from Guitarra import Guitarra
from Persona import Persona
from Bajo import Bajo


class Banda():
    def __init__(self):
        self.musicos= []

    def agregarm(self, nombre):
        self.musicos.append(nombre)


    def GenerarI(self):
        numero = random.randint(1, 3)
        if (numero == 1):
            i = Guitarra("DO")
            """print(i.afinar())
            print(i.tocar())
            print(i.tocarEn("Do"))"""
            return i
        elif (numero == 2):
            i = Bajo("Do")
            """print(i.afinar())
            print(i.tocar())
            print(i.tocarEn("Do"))"""
            return i
        else:
            i = Violin("Do")
            """print(i.afinar())
            print(i.tocar())
            print(i.tocarEn("Do"))"""
            return i

    def PresentarB(self):
        for m in  self.musicos:
            print (m.presentar())
            m.tocarI(self.GenerarI())


class Musico(Persona, Banda):
    def presentar(self):
        return "hola mi nombre es " + self.nombre + " y estoy:"

    def tocarI(self,i):

        print(i.afinar())
        print(i.tocar())
        print(i.tocarEn("Do"))


b=Banda()
b.agregarm(Musico("Andres"))
b.PresentarB()

"""p = Musico("Andres")
print(p.presentar())
print(p.tocarI())
j = Musico("Julio")
print(j.presentar())
print(j.tocarI())"""
