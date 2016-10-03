class Figuras:

    def cuadrado(self, lado):
        try:
            lado = float(lado)
            return lado * lado
        except Exception:
            return 'dato incorrecto'

    def rectangulo(self, ladoH, ladoB):
        try:
            ladoH = float(ladoH)
            ladoB = float(ladoB)
            return ladoH * ladoB
        except Exception, e:
            return 'dato incorrecto'

    def triangulo(self, ladoB, ladoH):
        try:
            ladoB = float(ladoB)
            ladoH = float(ladoH)
            return (ladoB * ladoH) / 2
        except Exception:
            return 'dato incorrecto'
"""
    def circulo(self, radio):
        try:
            radio = float(radio)
            return (radio * radio) * 3.1416
        except Exception:
            return 'dato incorrecto'
"""