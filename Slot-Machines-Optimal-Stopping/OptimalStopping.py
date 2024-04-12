import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random
def main():
    """
    Set up:
    Starting Balance: 1000 Qi coins
    Number of games: 1000
    Game Results: List of floats: 1.0-100.0 from uniform draw
        0-60.0: no reward
        60.0-80.0: amount paid * 2
        80.0-90.0: amount paid * 3
        90.0-98.0: amount paid * 5
        98.0-99.0: amount paid * 30
        99.0-99.3: amount paid * 80
        99.3-99.5: amount paid * 120
        99.5-99.75: amount paid * 200
        99.75-99.84: amount paid * 500
        99.84-99.9: amount paid * 1000
        99.9-100.0: amount paid * 1000

    luck is normal (no luck buffs)
    """
    # Amount paid is 100
    startingBalance = 1000
    amountPaid = 100
    numGames = 1000
    mixed = 0

    op_stop = optimal_stopping(startingBalance, mixed, numGames, amountPaid)
    numPos = findBestCandidate(op_stop, numGames, startingBalance, mixed, amountPaid)
    print("Optimal Stop of", op_stop * 100, "% had an accuracy of", numPos, "%")

    # Amount paid is 10
    startingBalance = 1000
    amountPaid = 10
    numGames = 1000
    mixed = 0

    op_stop = optimal_stopping(startingBalance, mixed, numGames, amountPaid)
    numPos = findBestCandidate(op_stop, numGames, startingBalance, mixed, amountPaid)
    print("Optimal Stop of", op_stop * 100, "% had an accuracy of", numPos, "%")

    # Amount paid is mixed
    startingBalance = 1000
    numGames = 1000
    mixed = 1

    op_stop = optimal_stopping(startingBalance, mixed, numGames)
    numPos = findBestCandidate(op_stop, numGames, startingBalance, mixed)
    print("Optimal Stop of", op_stop * 100, "% had an accuracy of", numPos, "%")


def optimal_stopping(startingBalance, mixed, numGames, amountPaid=0):
    solution_found_count = {}
    optimal_solution_found_count = {}
    for i in range(1, numGames):
        solution_found_count[str(i)] = 0
        optimal_solution_found_count[str(i)] = 0
    for experiment in range(1000):
        print(experiment)
        list1 = [np.random.uniform(0, 100) for i in range(numGames)]
        list2 = list1.copy()
        if mixed == 0:
            list2 = create_list(list2, startingBalance, amountPaid)
        else:
            list2 = create_list_mixed(list2, startingBalance)
        optimal_value = max(list2)
        for i in range(1, numGames):
            for item in list2[i:-1]:
                x = max(list2[0:i])
                if item > x:
                    solution_found_count[str(i)] += 1
                    if item > startingBalance and item == optimal_value:
                        optimal_solution_found_count[str(i)] += 1
                    break

    x, y = zip(*optimal_solution_found_count.items())
    maxNum = max(optimal_solution_found_count.values())
    itemList = [int(i) for i, j in optimal_solution_found_count.items() if j == maxNum]
    optimal_stop = round(((sum(itemList) / len(itemList)) / numGames), 3)
    print(optimal_solution_found_count)
    print(optimal_stop * 100, "%")
    plt.plot(x, y)
    plt.show()
    return optimal_stop


def findBestCandidate(opPercentage, length, startingBalance, mixed, amountPaid=0):
    numPos = 0
    for i in range(100):
        resListOriginal = [np.random.uniform(0, 100) for i in range(length)]
        if mixed == 0:
            resList = create_list(resListOriginal, startingBalance, amountPaid)
        else:
            resList = create_list_mixed(resListOriginal, startingBalance)

        lengthOpStop = round(length * opPercentage)
        fileInOpStop = resList[0:lengthOpStop]

        maxItemInOp = max(fileInOpStop)
        secList = resList[lengthOpStop - 1:-1]

        itemChosen = 0
        foundNewBest = False
        for item in secList:
            if item > maxItemInOp:
                itemChosen = item
                foundNewBest = True
                break
        if foundNewBest:
            numPos += 1
    return numPos


