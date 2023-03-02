
import numpy as np
from state import State
from gates import *


def shot(state: State, idx: int) -> int:
    """
    Simulate the measurement of a specified qubit in the computational base
    This function should modify the input state into the measured state

    Example:
        psi = State(1/np.sqrt(2)*np.array([1, 0, 0, 1]))
        outcome = shot(state, 0)

        If outcome = 0
        psi.amp = np.array([1, 0, 0, 0])
        if outcome = 1
        psi.amp = np.array([0, 0, 0, 1])

    Hint: recall that a measurement is a probabilistic process,
    np.random.random() (or similar rng) can be useful here

    Args:
        state: input state
        idx: qubit to be measured
    Returns:
        measurement outcome (0 or 1)
    """
    # TODO

    # utility function for inner uses
    def term(idx:int, nqubits:int, term:int) -> np.ndarray:
        op = [I.u]*nqubits
        if term == 0:
            op[idx] = P0.u
        if term == 1:
            op[idx] = P1.u
        return tensor(op[::-1])
    # initiating variables
    nqubits = state.n
    p0, p1, id, = P0.u, P1.u, I.u
    psi_ket = np.array([copy(state.amp)])
    psi_bra = psi_ket.conj().T
    # generating terms for calculation of prob and post state
    t0 = term(idx, nqubits, 0)
    t0_dagger = t0.conj().T
    t1 = term(idx, nqubits, 1)
    t1_dagger = t1.conj().T
    # computing probability based on single qubit
    prob0 = np.linalg.multi_dot([psi_bra, t0_dagger, t0, psi_ket][::-1])
    prob1 = np.linalg.multi_dot([psi_bra, t1_dagger, t1, psi_ket][::-1])
    
    # computing post quantum state (state after measurement of single qubit)
    if prob0[0][0] == 0:
        psi_ket1_ = (psi_ket@t1)/np.sqrt(prob1[0][0])
    elif prob1[0][0] == 0:
        psi_ket0_ = (psi_ket@t0)/np.sqrt(prob0[0][0])
    else:
        psi_ket0_ = (psi_ket@t0)/np.sqrt(prob0[0][0])
        psi_ket1_ = (psi_ket@t1)/np.sqrt(prob1[0][0])
    # probablistic process
    outcome = None
    if prob0 == prob1:
        #choose random number {0, 1} if both prob are same
        outcome = np.random.randint(0,2)
        if outcome == 0:
            state.amp = psi_ket0_[0]
        if outcome == 1:
            state.amp = psi_ket1_[0]
    elif prob0 != prob1:
        outcome = np.random.choice([0, 1], p = [prob0[0][0], prob1[0][0]])
        if outcome == 0:
            state.amp = psi_ket0_[0]
        if outcome == 1:
            state.amp = psi_ket1_[0]

    return outcome

    pass