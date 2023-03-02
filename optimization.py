import numpy as np
import scipy.optimize
from costFunction import cost

def optimize():
    """                 
    Run optimization routine
    This function tries to minimize the 'cost' function
    finding the optimal values of the theta angles
    thetaA0, thetaA1, thetaB0, thetaB1

    Returns:
        solution: array of optimized parameters
        evaluation: value of optimized cost function

    """
    # if you want to to  speedup/improve the optimization part you can play around with
    # the  optimization parameters and algorithms but this is not required :)
    # start = np.array([0.8, 1.5, 0.4, 0.6])
    start = np.array([0, np.pi/4, np.pi/8, -np.pi/8])

    bounds = [(-np.pi/2, np.pi/2), (-np.pi/2., np.pi/2), (-np.pi/2., np.pi/2), (-np.pi/2., np.pi/2)]
    options = {'eps': 0.6e-05}
    result = scipy.optimize.minimize(cost, start, method='L-BFGS-B', bounds=bounds, options=options)
    print('Status : %s' % result['message'])
    print('Total Evaluations: %d' % result['nfev'])
    # evaluate solution
    solution = result['x']
    evaluation = cost(solution)
    print('Solution: f(%s) = %.3f' % (solution, evaluation))
    return solution, evaluation
