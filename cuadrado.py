class Cuadrado(figurageometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)
    def area(self):
        return self.alto * self.ancho
    def __str__(self):
        return f"Cuadrado - lado: {self.alto}, área: {self.area()}"