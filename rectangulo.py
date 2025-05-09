from figurageometrica import figurageometrica
from Color import Color

class Rectangulo(figurageometrica):
    def _init_(self, alto=0, ancho=0, color=None):
        figurageometrica.__init__(self, alto, ancho)
        Color.__init__(self,color)

    def area(self):
        return self.alto * self.ancho

    def _str_(self):
        return f"Rectángulo -> {self.__dict__.__str__()}"

if __name__ == '__main__':
    r1 = Rectangulo (alto=10, ancho=6, color="Rojo")
    print(r1)
    print(f'area: {r1.area()}')
    print(f'perimetro: {r1.perimetro()}')