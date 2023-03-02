import numpy as np

# quantum state
class State:
    """
    Amplitude state vector class
    """
    def __init__(self, amp: np.ndarray):
        """
        Initialize the state with a linear numpy array for the amplitudes

        Args:
            amp: linear numpy array of amplitudes
            For a n-qubit quantum state amp must have 2**n entries

            Example |010>:

            psi = State(np.array([0, 0, 1, 0, 0, 0, 0, 0]))
            NOTE: it is up to you to make sure this is a valid quantum state :)
        """
        if self.check(amp):
            self.n = int(np.log2(amp.size))
            self.amp = amp
        else:
            raise Exception("Wrong state input")

    def normalize(self):
        """
        Normalize state
        """
        self.amp = self.amp / np.linalg.norm(self.amp)

    def check(self, amp):
        """
        Check that the array has correct shape
        """
        def isPower2(x):
            return np.ceil(np.log2(x)) == np.floor(np.log2(x))
        return amp.ndim == 1 and amp.size != 0 and isPower2(amp.size)


