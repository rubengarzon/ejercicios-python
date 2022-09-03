# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


print(es_primo(5))
