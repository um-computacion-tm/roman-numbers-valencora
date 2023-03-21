import unittest


def decimal_to_roman(decimal):
    if (decimal >= 1)&(decimal <= 3):
        return "I"
    elif decimal == 10:
        return "X"
    elif decimal == 5:
        return "V"
    elif decimal == 4:
        return "IV"
    elif (decimal >= 6)&(decimal <= 8)&(decimal != 5) :
        return  "V" + ("I" * (decimal-5))
class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        resultado = decimal_to_roman(1)

        self.assertEqual(resultado,"I")

    def test_10(self):
        resultado = decimal_to_roman(10)

        self.assertEqual(resultado,"X")

    def test_5(self):
        resultado = decimal_to_roman(5)

        self.assertEqual(resultado,"V")

    def test_2(self):
        resultado = decimal_to_roman(2)

        self.assertEqual = (resultado,"II")

    def test_4(self):
        resultado = decimal_to_roman(4)

        self.assertEqual = (resultado,"IV")

if __name__=="__main__":
    unittest.main()