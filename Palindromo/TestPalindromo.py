import unittest

from Palindromo import esPalindromo

class MyTestCase(unittest.TestCase):
    def test_esPalindromo(self):
        texto1 = "an na"
        self.assertEqual(True, esPalindromo(texto1))

if __name__ == '__main__':
    unittest.main()