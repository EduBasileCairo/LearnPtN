# Paso 1: Función que acepte cualquier número de argumentos y los imprima en una sola línea con "LOG:"
# Usaremos *args para aceptar cualquier número de argumentos y join() para unirlos en una sola línea
def log(*args):
    print("LOG:", *args)

log("Mensaje", "de", "prueba")  
# Salida: LOG: Mensaje de prueba

# Paso 2: Permitir que el usuario especifique un prefijo
# Añadiremos un argumento prefix para que el usuario pueda definirlo.
def log(prefix, *args):
    print(prefix, *args)

log("INFO:", "Este es un mensaje de información")  
# Salida: INFO: Este es un mensaje de información

# Paso 3: Hacer que el prefijo tenga un valor por defecto ("LOG:")
# Añadimos prefix="LOG:" como valor predeterminado.
def log(*args, prefix="LOG:"):
    print(prefix, *args)

log("Mensaje de prueba")  
# Salida: LOG: Mensaje de prueba

log("Error en el sistema", prefix="ERROR:")  
# Salida: ERROR: Error en el sistema

# Paso 4: Permitir que el usuario defina tanto prefix como sep (separador entre argumentos)
# El sep debe controlarse con join(), y ambos parámetros (prefix y sep) solo pueden pasarse por nombre.
def log(*args, prefix="LOG:", sep=" "):
    print(prefix, sep.join(map(str, args)))

log("Hola", "Mundo", prefix="INFO:", sep="-")  
# Salida: INFO: Hola-Mundo

log("Este", "es", "un", "mensaje")  
# Salida: LOG: Este es un mensaje

# Paso 5: Permitir el uso de un diccionario con **kwargs
# Podemos desempaquetar un diccionario con **kwargs y pasarlo a la función.
def log(*args, prefix="LOG:", sep=" "):
    print(prefix, sep.join(map(str, args)))

config = {"prefix": "DEBUG:", "sep": " | "}
log("Este", "es", "un", "debug", **config)
# Salida: DEBUG: Este | es | un | debug

''' Resumen de funcionalidades
log(*args): Acepta cualquier cantidad de argumentos.
log(prefix="INFO:", *args): Permite personalizar el prefijo.
log(prefix="INFO:", sep="-", *args): Personaliza el prefijo y el separador.
log(*args, **config): Permite pasar opciones como diccionario.'''





