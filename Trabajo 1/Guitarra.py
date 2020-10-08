from Instrumento import Instrumento
class Guitarra(Instrumento):
    def __init__(self, nota):
        self.nota= nota


    def afinar(self):
        return "Afinando la guitarra"
    def tocar(self):
        return "tocando la guitarra"
    def tocarEn(self,nota):
        return "tocando la guitarra en "+ self.nota

