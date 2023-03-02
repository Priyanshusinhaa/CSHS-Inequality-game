import numpy as np
from state import State
from gates import *
from measure import measure


def circuit(x, y, thetaA0, thetaA1, thetaB0, thetaB1) -> np.ndarray:
    """
    CHSH game circuit, as shown in the README.md file

    Return:
        prob: 2**n array of probabilities
    Probability for each of the 2**n computational base states
    """
    state_list = [np.array([1, 0]), np.array([1, 0])]
    psi = State(tensor(state_list))
    # bell state preparation
    H(psi, 0)
    CNOT(psi, (0,1))
    # change base
    thetaA = thetaA0
    thetaB = thetaB0
    if x == 1:
        thetaA = thetaA1
    if y == 1:
        thetaB = thetaB1
    UA = makeUTheta(thetaA)
    UB = makeUTheta(thetaB)
    UA(psi, 0)
    UB(psi, 1)
    # measure
    shots = 100 # you can change this to speed up the simulation
    prob = measure(psi, shots) / shots
    return prob
