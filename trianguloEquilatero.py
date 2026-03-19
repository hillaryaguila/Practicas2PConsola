class TrianguloEquilatero:
    def __init__(self, base, altura, lado):
        self.base = base
        self.altura = altura
        self.lado = lado

    def area(self):
        return (self.base * self.altura) / 2
    def perimetro(self):
        return self.lado * 3