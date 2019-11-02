# Defines simple vectors which add component wise 

from vector import Vector
from utils import matrix_rank

class SimpleVector(Vector):
    def __init__(self, x):
        self.n = len(x)
        self.data = x

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)

    def __add__(self, other):
        if (not isinstance(other, SimpleVector)):
            return NotImplemented
        if (self.n != other.n):
            return NotImplemented
        
        # Return the component wise sum
        return SimpleVector([self.data[i] + other.data[i] for i in range(self.n)])

    def __mul__(self, other):
        # Implements the dot product
        if (not isinstance(other, SimpleVector)):
            return NotImplemented
        if (self.n != other.n):
            return NotImplemented
    
        result = self.data[0].zero()
        for i in range(self.n):
            result += (self.data[i] * other.data[i])

        return result

    def __rmul__(self, other):
        # Implements scalar multiplication
        return SimpleVector([other * self.data[i] for i in range(self.n)])

    def __eq__(self, other):
        if (not isinstance(other, SimpleVector)):
            return NotImplemented
        if (self.n != other.n):
            return NotImplemented
        return self.data == other.data

    def zero(self):
        zeroElement = self.data[0].zero()
        return SimpleVector([zeroElement for i in range(self.n)])

    @staticmethod
    def linearlyIndependent(arr):
        if (len(arr) == 0):
            return True 
        
        n = arr[0].n
        m = len(arr)
        
        for v in arr:
            if (not isinstance(v, SimpleVector)) or v.n != n:
                return NotImplemented
            
        # If the number of vectors is greater than the dimension of the ambient space return False
        if m > n:
            return False 

        # Make a matrix of zeros
        zeroVector = arr[0].zero()
        M = [zeroVector.data for j in range(m)]

        for i in range(m):
            M[i] = arr[i].data 
        
        return matrix_rank(M) == m 


    
        