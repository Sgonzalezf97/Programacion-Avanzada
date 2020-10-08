from abc import ABCMeta, abstractclassmethod

class Instrumento(metaclass=ABCMeta):
    @abstractclassmethod
    def afinar(cls):
        pass
    @abstractclassmethod
    def tocar(cls):
        pass
    @abstractclassmethod
    def tocarEn(cls):
        pass

class Guitarra(Instrumento):
    def __init__(self, afinar,tocar):
        self.afinar= afinar
        self.tocar = tocar

    def afinar(self):
        return "Afinando la guitarra"
    def tocar(self):
        return "tocando la guitarra"

class Bajo(Instrumento):
    def __init__(self, afinar,tocar):
        self.afinar= afinar
        self.tocar = tocar

    def afinar(self):
        return "Afinando el bajo"
    def tocar(self):
        return "tocando el bajo"

class Violin(Instrumento):
    def __init__(self, afinar,tocar):
        self.afinar= afinar
        self.tocar = tocar

    def afinar(self):
        return "Afinando el violin"
    def tocar(self):
        return "tocando el violin "

class Persona():
    def __init__(self, nombre):
        self.nombre=nombre
    
    def presentar(self,nombre):
        return " hola mi nombre es "+ self.nombre