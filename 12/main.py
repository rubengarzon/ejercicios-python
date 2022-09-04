# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}  Modelo: {self.modelo}  Color: {self.color}"

def main():
    coche = Vehiculo("Ford", "Focus", "Rojo")
    print(coche)
    with open("coche.dat", "wb") as f:
        pickle.dump(coche, f)
    with open("coche.dat", "rb") as f:
        coche = pickle.load(f)
    print(coche)

if __name__ == "__main__":
    main()

 