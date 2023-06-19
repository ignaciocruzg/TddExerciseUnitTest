class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def dividir(self, a, b):
        if b == 0:
            raise ErrorAlDividirEntreZero()
        else:
            return a / b


class ErrorAlDividirEntreZero(Exception):
    pass
