def validar_user(funcion_p):
    def funcion_aux(*args, **kwargs):
        if kwargs.get("user", "") == "Pablo":
            result = funcion_p()
            return result
        print("usuario invalido!")

    return funcion_aux
