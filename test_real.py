import unittest
from real import R, Rn 

class TestRealVectors(unittest.TestCase):
    def setUp(self):
        # Set up unit vectors in R3
        self.i = Rn([1, 0, 0])
        self.j = Rn([0, 1, 0])
        self.k = Rn([0, 0, 1])

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

    def test_inv(self):
        self.assertEqual(R(10) + R.inv(R(10)), R.zero())

    # === Functions to test real vectors =============
    def test_eq(self):
        self.assertEqual(self.i, self.i)
        self.assertNotEqual(self.i, self.j)

    def test_zero(self):
        self.assertEqual(self.i + Rn.zero(3), self.i)

    def test_rmul(self):
        self.assertEqual(Rn([2, 2, 2]), R(2) * Rn([1, 1, 1]))

    def test_mul(self):
        self.assertEqual(10, Rn([1, 2, 3]) * Rn([3, 2, 1]))

    def test_add(self):
        self.assertEqual(Rn([1, 1, 1]), self.i + self.j + self.k)

    def test_linearlyIndependent(self):
        self.assertTrue(Rn.linearlyIndependent([self.i, self.j, self.k]))
        self.assertFalse(Rn.linearlyIndependent([Rn([1, 2, 3]), Rn([1, 4, 9]), Rn([3, 8, 15])]))
        self.assertFalse(Rn.linearlyIndependent([Rn([2, 3, 4]), Rn([5, 6, 3]), Rn([14, 32, 54]), Rn([9, 8, 7])]))

if __name__ == '__main__':
    unittest.main()