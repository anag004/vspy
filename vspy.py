# The main module which implements the vector space operations

from vector import Vector, Scalar

class VectorSpace:
    # Create a vector space by taking the span of the vectors in arr
    def __init__(self, arr):
        self.basis = []
        for v in arr:
            # Append v to the basis 
            self.basis.append(v)
            if not Vector.linearlyIndependent(self.basis):
                # Remove v if this makes the basis linearly dependent
                del self.basis[-1]

        # Define the dimension of the vector space
        self.dim = len(self.basis)

    # Check if a vector is inside a vector space
    def hasVector(self, v):
        # v lies in the vector space iff the basis augmented with v is linearly dependent
        return not Vector.linearlyIndependent(self.basis + [v])

    # Check if a vector space contains another
    def containsVspace(self, other):
        # If other has a larger dimension, it cannot be contained in self
        if (other.dim > self.dim):
            return False

        # Other is contained in self iff each basis vector of other is contained in self
        for v in other.basis:
            if not self.hasVector(v):
                return False

        return True
    
    def __add__(self, other):
        # Adds two vector spaces 
        return VectorSpace(self.basis + other.basis)

    def __mul__(self, other):
        # Gets the intersection of two vector spaces
        # Choose vectors from other.basis which lie in self
        newBasis = []
        for v in other.basis:
            if self.hasVector(v):
                newBasis.append(v)

        # Create a vector space with this basis
        return VectorSpace(newBasis)
    
    @staticmethod
    def nullSpace():
        # Returns the null space
        return VectorSpace([])


