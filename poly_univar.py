# This module implements the vector of homogenous bivariate polynomial 
# The coefficients can be derived from any scalar class

from simple_vectors import Vector
from utils import matrix_rank

class PolyUnivar(Vector):
    def __init__(self, arr):
        # Initialize the polynomial with coefficients
        if (len(arr) == 0):
            self.coeffs = []
            self.deg = 0
        elif (arr[0] == arr[0].zero()):
            raise Exception("The first coefficient of a polynomial cannot be zero")
        else:
            self.coeffs = arr
            self.deg = len(arr)

    def __repr__(self):
        return "(" + repr(self.coeffs) + ", " + repr(self.deg) + ")"

    def __add__(self, other):
        # If the degree of the other is more, swap the two variables
        if (self.deg < other.deg):
            self, other = other, self

        offset = self.deg - other.deg

        if (self.deg == 0):
            return PolyUnivar([])
        
        # Copy the first self.deg - other.deg coeffs
        result = [self.coeffs[i] for i in range(offset)]
    
        # Add the remaining values
        for i in range(other.deg):
            result.append(other.coeffs[i] + self.coeffs[i + offset])

        # Remove leading zeros 
        zeroElement = self.coeffs[0].zero()
        ctr = 0
        maxctr = len(result)
        while(ctr < maxctr):
            if (result[ctr] == zeroElement):
                ctr += 1
            else:
                break 
        result = result[ctr:]

        return PolyUnivar(result)

    def __mul__(self, other):
        if (self.deg < other.deg):
            self, other = other, self 

        if (other.deg == 0):
            if (self.deg == 0):
                return 0
            else:
                return self.coeffs[0].zero()

        result = self.coeffs[0].zero()
        offset = self.deg - other.deg
        
        for i in range(other.deg):
            result = result + self.coeffs[i + offset] * other.coeffs[i]
        
        return result 

    def __rmul__(self, other):
        if (other == other.zero()):
            return PolyUnivar([])

        result = []

        for i in range(self.deg):
            result.append(other * self.coeffs[i])
        
        return PolyUnivar(result)

    def __eq__(self, other):
        return self.coeffs == other.coeffs 

    def zero(self):
        return PolyUnivar([])

    def linearlyIndependent(self, arr):
        m = len(arr)

        # The empty set is linearly independent
        if (m == 0):
            return True

        # Find the maximal degree and a zero element 
        maxDegree = 0
        zeroElement = None

        for p in arr:
            maxDegree = max(maxDegree, p.deg)
            if (p.deg > 0 and zeroElement == None):
                zeroElement = p.coeffs[0].zero()
        
        if maxDegree == 0:
            return False

        M = [[zeroElement for i in range(maxDegree)] for j in range(m)]

        for i in range(m):
            offset = maxDegree - arr[i].deg 
            for j in range(offset):
                M[i][j] = zeroElement
            
            for j in range(arr[i].deg):
                M[i][j + offset] = arr[i].coeffs[j]

        return matrix_rank(M) == m

    # This is polynomial multiplication (not strictly a vector operation)
    def __pow__(self, other):
        if not isinstance(other, PolyUnivar):
            return NotImplemented
        else:
            if (self.deg == 0 or other.deg == 0):
                return PolyUnivar([])
            
            zeroElement = self.coeffs[0].zero()
            res_deg = self.deg + other.deg 
            res_coeffs = []

            for deg in range(res_deg):
                coeff_value = zeroElement
                for i in range(deg + 1):
                    if (i < self.deg and deg - i < other.deg):
                        coeff_value += self.coeffs[self.deg - i - 1] * other.coeffs[other.deg - deg + i - 1]
                res_coeffs.append(coeff_value)
            
            res_coeffs.reverse()

            # Remove leading zeros 
            ctr = 0
            ctr_max = len(res_coeffs)

            while(ctr < ctr_max):
                if res_coeffs[ctr] == zeroElement:
                    ctr+=1
                else:
                    break 

            res_coeffs = res_coeffs[ctr:]
            
            return PolyUnivar(res_coeffs)


