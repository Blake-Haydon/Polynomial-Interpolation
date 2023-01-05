# Polynomial Interpolation

Contains implementations for the [Lagrange](https://en.wikipedia.org/wiki/Lagrange_polynomial) and [Newton](https://en.wikipedia.org/wiki/Newton_polynomial) polynomial interpolation methods.
These notebooks are used for my own learning and are not intended to be a complete reference.

- [Simple Examples](polynomial_interpolation.ipynb): Polynomial interpolation over real numbers and finite fields
- [Lagrange Interpolation](lagrange_interpolation.ipynb): Implementation of Lagrange interpolation using finite fields
- [Matrix Interpolation](matrix_interpolation.ipynb): Polynomial interpolation over finite fields using matrices
- [Precomputed Inverse Vandermonde Matrix](precomputed_V_inv.ipynb): By fixing input values we can pre-compute $V(\bf{x})^{-1}$ to speed up interpolation
- [Fast Interpolation for $2^n - 1$ Elements](fast_2^n_interpolation.ipynb): By fixing the input values we can quickly compute a inverse Vandermonde matrix for $2^n - 1$ inputs
-
- [INCOMPLETE: Fast Interpolation for $n$ Elements](fast_generic_interpolation.ipynb): By fixing the input values we can quickly compute a inverse Vandermonde matrix for $n$ inputs. This is a generalization of the previous notebook.

<!-- TODO: Newton Interpolation: [Explanation and Examples](newton_interpolation.ipynb) -->
<!-- TODO: Neville's algorithm: https://en.wikipedia.org/wiki/Neville%27s_algorithm -->
