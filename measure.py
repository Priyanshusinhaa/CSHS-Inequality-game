import numpy as np
from copy import copy
from state import State
from shot import shot


def measure(state: State, n_shots: int) -> np.ndarray:
    """
    Measure n_shots of all qubits state in the computational base

    Args:
        state: n qubit state
        n_shots: number of shots

    Return:
        counts: 2**n array of counts
        Number of counts for each of the 2**n computational base states
    """
    n = state.n
    counts = np.zeros(2**n)

    for s in range(n_shots):
        state_copy = copy(state)
        for i in range(n):
            shot(state_copy, i)
        outcome = state_copy.amp
        outcome_idx = np.flatnonzero(outcome)
        if len(outcome_idx) != 1:
            print("Outcome:\n", outcome)
            raise Exception("Invalid measurement outcome: check your input")
        else:
            counts[outcome_idx[0]] += 1
    return counts