# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


print(es_bisiesto(2022))
