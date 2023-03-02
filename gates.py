import numpy as np
from copy import copy
from typing import Tuple, Union
from utilityFunctions import tensor
from state import State

#  gates
class Gate:
    """
    Quantum gate base class
    """

    u = None # unitary representation of gate
    op = None # n-qubit representation of operator

    def __init__(self, state: State, idx: Union[int, Tuple[int, ...]]):
        """
        Apply gate to state, specifying indices

        Args:
            state: quantum state to apply the gate to
            idx: index or tuple of indices of target qubit(s)
        """
        self.check(state, idx)
        self.n = state.n
        self.idx = idx
        self.makeOp()
        self.apply(state)

    def check(self, state: State, idx: int):
        """
        Checks if specified index is in qubit range

        Args:
            state: quantum state to apply the gate to
            idx: index of target qubit
        """
        n = state.n
        if not (n > idx):
            raise Exception("Index out of bounds for given state")
        pass

    def makeOp(self):
        """
        Create n-qubit operator op to apply to n-qubit state
        from matrix representation of gate u

            u: matrix representation of gate

                Example:
                Z.u = np.array([[1, 0], [0, -1]])

            op: n-qubit operator to be applied to a n-qubit state

                Example:
                psi = np.array([1, 0, 0, 0])
                Z gate on qubit 0 is (Z x I)
                Z.op = tensor([Z.u, I.u])
        """
        pass

    def apply(self, state: State):
        """
        Apply n-qubit operator op to n-qubit state

        Args:
            state: quantum state to apply the gate to
        """
        state.amp = np.dot(self.op, state.amp)

class OneQubitGate(Gate):
    """
    Single qubit gate class
    """
    def makeOp(self):
        """
        Create op by applying u to the specified qubit and
        identity to every other qubit in the n-qubit state
        """
        id = I.u
        gate_list = [self.u if i is self.idx else id for i in range(self.n)]
        self.op = tensor(gate_list[::-1])

class Projector(OneQubitGate):
    """
    Projector operator class

    Project method computes the projected state amplitudes and norm
    but does not apply the operation on the state
    """
    def apply(self, state: State):
        """
        Compute and store projected state and norm and store them
        State is not modified (see shot() function)
        """
        self.proj_amp = np.dot(self.op, state.amp)
        self.proj_norm = np.linalg.norm(self.proj_amp)

    def project(self):
        """
        Returns projected amplitude array and its norm
        """
        return self.proj_amp, self.proj_norm

# implementations
class P0(Projector):
    """
    Implementation of P0: |0><0|
    """
    u = np.array([[1,0],[0,0]])

class P1(Projector):
    """
    Implementation of P1: |1><1|
    """
    u = np.array([[0,0],[0,1]])


# implementations
class I(OneQubitGate):
    """
    Implementation of identity
    """
    u = np.eye(2)

class H(OneQubitGate):
    """
    Implementation of Hadamard
    """
    u = 1/np.sqrt(2) * np.array([[1., 1.], [1., -1.]])

class X(OneQubitGate):
    """
    Implementation of X
    """
    u = np.array([[0., 1.], [1., 0.]])

class ControlledGate(Gate):
    """
    Two qubit controlled gate

    Requires a tuple of two indices, labeled as (control, target)
    """
    def check(self, state: State, idx: Tuple[int, int]):
        """
        Checks that two indieces are provided
        """
        if len(idx) !=2:
            raise Exception("Two indices required")
        for i in idx:
            super(ControlledGate, self).check(state, i)

    def makeOp(self):
        """
        Create op for controlled gate

        Hint: in this case it can be very convenient to
        use gate decomposition

        Example:
            psi = State(np.array([1, 0, 0, 0]))
            You can apply CNOT(0, 1) by decomposing into:
                CNOT(0, 1) = |0><0| X I + |1><1| x X
                with x being the tensor product
            Applying the state on psi is just a matter of
            CNOT(psi, (0,1)) #0 control, 1 target
        """
        # TODO
        # Initiating Variable and operator
        id, x, p0, p1 = I.u, X.u, P0.u, P1.u
        term1, term2 = [], [] 
        ctrl, trgt = self.idx
        nqubits = self.n
        #create a term1 and term2 list for cnot
        term1 = [id]*nqubits
        term2 = [id]*nqubits
        term1[ctrl] = p0
        term2[ctrl] = p1
        term2[trgt] = x
        #cnot unitary
        cnot_u = tensor(term1[::-1]) + tensor(term2[::-1])
        self.op = cnot_u

        pass

# implementation
class CNOT(ControlledGate):
    """
    Implementation of CNOT
    """
    u = X.u

def makeUTheta(theta: float) -> OneQubitGate:
    """
    Make parametric unitary gate U that changes state representation to rotated base
    The rotated base is described in README.md

    Args:
        theta: angle
    Returns:
        UTheta:
            unitary gate applying the change of base to a state
    """
    # TODO
    # Initiate unitary gate
    class U(OneQubitGate):
        u = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return U
    pass