# Polynomial Interpolation

Contains implementations for the [Lagrange](https://en.wikipedia.org/wiki/Lagrange_polynomial) polynomial interpolation methods.
These notebooks are used for my own learning and are not intended to be a complete reference.

## **Notebooks**

- **1 Dimensional Interpolation $f(x)$**
  - [Simple Examples](polynomial_interpolation.ipynb): Polynomial interpolation using libraries over real numbers and finite fields
  - [Lagrange Interpolation](lagrange_interpolation.ipynb): Implementation of Lagrange interpolation using finite fields
  - [Matrix Interpolation](matrix_interpolation.ipynb): Polynomial interpolation over finite fields using matrices
  - [Precomputed Inverse Vandermonde Matrix](precomputed_V_inv.ipynb): By fixing input values we can pre-compute $V(\bf{x})^{-1}$ to speed up interpolation
  - [Fast Interpolation for 2^n - 1 Elements](fast_2^n_interpolation.ipynb): By fixing the input values we can quickly compute a inverse Vandermonde matrix for $2^n - 1$ inputs
  - [Multiprocessor Interpolation for 2^n - 1 Elements](MPI_interpolation.py): Using MPI to speed up the previous notebook for $2^n - 1$ inputs (run using `mpiexec -n 4 python -m mpi4py MPI_interpolation.py`)
  - [INCOMPLETE: Fast Interpolation for n Elements](fast_generic_interpolation.ipynb): By fixing the input values we can quickly compute a inverse Vandermonde matrix for $n$ inputs. This is a generalization of the previous notebook.
- **2 Dimensional Interpolation $f(x, y)$**
  - [Bilinear Interpolation](bilinear_interpolation.ipynb): Polynomial interpolation using the bilinear interpolation method

 <!-- TODO: Newton Interpolation: [Explanation and Examples](newton_interpolation.ipynb) -->
   <!-- TODO: Neville's algorithm: https://en.wikipedia.org/wiki/Neville%27s_algorithm -->
