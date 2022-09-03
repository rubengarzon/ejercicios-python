# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

numero_inicial = 2
numero_final = 8

for numero in range(numero_inicial, numero_final + 1):
    if numero % 2 != 0:
        print(numero)
