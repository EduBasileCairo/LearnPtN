# Un proceso de automatización de verificación
from math import pi

def area(radio):
    
    areaC = pi*(radio**2)
    return areaC

radio = 5 # Asignamos el valor 5 a la variable radio
resultado = area(radio) # Llamamos a la función area y guardamos el resultado

print('El área de la circunferencia es: ', resultado) # Imprimimos el resultado

valores = [1, 3, 5 ]# 0 , -1, -3, 2+3j, True, 'hola']

for v in valores:
    areaCalculada = area(v)
print('Para el valor', v, 'el área es', areaCalculada)