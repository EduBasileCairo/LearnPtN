# Acciones de finalización y limpieza
# Cuando tenemos excepciones, hay situaciones en las que queremos hacer operaciones de limpieza o finalización sin importar si la excepción ha saltado o no. Este tipo de operaciones suelen ser, por ejemplo, asegurarnos que cerramos un fichero, una conexión, etc. Para esto tenemos la sentencia finally:
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
except IndexError:
    print("Se ha producido un IndexError: índice fuera de rango")
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')

# Finally sólo asegura que el código de su bloque se va a ejecutar, pero impide que el flujo de programa se detenga. Para eso, recordad que tenemos el bloque except.


# El bloque 'else' en las excepciones
# La última sentencia útil en el uso de excepciones es la sentencia else. En el caso de excepciones, la sentencia else se comporta de manera muy parecida a cómo lo hacía al ponerla tras un bucle: ejecuta el código de su bloque sólo si NO salta la excepción en el bloque try/except:
def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print('El resultado es: ')
    finally:
        print('Ejecutamos el finally')
divide(4, 12)
divide(4, 0)
# En el ejemplo intentamos hacer una división, y controlamos dentro de un bloque try/except si hemos intentado hacer una división por 0. Si el usuario intenta dividir por 0, capturamos la excepción en el except. Si la operación es correcta, entonces mostramos el resultado en el bloque else.La ventaja del bloque else nos ahorra tener que evaluar si tenemos resultado o no (podríamos no haber obtenido un resultado en el caso de división por cero).