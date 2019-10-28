# Defines n dimensional vectors over euclidean space

import vector
import numpy as np 
from numpy.linalg import matrix_rank

class R(vector.Scalar):
    def __init__(self, x):
        self.data = x

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)
    
    def __add__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for + not a real number")
            return NotImplemented
        return R(self.data + x.data)

    def __mul__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for * not a real number")
            return NotImplemented
        return R(self.data * x.data)

    def __eq__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for = not a real number")
            return NotImplemented
        return self.data == x.data

    def __gt__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for > not a real number")
            return NotImplemented
        return self.data > x.data

    def __ge__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for >= not a real number")
            return NotImplemented
        return self.data >= x.data

    def __lt__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for < not a real number")
            return NotImplemented
        return self.data < x.data

    def __le__(self, other):
        if not isinstance(other, R):
            # raise NotImplemented("Second operand for <= not a real number")
            return NotImplemented
        return self.data <= x.data

    @staticmethod
    def zero():
        return R(0)
    
    @staticmethod
    def inv(x):
        if not isinstance(x, R):
            # raise NotImplemented("Operand for (-) is not a real number")
            return NotImplemented
        return R(-x.data)

class Rn(vector.Vector):
    def __init__(self, x):
        self.n = len(x)
        self.data = x

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)

    def __add__(self, other):
        if (not isinstance(other, Rn)):
            # raise NotImplemented("Second vector for + is not of type Rn")
            return NotImplemented
        if (self.n != other.n):
            # raise NotImplemented("Dimensions of vectors do not match for +")
            return NotImplemented
        
        # Return the component wise sum
        return Rn([self.data[i] + other.data[i] for i in range(self.n)])

    def __mul__(self, other):
        # Implements the dot product
        if (not isinstance(other, Rn)):
            # raise NotImplemented("Second vector for dot product is not of type Rn")
            return NotImplemented
        if (self.n != other.n):
            # raise NotImplemented("Dimensions of vectors do not match for dot product")
            return NotImplemented
    
        result = 0
        for i in range(self.n):
            result += (self.data[i] * other.data[i])

        return result

    def __rmul__(self, other):
        # Implements scalar multiplication
        if (not isinstance(other, R)):
            # raise NotImplemented("Scalar for * is not of type R")
            return NotImplemented
    
        return Rn([other.data * self.data[i] for i in range(self.n)])

    def __eq__(self, other):
        if (not isinstance(other, Rn)):
            # raise NotImplemented("Second vector for = is not of type Rn")
            return NotImplemented
        if (self.n != other.n):
            # raise NotImplemented("Dimensions of vectors do not match for =")
            return NotImplemented
        return self.data == other.data

    @staticmethod
    def zero(n):
        return Rn([0 for i in range(n)])

    @staticmethod
    def linearlyIndependent(arr):
        if (len(arr) == 0):
            return True 
        
        n = arr[0].n
        m = len(arr)
        
        for v in arr:
            if (not isinstance(v, Rn)) or v.n != n:
                return NotImplemented
            
        # If the number of vectors is greater than the dimension of the ambient space return False
        if m > n:
            return False 

        M = np.zeros((m, n))
        for i in range(m):
            M[i] = arr[i].data 
        
        return matrix_rank(M) == m 


    
        