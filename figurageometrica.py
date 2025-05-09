class figurageometrica:

    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, valor):
        self._alto = valor
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor

    def area(self):
        return self.alto * self.ancho

    def perimetro(self ):
        return 2 * self.alto + 2 * self.ancho

    def __str__(self):
        return f'figurageometrica: {self.__dict__.__str__()}'

if __name__ == '__main__':
    fg = figurageometrica(8,5)
    print(fg)