# Module defines the abstract classes Vector and Scalar with methods that child classes must implement

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

    @staticmethod
    @abc.abstractmethod
    def zero():
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

    @abc.abstractmethod
    def __eq__(self, other):
        # Compare two scalars
        # Check that the other is also a Scalar of the same type
        pass 

    @abc.abstractmethod
    def __gt__(self, other):
        # Return true iff self > other 
        # Check that the other is also a Scalar of the same type
        pass 

    @abc.abstractmethod
    def __ge__(self, other):
        # Return true iff self >= other
        # Check that the other is also a Scalar of the same type
        pass 

    @abc.abstractmethod
    def __lt__(self, other):
        # Return true iff self < other
        # Check that the other is also a Scalar of the same type
        pass 

    @abc.abstractmethod
    def __le__(self, other):
        # Return true iff self <= other
        # Check that the other is also a Scalar of the same type
        pass 

    @staticmethod
    @abc.abstractmethod
    def zero():
        # Return the ZERO SCALAR
        pass 

    @staticmethod
    @abc.abstractmethod
    def inv(x):
        # Return the inverse of the scalar x
        # Check that x is a Scalar of the given type
        pass 

    
    
