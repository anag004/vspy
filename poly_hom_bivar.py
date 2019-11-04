# This is the vector space of bivariate homogeneous polynomias

from simple_vectors import SimpleVector

class PolyHomBivar(SimpleVector):
    def __eq__(self, other):
        if not isinstance(other, PolyHomBivar):
            return NotImplemented
        else:
            return self.data == other.data

    # This is polynomial multiplication for homogenous polys
    def __pow__(self, other):
        if not isinstance(other, PolyHomBivar):
            return NotImplemented
        else:
            if (self.n == 0 or other.n == 0):
                return PolyHomBivar([])
            
            zeroElement = self.data[0].zero()
            res_len = self.n + other.n - 1
            res_coeffs = []

            for deg in range(res_len):
                coeff_value = zeroElement
                for i in range(deg + 1):
                    if (i < self.n and deg - i < other.n):
                        coeff_value += self.data[self.n - i - 1] * other.data[other.n - deg + i - 1]
                res_coeffs.append(coeff_value)

            return PolyHomBivar(res_coeffs[::-1])