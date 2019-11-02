import unittest
from utils import matrix_rank
from real import R
import numpy as np

class TestUtils(unittest.TestCase):
    def testSquare1Rank1(self):
        # Tests for a 1x1 square matrix of rank 1
        M = [[R(1)]]
        self.assertEqual(1, matrix_rank(M))
    
    def testSquare1Rank0(self):
        # Tests for a 1x1 square matrix of rank 0
        M = [[R(0)]]
        self.assertEqual(0, matrix_rank(M))

    def testSquare2Rank2(self):
        # Tests for a 2x2 square matrix of rank 2
        M = [[R(1), R(2)], [R(3), R(4)]]
        self.assertEqual(2, matrix_rank(M))
    
    def testSquare2Rank1(self):
        # Tests for a 2x2 square matrix of rank 1
        M = [[R(1), R(2)], [R(4), R(8)]]
        self.assertEqual(1, matrix_rank(M))
    
    def testSquare2Rank0(self):
        # Tests for a 2x2 square matrix of rank 1
        M = [[R(0), R(0)], [R(0), R(0)]]
        self.assertEqual(0, matrix_rank(M))

    def testSquare3Rank3(self):
        # Tests for a 3x3 square matrix of rank 3
        M = [[R(1), R(1), R(1)],
             [R(1), R(2), R(3)],
             [R(1), R(4), R(9)]]
        self.assertEqual(3, matrix_rank(M))
    
    def testSquare3Rank2(self):
        # Tests for a 3x3 square matrix of rank 2
        M = [[R(1), R(1), R(1)],
             [R(1), R(2), R(3)],
             [R(5), R(9), R(13)]]
        self.assertEqual(2, matrix_rank(M))

    def testSquare3Rank1(self):
        # Tests for a 3x3 square matrix of rank 1
        M = [[R(3), R(6), R(9)],
             [R(1), R(2), R(3)],
             [R(5), R(10), R(15)]]
        self.assertEqual(1, matrix_rank(M))
    
    def testSquare3Rank0(self):
        # Tests for a 3x3 square matrix of rank0
        M = [[R(0), R(0), R(0)],
             [R(0), R(0), R(0)],
             [R(0), R(0), R(0)]]
        self.assertEqual(0, matrix_rank(M))

    def test2by1Rank1(self):
        # Test for 2x1 square matrix of rank 1
        M = [[R(1)], [R(2)]]
        self.assertEqual(1, matrix_rank(M))

    def test1by2Rank1(self):
        # Test for 1x2 square matrix of rank 1
        M = [[R(1), R(2)]]
        self.assertEqual(1, matrix_rank(M))

    def test2by3Rank1(self):
        # Test for 2x3 square matrix of rank 1
        M = [[R(1), R(2), R(3)], [R(2), R(4), R(6)]]
        self.assertEqual(1, matrix_rank(M))
    
    def test2by3Rank2(self):
        # Test for 2x3 square matrix of rank 2
        M = [[R(1), R(2), R(3)], [R(2), R(4), R(5)]]
        self.assertEqual(2, matrix_rank(M))

    def test3by2Rank1(self):
        # Test for 3x2 square matrix of rank 1
        M = [[R(1), R(2)], [R(2), R(4)], [R(3), R(6)]]
        self.assertEqual(1, matrix_rank(M))
    
    def test3by2Rank2(self):
        # Test for 2x3 square matrix of rank 2
        M = [[R(1), R(2)], [R(2), R(4)], [R(3), R(5)]]
        self.assertEqual(2, matrix_rank(M))    

    def test4by5Rank3(self):
        # Test for 4x5 square matrix of rank 3
        M = [[R(1), R(0), R(-2), R(1), R(0)],
             [R(0), R(-1), R(-3), R(1), R(3)],
             [R(-2), R(-1), R(1), R(-1), R(3)],
             [R(0), R(3), R(9), R(0), R(-12)]]
        self.assertEqual(3, matrix_rank(M))

    def testSquare5Rank3(self):
        # Test a 5by5 square matrix with rank 3
        M = [[R(1), R(1), R(4), R(1), R(2)],
            [R(0), R(1), R(2), R(1), R(1)],
            [R(0), R(0), R(0), R(1), R(2)],
            [R(1), R(-1), R(0), R(0), R(2)],
            [R(2), R(1), R(6), R(0), R(1)]]
        self.assertEqual(3, matrix_rank(M))

    def testRandomMats(self):
        # Test random matrices against the numpy.linalg matrix_rank method
        size_max = 2
        high = 5
        for m in range(1, size_max + 1):
            for n in range(1, size_max + 1):
                with self.subTest(msg="Testing for a random " + str(m) + "x" + str(n) + "matrix"):
                    # Make a random numpy array 
                    M = np.random.randint(high, size=(m,n))
                    # Copy that array into an R array
                    M1 = [[R.zero() for i in range(n)] for j in range(m)]
                    for i in range(m):
                        for j in range(n):
                            M1[i][j] = R(M[i][j])
                    
                    # Test equality
                    self.assertEqual(np.linalg.matrix_rank(M), matrix_rank(M1))
                
# ===== OLD CODE TO GENERATE TESTS ==========
# # Use this to create random tests for a matrix of size m, n
# def create_test(m, n, high):
#     def do_test_expected(self):
#         # Make a random numpy array 
#         M = np.random.randint(high, size=(m,n))
#         # Copy that array into an R array
#         M1 = [[R.zero() for i in range(n)] for j in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 M1[i][j] = R(M[i][j])
            
#         self.assertEqual(np.linalg.matrix_rank(M), matrix_rank(M1))

#     return do_test_expected

# # Generate tests 
# size_max = 100
# high = 5
# for i in range(1, size_max + 1):
#     for j in range(1, size_max + 1):
#         test_method = create_test(i, j, high)
#         test_method.__name__ = "random_test_" + str(i) + "by" + str(j)
#         print("Generating test: ", test_method.__name__)
#         setattr(TestUtils, test_method.__name__, test_method)

if __name__ == "__main__":
    unittest.main()