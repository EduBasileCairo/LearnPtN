from math import pi
def area(r):
    #Verificamos los tipos correctos
    if type(r) not in [float, int]:
        raise TypeError("Solo números enteros o de coma flotante.")
    if r<0:
        raise ValueError("No se permiten valores negativos")
    areaC = pi*(r**2)
    return areaC




try:
    resultado = area("hola")
except TypeError as e:
    print(f"Error de tipo: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")