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
    
if __name__ == '__main__':
    unittest.main()