import unittest

def roman_to_int(s: str) -> int:
    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    resultado = 0
    anterior = 0
    for letra in s:
        actual = roman_int[letra]
        resultado += actual
        if anterior < actual:
            resultado -= anterior * 2
        anterior = actual
    return resultado

class TestRomanToInt(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("L"), 50)
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("D"), 500)
        self.assertEqual(roman_to_int("M"), 1000)

    def test_suma(self):
        self.assertEqual(roman_to_int("II"), 2)
        self.assertEqual(roman_to_int("VI"), 6)
        self.assertEqual(roman_to_int("XIII"), 13)
        self.assertEqual(roman_to_int("LX"), 60)
        self.assertEqual(roman_to_int("MMXXI"), 2021)
    
    def test_resta(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XL"), 40)
        self.assertEqual(roman_to_int("XC"), 90)
        self.assertEqual(roman_to_int("CD"), 400)
        self.assertEqual(roman_to_int("CM"), 900)

    
if __name__ == '__main__':
    unittest.main()