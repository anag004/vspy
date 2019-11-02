import unittest
from real import R
from simple_vectors import SimpleVector

class TestRealVectors(unittest.TestCase):
    def setUp(self):
        # Set up unit vectors in R3
        self.i = SimpleVector([R(1), R(0), R(0)])
        self.j = SimpleVector([R(0), R(1), R(0)])
        self.k = SimpleVector([R(0), R(0), R(1)])

    # === Functions to test real scalars =============
    def test_eq(self):
        self.assertEqual(R(21), R(21))
        self.assertNotEqual(R(20), R(21))

    def test_gt(self):
        self.assertTrue(R(21) > R(20))
        self.assertFalse(R(21) > R(21))

    def test_ge(self):
        self.assertTrue(R(20) >= R(20))
        self.assertFalse(R(21) >= R(22))

    def test_lt(self):
        self.assertTrue(R(20) < R(21))
        self.assertFalse(R(21) < R(21))

    def test_le(self):
        self.assertTrue(R(20) <= R(20))
        self.assertFalse(R(22) <= R(21))

    def test_add(self):
        self.assertEqual(R(42), R(29) + R(13))

    def test_zero(self):
        self.assertEqual(R(10), R(10) + R.zero())

    def test_sub(self):
        self.assertEqual(R(10), R(12) - R(2))

    def test_div(self):
        self.assertEqual(R(4), R(16) / R(4))

    def test_inv(self):
        self.assertEqual(R(10) + R.inv(R(10)), R.zero())

    # === Functions to test real vectors =============
    def test_vector_eq(self):
        self.assertEqual(self.i, self.i)
        self.assertNotEqual(self.i, self.j)

    def test_vector_zero(self):
        self.assertEqual(self.i + SimpleVector.zero(3, R.zero()), self.i)

    def test_vector_rmul(self):
        self.assertEqual(SimpleVector([R(2), R(2), R(2)]), R(2) * SimpleVector([R(1), R(1), R(1)]))

    def test_vector_mul(self):
        self.assertEqual(R(10), SimpleVector([R(1), R(2), R(3)]) * SimpleVector([R(3), R(2), R(1)]))

    def test_vector_add(self):
        self.assertEqual(SimpleVector([R(1), R(1), R(1)]), self.i + self.j + self.k)

    def test_vector_linearlyIndependent(self):
        self.assertTrue(SimpleVector.linearlyIndependent([self.i, self.j, self.k], R.zero()))
        self.assertFalse(SimpleVector.linearlyIndependent([SimpleVector([R(1), R(2), R(3)]), SimpleVector([R(1), R(4), R(9)]), SimpleVector([R(3), R(8), R(15)])], R.zero()))
        self.assertFalse(SimpleVector.linearlyIndependent([SimpleVector([R(2), R(3), R(4)]), SimpleVector([R(5), R(6), R(3)]), SimpleVector([R(14), R(32), R(54)]), SimpleVector([R(9), R(8), R(7)])], R.zero()))

if __name__ == '__main__':
    unittest.main()