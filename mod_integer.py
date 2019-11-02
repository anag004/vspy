# This module implements integers modulo p scalars 

from vector import Scalar
from sympy import mod_inverse

# The integer class Z mod m
class Zm(Scalar):
    def __init__(self, n, m):
        if (not isinstance(n, int)) or (not isinstance(m, int)):
            raise Exception("Arguments must be integers")
        elif m <= 0:
            raise Exception("Modulus must be positive integer")
        else:
            self.data = n % m 
            self.m = m

    def __add__(self, other):
        if (not isinstance(other, Zm)):
            return NotImplemented
        elif (self.m != other.m):
            return NotImplemented
        else:
            return Zm(self.data + other.data, self.m)

    def __mul__(self, other):
        if (not isinstance(other, Zm)):
            return NotImplemented
        elif (self.m != other.m):
            return NotImplemented
        else:
            return Zm(self.data * other.data, self.m)
        
    def __eq__(self, other):
        if (not isinstance(other, Zm)):
            return NotImplemented
        elif (self.m != other.m):
            raise Exception("Cannot compare two modular integers with different moduli")
        else:
            return self.data == other.data

    def __ge__(self, other):
        return NotImplemented

    def __sub__(self, other):
        if (not isinstance(other, Zm)):
            return NotImplemented
        elif (self.m != other.m):
            return NotImplemented
        else:
            return Zm(self.data - other.data, self.m)

    def __truediv__(self, other):
        if (not isinstance(other, Zm)):
            return NotImplemented
        elif (self.m != other.m):
            return NotImplemented
        else:
            return Zm(self.data * mod_inverse(other.data, other.m), self.m)

    def zero(self):
        return Zm(0, self.m)

    @staticmethod
    def inv(x):
        return Zm(-x.data, x.m)