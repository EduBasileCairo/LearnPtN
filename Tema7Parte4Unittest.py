# Un proceso de automatización de verificación
from math import pi

def area(radio):
    
    areaC = pi*(radio**2)
    return areaC

radio = 5 # Asignamos el valor 5 a la variable radio
resultado = area(radio) # Llamamos a la función area y guardamos el resultado

print('El área de la circunferencia es: ', resultado) # Imprimimos el resultado

valores = [1, 3, 5, 0 , -1, -3 , 2+3j, True, 'hola']

for v in valores:
    areaCalculada = area(v)
    print('Para el valor', v, 'el área es', areaCalculada)

# Ya sabemos que nuestra función está bien realizada, hace su trabajo, pero dependiendo de los valores que le pasemos, puede dar problemas. Hace cálculos que no se deberían llevar a cabo e incluso da error cuando le pasamos una cadena de texto. Este es un test muy primitivo. Haciendo uso de unittest podemos automatizar el proceso de prueba de nuestro código. Para usar unittest tenemos que seguir un protocolo, vamos a tener que crear otro archivo en el que se va a encontrar el propio código de unittest. Deberemos crear un archivo con el siguiente nombre: test_nombreArchivo.py El nombre deberá empezar por la palabra test_ seguido del nombre del archivo sobre el que vamos a realizar las pruebas. De tal forma que, si nuestro archivo se llama, por ejemplo, funcionRadio.py, el archivo de testing se debería llamar test_funcionRadio.py.
