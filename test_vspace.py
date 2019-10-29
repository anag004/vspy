import unittest
from vspy import VectorSpace
from real import Rn, R

class TestVectorSpace(unittest.TestCase):
    def setUp(self):
        self.i = Rn([1, 0, 0])
        self.j = Rn([0, 1, 0])
        self.k = Rn([0, 0, 1])
        self.x = VectorSpace([self.i])
        self.y = VectorSpace([self.j])
        self.z = VectorSpace([self.k])
        self.xy = VectorSpace([self.i, self.j])
        self.yz = VectorSpace([self.j, self.k])
        self.zx = VectorSpace([self.k, self.i])
        self.xyz = VectorSpace([self.i, self.j, self.k])

    def test_contains(self):
        # Check that the i + 2j lies in the xy plane
        self.assertIn(self.i + R(2) * self.j, self.xy)
        # Check that i + 2k does not lie in the xy planes
        self.assertNotIn(self.i + R(2) * self.k, self.xy)

    def test_ge(self):
        self.assertGreaterEqual(self.xyz, self.xy)
        self.assertFalse(self.xy >= self.yz)
    
    def test_gt(self):
        self.assertGreater(self.xyz, self.xy)
        self.assertFalse(self.xy > self.yz)

    def test_le(self):
        self.assertLessEqual(self.xy, self.xyz)
        self.assertFalse(self.xy < self.yz)
    
    def test_lt(self):
        self.assertLess(self.xy, self.xyz)
        self.assertFalse(self.xy <= self.yz)
        
    def test_eq(self):
        # Test that self.xyz = span(i + j, j + k, k + i)
        self.assertEqual(self.xyz, VectorSpace([self.i + self.j, self.j + self.k, self.k + self.i]))
        # Test that self.xyz != span(i + j, k, i + j + k)
        self.assertNotEqual(self.xyz, VectorSpace([self.i + self.j, self.k, self.i + self.j + self.k]))

    def test_add(self):
        # Test that xy and yz together become xyz
        self.assertEqual(self.xyz, self.xy + self.yz)
        # Test that xy and x together are not xyz
        self.assertNotEqual(self.xyz, self.x + self.xy)

    def test_mul(self):
        # Test that intersection of xy and yz is y
        self.assertEqual(self.xy * self.yz, self.y)
        # Test that the intersection of xy and xyz is not x
        self.assertNotEqual(self.xyz * self.xy, self.x)

    def test_null(self):
        # Test that the addition of self.xy and null is self.xy
        self.assertEqual(self.xy, self.xy + VectorSpace.nullSpace())

if __name__ == '__main__':
    unittest.main()
