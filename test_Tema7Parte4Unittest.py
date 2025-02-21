import unittest
from math import pi

def area(radio):
    if not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número")
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return pi * (radio**2)
class TestArea(unittest.TestCase):
    def test_area_radio_5(self):
        self.assertAlmostEqual(area(5), pi * 5**2, places=6)  # Usamos pi directamente para mayor precisión

    def test_area_radio_0(self):
        self.assertEqual(area(0), 0)

    def test_area_radio_negativo(self):
        with self.assertRaisesRegex(ValueError, "El radio no puede ser negativo"): # Usamos assertRaisesRegex para verificar el mensaje
            area(-1)

    def test_area_radio_no_numero(self):
         with self.assertRaisesRegex(TypeError, "El radio debe ser un número"):
            area("hola")

    def test_area_radio_complejo(self):
        with self.assertRaisesRegex(TypeError, "El radio debe ser un número"):
            area(2+3j)

    def test_area_radio_booleano(self):
        self.assertAlmostEqual(area(True), pi) #True se interpreta como 1

if __name__ == '__main__':
    unittest.main()