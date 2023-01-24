import numpy as np
from bilinear_interpolation import BilinearInterpolationPoly


class LookupDFA:
    """Use 2D lookup table to implement a DFA state transition function"""

    def __init__(self, filename: str):
        self.cs = int(0)  # Initialise the current state to 0

        # Load the file into a numpy array and create the lookup table used to find the next state
        arr = np.loadtxt(filename, delimiter=",", dtype=int)
        self.inputs = np.unique(arr[:, 0])
        self.states = np.unique(arr[:, 1])
        self.lookup_table = np.zeros(
            shape=(
                np.max(self.inputs) + 1,
                np.max(self.states) + 1,
            )
        )
        for i in range(len(arr)):
            token, cs, ns = arr[i]
            self.lookup_table[token, cs] = ns

    def transition(self, token: int) -> None:
        # In an accepting state, we can't transition to another state
        if self.cs not in self.states:
            return

        self.cs = self.lookup_table[token, int(self.cs)]

    def current_state(self) -> int:
        return int(self.cs)

    def restart(self):
        self.cs = int(0)


class PolyDFA:
    """Use a multivariate polynomial to implement a DFA state transition function"""

    def __init__(self, GF, filename: str):
        self.cs = int(0)  # Initialise the current state to 0

        # Load the file into a numpy array and create the lookup table used to find the next state
        arr = np.loadtxt(filename, delimiter=",", dtype=int)

        # Generate the polynomial
        self.poly = BilinearInterpolationPoly(
            GF,
            GF(arr[:, 0]),
            GF(arr[:, 1]),
            GF(arr[:, 2]),
        )

    def transition(self, token: int) -> None:
        self.cs = self.poly.evaluate(token, int(self.cs))

    def current_state(self) -> int:
        # FIXME: accepting states are not handled correctly. Once in an accepting state,
        # we can't transition to another state, but we currently can
        return int(self.cs)

    def restart(self):
        self.cs = int(0)
