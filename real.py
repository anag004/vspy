# Defines real scalars

import vector
from utils import matrix_rank

class R(vector.Scalar):
    def __init__(self, x):
        self.data = x

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)
    
    def __add__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return R(self.data + other.data)

    def __mul__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return R(self.data * other.data)

    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        else:
            return R(self.data * other)

    def __eq__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return self.data == other.data

    def __gt__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return self.data > other.data

    def __ge__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return self.data >= other.data

    def __lt__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return self.data < other.data

    def __le__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        return self.data <= other.data

    def __truediv__(self, other):
        if not isinstance(other, R):
            return NotImplemented
        elif (other == self.zero()):
            raise Exception("Cannot divide by zero")
        else: 
            return R(self.data / other.data)

    def zero(self):
        return R(0)
    
    @staticmethod
    def inv(x):
        if not isinstance(x, R):
            return NotImplemented
        return R(-x.data)

