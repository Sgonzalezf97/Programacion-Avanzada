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
