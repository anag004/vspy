from mod_integer import Zm 
import unittest
from simple_vectors import SimpleVector

class TestModInteger(unittest.TestCase):
    # ==== Tests for the scalar alone =====
    def test_eq(self):
        self.assertEqual(Zm(4, 3), Zm(1, 3))
        self.assertEqual(Zm(-1, 3), Zm(2, 3))

    def test_add(self):
        self.assertEqual(Zm(5, 4), Zm(6, 4) + Zm(3, 4))

    def test_mul(self):
        self.assertEqual(Zm(5, 31), Zm(9, 31) * Zm(4, 31))

    def test_rmul(self):
        self.assertEqual(Zm(5, 31), 9 * Zm(4, 31))

    def test_sub(self):
        self.assertEqual(Zm(1, 4), Zm(9, 4), Zm(12, 4))

    def test_div(self):
        self.assertEqual(Zm(4, 7), Zm(5, 7) / Zm(3, 7))

    def test_zero(self):
        self.assertEqual(Zm(4, self.m), Zm(4, self.m) + self.c.zero())
    
    def test_inv(self):
        x = Zm(4, self.m)
        self.assertEqual(self.c.zero(), Zm.inv(x) + x)

    # ===== Zm can be coupled with the the SimpleVector class ===  
    def setUp(self):
        self.m = 31
        self.i = SimpleVector([Zm(1, self.m), Zm(0, self.m), Zm(0, self.m)])
        self.j = SimpleVector([Zm(0, self.m), Zm(1, self.m), Zm(0, self.m)])
        self.k = SimpleVector([Zm(0, self.m), Zm(0, self.m), Zm(1, self.m)])
        self.c = Zm(0, self.m)

    def test_vector_eq(self):
        self.assertEqual(self.i, self.i)

    def test_vector_zero(self):
        self.assertEqual(self.i + self.i.zero(), self.i)
    
    def test_vector_rmul(self):
        self.assertEqual(SimpleVector([Zm(2, self.m), Zm(0, self.m), Zm(0, self.m)]), Zm(2, self.m) * self.i)

    def test_vector_mul(self):
        self.assertEqual(Zm(10, self.m), SimpleVector([Zm(1, self.m), Zm(2, self.m), Zm(3, self.m)]) * SimpleVector([Zm(3, self.m), Zm(2, self.m), Zm(1, self.m)]))

    def test_vector_add(self):
        self.assertEqual(SimpleVector([Zm(1, self.m), Zm(1, self.m), Zm(1, self.m)]), self.i + self.j + self.k)

    def test_vector_linearlyIndependent(self):
        self.assertTrue(SimpleVector.linearlyIndependent([self.i, self.j, self.k]))
        self.assertFalse(SimpleVector.linearlyIndependent([SimpleVector([Zm(1, self.m), Zm(2, self.m), Zm(3, self.m)]), SimpleVector([Zm(1, self.m), Zm(35, self.m), Zm(9, self.m)]), SimpleVector([Zm(34, self.m), Zm(-23, self.m), Zm(15, self.m)])]))
        self.assertFalse(SimpleVector.linearlyIndependent([SimpleVector([Zm(2, self.m), Zm(34, self.m), Zm(4, self.m)]), SimpleVector([Zm(5, self.m), Zm(6, self.m), Zm(3, self.m)]), SimpleVector([Zm(14, self.m), Zm(32, self.m), Zm(54, self.m)]), SimpleVector([Zm(9, self.m), Zm(8, self.m), Zm(7, self.m)])]))

if __name__ == "__main__":
    unittest.main()