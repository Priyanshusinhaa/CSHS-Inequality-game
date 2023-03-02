from circuit import circuit

def getWinningProb(thetaA0, thetaA1, thetaB0, thetaB1) -> float:
    """
    Return the probability of winning the game

    Hint: consider the game rules and which outcomes lead to a win
    and which do not
    """
    # TODO
    #Take an average of all four possible charlie could send
    charlie = [(0, 0), (0, 1), (1, 0), (1, 1)]
    send_answer = [(0, 0), (0, 1), (1, 0), (1, 1)]
    final_prob = 0
    for i in range(len(charlie)):
        x, y = charlie[i]
        prob = circuit(x, y, thetaA0, thetaA1, thetaB0, thetaB1)
        for j in range(len(send_answer)):
            a, b = send_answer[j]
            if (x and y) == (a + b)%2:
                if x == 0 and y == 0:
                    final_prob += (prob[0] + prob[-1])/2
                if x == 0 and y == 1:
                    final_prob += (prob[0] + prob[-1])/2
                if x == 1 and y == 0:
                    final_prob += (prob[0] + prob[-1])/2
                if x == 1 and y == 1:
                    final_prob += (prob[1] + prob[2])/2

    return final_prob/4
    pass