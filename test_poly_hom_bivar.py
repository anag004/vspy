import unittest
from poly_hom_bivar import PolyHomBivar
from real import R

class TestPolyHomBivarReal(unittest.TestCase):
    # Test polynomial addition
    def test_add(self):
        a = PolyHomBivar([R(1), R(2), R(3)])
        b = PolyHomBivar([R(4), R(5), R(6)])
        c = PolyHomBivar([R(5), R(7), R(9)])
        self.assertEqual(c, a + b)

    # Test polynomial multiplication
    def test_pow(self):
        a = PolyHomBivar([R(1), R(2), R(1)])
        b = PolyHomBivar([R(1), R(1)])
        self.assertEqual(a, b ** b)

    def test_pow2(self):
        a = PolyHomBivar([R(0), R(1), R(2), R(1)])
        b = PolyHomBivar([R(1), R(1)])
        c = PolyHomBivar([R(0), R(1), R(3), R(3), R(1)])
        e = PolyHomBivar([R(1), R(3), R(3), R(1)])
        self.assertEqual(c, a ** b)
        self.assertNotEqual(e, a ** b)

if __name__ == '__main__':
    unittest.main()