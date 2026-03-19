class OperacionesMatematicas:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self,numero1, numero2):
        return numero1 + numero2

    def restar(self,numero1, numero2):
        return numero1 - numero2

    def multiplicar(self,numero1, numero2):
        return numero1 * numero2

    def dividir(self,numero1, numero2):
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Error: División por cero no permitida"