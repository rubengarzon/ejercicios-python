# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    impares = list(filter(lambda x: x % 2 != 0, lista))
    suma = reduce(lambda x, y: x + y, impares)
    print(suma)


if __name__ == "__main__":
    main()
