from decorador import validar_user


lista = []


def agregar_item(item):
    lista.append(item)


@validar_user
def retirar_item():
    return lista.pop()

