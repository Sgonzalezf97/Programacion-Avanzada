from Instrumento import Instrumento
class Bajo(Instrumento):
    """ def __init__(self, afinar,tocar):
            self.afinar= afinar
            self.tocar = tocar"""

    def afinar(self):
        return "Afinando el bajo"

    def tocar(self):
        return "tocando el bajo"

    def tocarEn(self):
        return " tocando el bajo en DO"
