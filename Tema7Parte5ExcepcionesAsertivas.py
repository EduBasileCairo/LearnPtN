## Las excepciones asertivas (assert) son constructos sintácticas de Python que se configuran como booleanos puros, sólo devuelven True o False
## Saber cómo escribir afirmaciones en Python le permite escribir fácilmente minipruebas para su código. Los marcos de prueba como PyTest pueden funcionar directamente con afirmaciones para formar /UnitTests en pleno funcionamiento.
## Lista de DECLARACIONES DE AFIRMACION DE PYTES
## Module Imports
## from types import *
## import pandas as pd
## import numpy as np
## from collections.abc import Iterable

## Para probar cada línea o trozo, pintar con el mouse la línea o el código que se desea ejecutar y con botón derecho del mouse ir a RUNPYTHON y luego a RUN SELECTION 

## 1. Igual o no igual a [valor]
assert 5 == 5 # Success Example
assert 5 == 3 # Fail Example

## AssertionError:
assert 5 != 3 # Success Example
assert 5 != 5 # Fail Example

## 2. Type() is [valor]

assert type(5) is int # Success Example
assert type(5) is not int # Fail Example

# 3. Isinstance
assert type(5) is int # Success Example
assert type(5) is not int # Fail Example

# 4. Is [Tipo booleano]
true = 5==5
assert true is True # Success Example
assert true is False # Fail Example

# 5. In y not in [iterable]
list_one=[1,3,5,6]
assert 5 in list_one # Success Example
assert 5 not in list_one # Fail Example

# 6. Mayor o menor que [valor]
assert 5 > 4 # Success Example
assert 5 > 7 # Fail Example

# 7. El módulo % es igual a [valor]
assert 2 % 2 == 0 # Success Example
assert 2 % 2 == 1 # Fail Example

# 8. Declaracion de afirmación any()
example = [5,3,1,6,6]
booleans = [False, False,True, False]
assert any(example) == True # Success Example
assert any(booleans) == True # Success Example

# 9. Declaracion de afirmación all()
all(example)
True
all(booleans)
False
assert all(example) # Success Example
assert all(booleans) # Fail Example

# 10. Objetos personalizados: Es posible identificar si una clase es un tipo específico de objeto. Podemos hacer esto usando:
type(object).__name__
df = pd.DataFrame()
type(df).__name__
'DataFrame'
type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ is 'DataFrame' # True Boolean
type(df).__name__ == type([]).__name__ # False Boolean
type(df).__name__ is type([]).__name__ # False Boolean
assert(type(df).__name__ == 'DataFrame')
# Success Example
assert(type(df).__name__ ==type([]).__name__) # Fail Example

# COMBINACIÓN DE VARIAS DECLARACIONES ADN/OR CON DECLARACIONES DE AFIRMACIÓN: es posible combinar múltiples condiciones con OR o AND y probar los comandos encadenados con la declaración de afirmación
# AND
true_statement = 5 == 5 and 10 == 10
false_statement = 5 == 3 and 10 == 2
print(true_statement, false_statement)
True
False
assert true_statement # Success Example
assert false_statement # Fail Example

# OR
true_or_statement = 5 == 5 or 3 == 3
false_or_statement = 7 == 3 or 10 == 1
print(true_or_statement, false_or_statement)
True
False
assert true_or_statement # Success Example
assert false_or_statement # Fail Example

# PRUEBA DE VARIOS COMANDOS: podemos probar más de una cosa a la vez al tener múltiples afirmaciones dentro del mismo método de Python:
class Test(object):
    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name
    def test_all_class_arguments(self):
        print('Testing both of the class variables to see whether they are both strings!')
    for _ in [self.first_name, self.last_name]:
        assert(type(_) is str)
print('------')
print('Passed all of the tests')
yay = Test('James' , 'Phoenix') # Success
Example
yay.test_all_class_arguments()
Testing both of the class variables to
see whether they are both strings!
