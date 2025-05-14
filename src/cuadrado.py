from src.figurageometrica import Figurageometrica
from src.color import Color


class Cuadrado(Figurageometrica, Color):
    def __init__(self, lado, color=None):
        Figurageometrica.__init__(self,ancho=lado, alto= lado)
        color.__init__(self,nombre= color)

    def area(self):
        return self.alto * self.ancho

    def _str_(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"

if __name__ == '__main__':
    c1 = Cuadrado(lado=6, color="Rojo")
    print(c1)
    print(f'area: {c1.area()}')
    print(f'perimetro: {c1.perimetro()}')