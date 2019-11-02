# Module defines the  Vector and abstract class Scalar with methods that child classes must implement

import abc

class Vector(abc.ABC):
    @abc.abstractmethod
    def __add__(self, other):
        # Add two vectors
        # Check that the other is a Vector of the same type
        pass 

    @abc.abstractmethod
    def __mul__(self, other):
        # Implements the dot product
        # Check that the other is a Vector of the same type
        pass

    @abc.abstractmethod
    def __rmul__(self, other):
        # Implements scalar multiplication
        # Check that other is a Scalar of the supported type
        pass 

    @abc.abstractmethod
    def __eq__(self, other):
        # Compare two vectors
        # Check that the other is also a Vector of the same type
        pass

    @abc.abstractmethod
    def zero(self):
        # Return the ZERO vector
        pass

    @staticmethod
    @abc.abstractmethod
    def linearlyIndependent(arr):
        # Returns true iff the set of vectors is linearly independent
        # Check if all the vectors are compatible
        pass
    
class Scalar(abc.ABC):
    @abc.abstractmethod
    def __add__(self, other):
        # Add two scalars
        pass

    @abc.abstractmethod
    def __mul__(self, other):
        # Multiply two scalars
        # Check that other is also a Scalar of the same type
        pass 

    def __eq__(self, other):
        # Compare two scalars
        return (self >= other) and (other >= self)

    @abc.abstractmethod
    def __ge__(self, other):
        # Return true iff self >= other 
        # Check that the other is also a Scalar of the same type
        pass 

    def __gt__(self, other):
        # Return true iff self > other
        return self >= other and not (other >= self) 

    def __lt__(self, other):
        # Return true iff self < other
        return other > self 

    def __le__(self, other):
        # Return true iff self <= other
        return other >= self

    def __sub__(self, other):
        # Return self added to the inverse of the other
        return self + self.inv(other)

    @abc.abstractmethod
    def __truediv__(self, other):
        # Return self / other
        # Check that other is a Scalar of the same type and is nonzero
        pass

    @abc.abstractmethod
    def zero(self):
        # Return the ZERO SCALAR
        pass 

    @staticmethod
    @abc.abstractmethod
    def inv(x):
        # Return the inverse of the scalar x
        # Check that x is a Scalar of the given type
        pass 

    
    
