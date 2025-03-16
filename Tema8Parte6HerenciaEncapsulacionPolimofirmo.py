# HERENCIA

# Supongamos que tenemos una clase padre vehículo.Necesitamos crear dos clases hijas, Coche y Moto que heredarán de Vehículo. Posteriormente crearemos una instancia de la clase Coche y otra de la clase Moto.

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True
    def arrancar(self):
        self.arrancado = True
        self.parado = False
    def parar(self):
        self.parado = True
        self.arrancado = False
    def resumen(self):
        print("Marca:", self.marca, "\n", "Modelo:", self.modelo, "\n", "Color:", self.color, "\n", "Está arrancado:", self.arrancado,"\n", "Está parado:", self.parado)

miCoche = Vehiculo("Renault", "Megane")

miCoche.arrancar()

miCoche.resumen()

class Moto(Vehiculo):
    pass

miMoto = Moto("Kawasaki", "Ninja")

miMoto.resumen()

