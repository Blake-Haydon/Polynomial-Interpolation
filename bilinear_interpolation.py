import numpy as np
from galois import FieldArray


class BilinearInterpolationPoly:
    """This class enables the creation of a bilinear interpolation polynomial from a set of (x, y, z) values. It is
    based off the following wikipedia pages:
    https://en.wikipedia.org/wiki/Bilinear_interpolation
    https://en.wikipedia.org/wiki/Multilinear_polynomial
    """

    def __init__(self, GF, x: FieldArray, y: FieldArray, z: FieldArray):
        """Creates a bilinear interpolation polynomial from the given x, y, and z values"""

        assert len(x) == len(y) == len(z), "Coordinate arrays must be the same length"

        self.GF = GF
        self.x = x
        self.y = y
        self.z = z
        self.x_elems = np.unique(x)  # Number of unique x values
        self.y_elems = np.unique(y)  # Number of unique y values

        assert len(self.x_elems) * len(self.y_elems) == len(
            x
        ), "(x, y) values must be unique and fully cover the domain"  # TODO: use correct terminology

        self.poly_powers = self._gen_poly_powers()  # Cache as it is used a lot
        self.coefficients = self.interpolate_points(x, y, z)

    def interpolate_points(self, x: FieldArray, y: FieldArray, z: FieldArray):
        """We will aim to solve the equation Ax = z, where A is the multilinear
        polynomial matrix and x are polynomial coefficients."""

        # Generate the A matrix
        A = self.GF.Zeros((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                x_pow = self.poly_powers[j][0]
                y_pow = self.poly_powers[j][1]

                A[i][j] = (x[i] ** x_pow) * (y[i] ** y_pow)

        return np.linalg.solve(A, z)

    def evaluate(self, x, y):
        """Evaluates the polynomial at the given x and y values"""

        total = self.GF(0)
        for i in range(len(self.poly_powers)):
            x_pow = self.poly_powers[i][0]
            y_pow = self.poly_powers[i][1]

            total += self.coefficients[i] * (x**x_pow) * (y**y_pow)

        return total

    def _gen_poly_powers(self):
        """Generates a list of tuples of the powers of x and y.
        e.g. [(0, 0), (1, 0), (0, 1), (1, 1)] would mean:
            f(x, y) = a*x^0*y^0 + b*x^1*y^0 + c*x^0*y^1 + d*x^1*y^1
                    = a + bx + cy + dxy
        """
        return [
            (x_pow, y_pow)
            for x_pow in range(len(self.x_elems))
            for y_pow in range(len(self.y_elems))
        ]

    def __str__(self):
        # Generate the powers of x and y
        poly_powers = self._gen_poly_powers()

        # Generate the polynomial string
        poly_str = "f(x, y) = "
        for i in range(len(poly_powers)):
            poly_str += f"{self.coefficients[i]}"
            if poly_powers[i][0] != 0:
                poly_str += f"x^{poly_powers[i][0]}"
            if poly_powers[i][1] != 0:
                poly_str += f"y^{poly_powers[i][1]}"
            if i != len(poly_powers) - 1:
                poly_str += " + "

        return poly_str
