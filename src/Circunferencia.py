import math

from src.color import Color
from src.figurageometrica import Figurageometrica

class Circunferencia(Figurageometrica, Color):
    def __init__(self, radio=0, color=None):
        Figurageometrica.__init__(self, alto=0, ancho=radio)
        color.__init__(self, valor=color)

    def __str__(self):
        return  f'Circunferencia-> [radio={self.ancho}. color={self._nombre}]'

    def area(self):
        return math.pi * self.ancho * self.ancho
    def perimetro(self):
        return 2 * math.pi * self.ancho * self.ancho

if __name__ == '__main__':
    c1=Circunferencia(color='red', radio=5)
    print(c1)
    print(f'Area: {c1.area()}')
    print(f'perimetro: {c1.perimetro()}')