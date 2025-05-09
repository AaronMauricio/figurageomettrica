from Color import Color
from figurageometrica import *

class Cuadrado(figurageometrica, Color):
    def __init__(self, lado, color=None):
        figurageometrica.__init__(self,ancho=lado, alto= lado)
        color._init_(self,nombre= color)

    def area(self):
        return self.alto * self.ancho

    def _str_(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"

if __name__ == '__main__':
    c1 = Cuadrado(lado=8, color="Rojo")
    print(c1)
    print(f'area: {c1.area()}')
    print(f'perimetro: {c1.perimetro()}')