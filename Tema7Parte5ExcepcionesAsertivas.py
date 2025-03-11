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
import pandas as pd

type(object).__name__
df = pd.DataFrame()

type(df).__name__ #DataFrame'
type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ is 'DataFrame' # True Boolean
type(df).__name__ == type([]).__name__ # False Boolean
type(df).__name__ is type([]).__name__ # False Boolean
assert(type(df).__name__ == 'DataFrame') # Success Example
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
        for _ in [self.first_name, self.last_name]: assert(type(_) is str)
        print('------')
        print('Passed all of the tests')
yay = Test('James' , 'Phoenix') # Success Example
yay.test_all_class_arguments()
# Testing both of the class variables to see whether they are both strings!
# Passed all of the tests

yay = Test(5 , 'Phoenix') # Fail Example
yay.test_all_class_arguments()
# Testing both of the class variables to see whether they are both strings!
# ----------------------------------------------------------------
AssertionError
# Traceback (most recent call last)
yay = Test(5 , 'Phoenix') # Fail Example
class Test(object):
    def __init__(self, first_name, last_name ):
        self.first_name = first_name
        self.last_name = last_name

    def test_all_class_arguments(self):
        argumentos = [self.first_name, self.last_name] #almaceno en una variable para poder usarla fuera de la clase.
        for _ in [self.first_name, self.last_name]: assert(type(_) is str)
        print('------')
        print('Passed all of the tests')

yay = Test(5 , 'Phoenix') # Fail Example
yay.test_all_class_arguments()


print('Passed all of the tests')

# METODOS DE AFIRMACIÓN DE PYTHON 3.x Unitest
# A continuación, se detalla la lista de todos los métodos de afirmación de UnitTest:

# Método                    Implementación
# assertEqual               a == b
# assertNotEqual            a != b
# assertTrue bool           (x) is True
# assertFalse bool          (x) is False
# assertIs                  a is b
# assertIsNot               a is not b
# assertIsNone              x is None
# assertIsNotNone           x is not None
# assertIn                  a in b
# assertNotIn               a not in b
# assertIsInstance          is instance(a,b)
# assertNotIsInstance       not is instance(a,b)
# assertRaises              fun(*args,**kwds)
#                           raises exc
# assertRaisesRegexp        fun(*args,**kwds)
#                           raises exc(regex)
# assertAlmostEqual         round(a-b,7) == 0
# assertNotAlmostEqual      round(a-b,7) != 0
# assertGreater             a > b
# assertGreaterEqual        a >= b
# assertLess                a < b
# assertLessEqual           a <= b
# assertRegexpMatches       r.search(s)
# assertNotRegexpMatches    not r.search(s)
# assertItemsEqual          sorted(a) == sorted(b)
# assertDictContainsSubset  all the key/value pairs in a exist in b
# assertMultiLineEqual      strings
# assertSequenceEqual       sequences
# assertListEqual           lists
# assertTupleEqual          tuples
# assertSetEqual            sets or frozensets
# assertDictEqual           dicts

# ESCRIBIR DECLARACIONES DE AFIRMACIÓN
# Además de usar declaraciones de afirmación simples, al importar el módulo de tipos de Python podemos hacer declaraciones de afirmación más abstractas en Tipos específicos:
from types import LambdaType # Importamos LambdaType

class Example():
    def __init__(self, id_, name):
        self._id = id_
        self.name = name

    def subtract(self):
        answer = 5 + 5
        return answer

    def test_lambda_function(self):
        assert(lambda x: x is LambdaType)

    def test_subtract_function(self):
        assert(self.subtract is LambdaType)
example_class = Example("123", 'James Phoenix')
print(example_class._id, example_class.name)
# 123 James Phoenix
# ------------------------------------------------
example_class.test_lambda_function() # Success Example
example_class.test_subtract_function() # Fail Example
# -----------------------------------------
AssertionError
example_class.test_subtract_function() # Success

def test_subtract_function(self):
    assert(self.subtract is LambdaType)

