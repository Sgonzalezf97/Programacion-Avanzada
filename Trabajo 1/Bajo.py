from Instrumento import Instrumento
class Bajo(Instrumento):
    def __init__(self, nota):
            self.nota= nota

    def afinar(self):
        return "Afinando el bajo"

    def tocar(self):
        return "tocando el bajo"

    def tocarEn(self,nota):
        return "tocando el bajo en: "+self.nota
