import unittest

from Pais import calcularPoblacion

class MyTestCase(unittest.TestCase):
    def test_calcularPoblacion(self):
        A = 35000000
        B = 19900000
        año = 2019
        self.assertEqual(36985, calcularPoblacion(A,B,año))

if __name__ == '__main__':
    unittest.main()