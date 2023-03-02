from optimization import *

def main():
    iteration = 10
    for i in range(iteration):
        solution, evaluation = optimize()
        winning_percent = (1-evaluation)*100
        print('Winning Percentage: %.2f' % winning_percent, '\n')

    pass


if __name__ == '__main__':
    main()