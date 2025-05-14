from src.figurageometrica import Figurageometrica
from src.color import Color

class Rectangulo(Figurageometrica):
    def __init__(self, alto=0, ancho=0, color=None):
        Figurageometrica.__init__(self, alto, ancho)
        Color.__init__(self,color)

    def area(self):
        return self.alto * self.ancho

    def _str_(self):
        return f"Rectángulo -> {self.__dict__.__str__()}"

if __name__ == '__main__':
    r1 = Rectangulo (alto=8, ancho=7, color="negro")
    print(r1)
    print(f'area: {r1.area()}')
    print(f'perimetro: {r1.perimetro()}')