# The main module which implements the vector space operations

from vector import Vector, Scalar

class VectorSpace:
    # Create a vector space by taking the span of the vectors in arr
    def __init__(self, arr):
        self.basis = []
        for v in arr:
            # Append v to the basis 
            self.basis.append(v)
            if not v.linearlyIndependent(self.basis):
                # Remove v if this makes the basis linearly dependent
                del self.basis[-1]

        # Define the dimension of the vector space
        self.dim = len(self.basis)

    # Return a basis array for debugging purposes -- no __str__ because space has no canonical basis
    def __repr__(self):
        return repr(self.basis)

    # Check if a vector is inside a vector space
    def __contains__(self, v):
        # v lies in the vector space iff the basis augmented with v is linearly dependent
        return not v.linearlyIndependent(self.basis + [v])

    # Check if a vector space contains another (overload the >= operator)
    def __ge__(self, other):
        # If other has a larger dimension, it cannot be contained in self
        if (other.dim > self.dim):
            return False

        # Other is contained in self iff each basis vector of other is contained in self
        for v in other.basis:
            if v not in self:
                return False

        return True

    # Check if other contains self
    def __le__(self, other):
        return other >= self 

    # Check if self strictly contains other
    def __gt__(self, other):
        # self contains other, but other does not contain self
        return (other <= self) and (not (self <= other))

    # Check if other strictly contains self
    def __lt__(self, other):
        # other strictly contains self
        return (other > self)

    # Check if self and other are the same vector space
    def __eq__(self, other):
        # Vector spaces are equal iff they contain each other
        return (self <= other) and (self >= other)
        
    def __add__(self, other):
        # Adds two vector spaces 
        return VectorSpace(self.basis + other.basis)

    def __xor__(self, other):
        # Gets the intersection of two vector spaces
        # Choose vectors from other.basis which lie in self
        newBasis = []
        for v in other.basis:
            if v in self:
                newBasis.append(v)

        # Create a vector space with this basis
        return VectorSpace(newBasis)
    
    @staticmethod
    def nullSpace():
        # Returns the null space
        return VectorSpace([])

