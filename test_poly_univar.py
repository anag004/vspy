# Test the hom poly bivar module over R and Zm

from real import R 
from mod_integer import Zm 
from poly_univar import PolyUnivar
import unittest

class TestPolyUnivarReal(unittest.TestCase):
    def test_eq(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        b = PolyUnivar([R(1), R(2), R(3)])
        c = PolyUnivar([R(1), R(1), R(2), R(3)])
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_add(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        b = PolyUnivar([R(-1), R(2), R(3)])
        c = PolyUnivar([R(4), R(6)])
        d = PolyUnivar([R(4), R(6), R(6)])
        self.assertEqual(c, a + b)
        self.assertNotEqual(d, a + b)

    def test_mul(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        b = PolyUnivar([R(1), R(2), R(3), R(4)])
        self.assertEqual(R(20), a * b)
        self.assertNotEqual(R(21), a * b)

    def test_rmul(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        b = PolyUnivar([R(2), R(4), R(6)])
        c = PolyUnivar([R(2), R(4), R(7)])
        self.assertEqual(b, R(2) * a)
        self.assertEqual(PolyUnivar([]), R(0) * a)
        self.assertNotEqual(c, R(2) * a)
        self.assertNotEqual(c, R(0) * a)

    def test_zero(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        self.assertEqual(a.zero() + a, a)
        self.assertEqual(a.zero(), R(0) * a)

    def test_linearlyIndependent(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        b = PolyUnivar([R(2), R(3), R(4)])
        c = PolyUnivar([R(3), R(4), R(5)])
        d = PolyUnivar([R(3), R(5), R(5)])
        self.assertTrue(a.linearlyIndependent([a, b, d]))
        self.assertFalse(a.linearlyIndependent([a, b, c]))
        self.assertFalse(a.linearlyIndependent([a, b, PolyUnivar([])]))

    def test_pow(self):
        a = PolyUnivar([R(1), R(2), R(3)])
        b = PolyUnivar([R(2), R(3), R(4)])
        c = PolyUnivar([R(2), R(7), R(16), R(17), R(12)])
        d = PolyUnivar([R(2), R(7), R(16), R(17), R(13)])
        self.assertEqual(c, a ** b)
        self.assertEqual(c, b ** a)
        self.assertNotEqual(d, a ** b)

class TestPolyUnivarModInteger(unittest.TestCase):
    def test_eq(self):
        a = PolyUnivar([Zm(1, 31), Zm(2, 31), Zm(3, 31)])
        b = PolyUnivar([Zm(1, 31), Zm(2, 31), Zm(34, 31)])
        c = PolyUnivar([Zm(1, 31), Zm(1, 31), Zm(2, 31), Zm(3, 31)])
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_add(self):
        a = PolyUnivar([Zm(1, 31), Zm(2, 31), Zm(3, 31)])
        b = PolyUnivar([Zm(30, 31), Zm(29, 31), Zm(28, 31)])
        d = PolyUnivar([Zm(4, 31), Zm(6, 31), Zm(6, 31)])
        self.assertEqual(a.zero(), a + b)
        self.assertNotEqual(d, a + b)

    def test_mul(self):
        a = PolyUnivar([Zm(1, 7), Zm(2, 7), Zm(3, 7)])
        b = PolyUnivar([Zm(1, 7), Zm(2, 7), Zm(3, 7), Zm(4, 7)])
        self.assertEqual(Zm(6, 7), a * b)
        self.assertNotEqual(Zm(0, 7), a * b)

    def test_rmul(self):
        a = PolyUnivar([Zm(1, 7), Zm(2, 7), Zm(3, 7)])
        b = PolyUnivar([Zm(2, 7), Zm(4, 7), Zm(-1, 7)])
        c = PolyUnivar([Zm(2, 7), Zm(4, 7), Zm(0, 7)])
        self.assertEqual(b, Zm(2, 7) * a)
        self.assertEqual(PolyUnivar([]), Zm(0, 7) * a)
        self.assertNotEqual(c, Zm(2, 7) * a)
        self.assertNotEqual(c, Zm(0, 7) * a)

    def test_zero(self):
        a = PolyUnivar([Zm(1, 7), Zm(2, 7), Zm(3, 7)])
        self.assertEqual(a.zero() + a, a)
        self.assertEqual(a.zero(), Zm(0, 7) * a)

    def test_linearlyIndependent(self):
        a = PolyUnivar([Zm(1, 5), Zm(2, 5), Zm(3, 5)])
        b = PolyUnivar([Zm(2, 5), Zm(3, 5), Zm(4, 5)])
        c = PolyUnivar([Zm(3, 5), Zm(4, 5), Zm(0, 5)])
        d = PolyUnivar([Zm(3, 5), Zm(0, 5), Zm(0, 5)])
        self.assertTrue(a.linearlyIndependent([a, b, d]))
        self.assertFalse(a.linearlyIndependent([a, b, c]))
        self.assertFalse(a.linearlyIndependent([a, b, PolyUnivar([])]))

    def test_pow(self):
        a = PolyUnivar([Zm(1, 7), Zm(2, 7), Zm(3, 7)])
        b = PolyUnivar([Zm(2, 7), Zm(3, 7), Zm(4, 7)])
        c = PolyUnivar([Zm(2, 7), Zm(0, 7), Zm(2, 7), Zm(3, 7), Zm(5, 7)])
        d = PolyUnivar([Zm(2, 7), Zm(0, 7), Zm(2, 7), Zm(3, 7), Zm(6, 7)])
        self.assertEqual(c, a ** b)
        self.assertEqual(c, b ** a)
        self.assertNotEqual(d, a ** b)    

if __name__ == "__main__":
    unittest.main()