def create_list(list2, startingBalance, amountPaid):
    currBalance = startingBalance
    for i in range(len(list2)):
        if currBalance <= 0:
            list2[i] = 0
            currBalance = 0
            continue

        if list2[i] < 60:
            list2[i] = currBalance - amountPaid
            currBalance -= amountPaid

        elif list2[i] >= 60 and list2[i] < 80:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 2)
            currBalance -= amountPaid
            currBalance += amountPaid * 2

        elif list2[i] >= 80 and list2[i] < 90:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 3)
            currBalance -= amountPaid
            currBalance += amountPaid * 3

        elif list2[i] >= 90 and list2[i] < 98:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 5)
            currBalance -= amountPaid
            currBalance += amountPaid * 5

        elif list2[i] >= 98 and list2[i] < 99:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 30)
            currBalance -= amountPaid
            currBalance += amountPaid * 30

        elif list2[i] >= 99 and list2[i] < 99.3:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 80)
            currBalance -= amountPaid
            currBalance += amountPaid * 80

        elif list2[i] >= 99.3 and list2[i] < 99.5:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 120)
            currBalance -= amountPaid
            currBalance += amountPaid * 120

        elif list2[i] >= 99.5 and list2[i] < 99.75:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 200)
            currBalance -= amountPaid
            currBalance += amountPaid * 200

        elif list2[i] >= 99.75 and list2[i] < 99.84:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 500)
            currBalance -= amountPaid
            currBalance += amountPaid * 500

        elif list2[i] >= 99.84 and list2[i] < 99.9:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 1000)
            currBalance -= amountPaid
            currBalance += amountPaid * 1000

        elif list2[i] >= 99.9 and list2[i] < 100:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 2500)
            currBalance -= amountPaid
            currBalance += amountPaid * 2500

    return list2


def create_list_mixed(list2, startingBalance):
    currBalance = startingBalance
    for i in range(len(list2)):
        value = random.randint(0, 1)
        if value == 0:
            amountPaid = 10
        else:
            amountPaid = 100

        if currBalance <= 0:
            list2[i] = 0
            currBalance = 0
            continue

        if list2[i] < 60:
            list2[i] = currBalance - amountPaid
            currBalance -= amountPaid

        elif list2[i] >= 60 and list2[i] < 80:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 2)
            currBalance -= amountPaid
            currBalance += amountPaid * 2

        elif list2[i] >= 80 and list2[i] < 90:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 3)
            currBalance -= amountPaid
            currBalance += amountPaid * 3

        elif list2[i] >= 90 and list2[i] < 98:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 5)
            currBalance -= amountPaid
            currBalance += amountPaid * 5

        elif list2[i] >= 98 and list2[i] < 99:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 30)
            currBalance -= amountPaid
            currBalance += amountPaid * 30

        elif list2[i] >= 99 and list2[i] < 99.3:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 80)
            currBalance -= amountPaid
            currBalance += amountPaid * 80

        elif list2[i] >= 99.3 and list2[i] < 99.5:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 120)
            currBalance -= amountPaid
            currBalance += amountPaid * 120

        elif list2[i] >= 99.5 and list2[i] < 99.75:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 200)
            currBalance -= amountPaid
            currBalance += amountPaid * 200

        elif list2[i] >= 99.75 and list2[i] < 99.84:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 500)
            currBalance -= amountPaid
            currBalance += amountPaid * 500

        elif list2[i] >= 99.84 and list2[i] < 99.9:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 1000)
            currBalance -= amountPaid
            currBalance += amountPaid * 1000

        elif list2[i] >= 99.9 and list2[i] < 100:
            list2[i] = (currBalance - amountPaid) + (amountPaid * 2500)
            currBalance -= amountPaid
            currBalance += amountPaid * 2500

    return list2


if __name__ == '__main__':
    main()
