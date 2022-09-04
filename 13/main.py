# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.


def main():
    paises = input("Introduce una lista de países (separados por comas): ")
    paises = set(paises.split(","))
    paises = sorted(paises)
    print(", ".join(paises))


if __name__ == "__main__":
    main()
