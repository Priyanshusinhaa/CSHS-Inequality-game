from winningProbability import getWinningProb

def cost(v) -> float:
    """
    Cost function

    Arguments:
        v: array of optimization parameters,
        i.e. thetaA0, thetaA1, thetaB0, thetaB1
    """
    return 1 - getWinningProb(*v)