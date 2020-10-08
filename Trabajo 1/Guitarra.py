from Instrumento import Instrumento
class Guitarra(Instrumento):
    """def __init__(self, afinar,tocar):
        self.afinar= afinar
        self.tocar = tocar"""

    def afinar(self):
        return "Afinando la guitarra"
    def tocar(self):
        return "tocando la guitarra"
    def tocarEn(self):
        return " tocando la guitarra en DO"

