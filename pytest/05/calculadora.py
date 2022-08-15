
def calculadora(numero1, numero2, operacion):
    if operacion == '+':
        return numero1 + numero2
    elif operacion == '-':
        return numero1 - numero2
    elif operacion == '/':
        return numero1 / numero2
    elif operacion == '*':
        return numero1 * numero2
    else:
        return "operacion invalida"
