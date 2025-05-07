class figurageometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    def alto(self):
        return self._alto
    def alto(self, valor):
        self._alto = valor
    def ancho(self):
        return self._ancho
    def ancho(self, valor):
        self._ancho = valor
    def __int__(self):
        return f"Alto: {self.alto}, Ancho: {self.ancho}"
class Cuadrado(figurageometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)
    def area(self):
        return self.alto * self.ancho
    def __str__(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"
class Rectangulo(figurageometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)
    def area(self):
        return self.alto * self.ancho
    def __str__(self):
        return f"Rectángulo - alto: {self.alto}, ancho: {self.ancho}, área: {self.area()}"
if __name__ == '__main__':
    cuadrado = Cuadrado(8)
    print(cuadrado)
    rectangulo = Rectangulo(16, 6)
    print(rectangulo)