class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def dividir(self, a, b):
        try:
            return a / b
        except Exception:
            raise ErrorAlDividirEntreZero()


class ErrorAlDividirEntreZero(Exception):
    pass
