# Excepciones en Python: Manejo de errores - Notificación de eventos - Manejo de casos especiales - Manejo de casos especiales

def indexador(objeto, indice):
    return objeto[indice] 
resultado=indexador('Python', 0) # Llamamos a la función
print(resultado) # Mostramos el resultado en consola - Deberá ser p

#Capturando excepciones
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10) # Llamamos a la función con un índice fuera de rango
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch') # Se ejecuta después del try/except