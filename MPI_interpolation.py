import galois
import numpy as np
from mpi4py import MPI

######################## HOW TO RUN #########################
# Run with 4 processors:                                    #
# `mpiexec -n 4 python -m mpi4py MPI_interpolation.py`      #
#############################################################


def eval_poly(poly: galois.Poly, x: int):
    # Because the polynomial is generated from a Vandermonde matrix with a primitive element as the base of
    # the exponent we must evaluate slightly differently.
    return poly(poly.field.primitive_element**x)


def MPI_iterative_interpolation(
    GF: galois.GF,
    y: galois.FieldArray,
    rank: int,
    size: int,
) -> np.ndarray:
    assert len(y) == GF.order - 1
    assert rank < size

    # Flip first row of the Vandermonde matrix to get the inverse as per trick in previous notebook
    V_row_flip = GF.Vandermonde(GF.primitive_element, 2, len(y))[1]
    V_row_flip[1:] = np.flip(V_row_flip[1:], 0)

    # Calculate the coefficients of the polynomial one by one
    # This keeps the memory usage low as we do not need the entire Vandermonde matrix
    coefficients = GF.Zeros(len(y))
    for i in range(rank, len(y), size):
        coefficients[i] = V_row_flip**i @ y

    return np.array(np.flip(coefficients))


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    N = 2**3
    NUM_POINTS = N - 1
    GF = galois.GF(N)

    # Random values to interpolate
    # by setting the seed they are all the same and we do not need to pass around values
    y = GF.Random(NUM_POINTS, seed=0)

    # Calculate the coefficients of the polynomial
    coefficients = MPI_iterative_interpolation(GF, y, rank, size)

    # Send the results to rank 0
    if rank != 0:
        comm.send(coefficients, dest=0)

    # Let rank 0 combine the results and check that the polynomial is correct
    if rank == 0:
        coefficients = GF(coefficients)
        for i in range(1, size):
            coefficients += GF(comm.recv(source=i))

        poly = galois.Poly(coefficients)

        for i in range(NUM_POINTS):
            assert eval_poly(poly, i) == y[i]

    MPI.Finalize()
