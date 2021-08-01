from random import *
from fitness import fitness
from progress.bar import Bar


def tournament(chroms, fitnessVals):
    champs, parent = [], []
    fitnessVals, eliteChrom, elitePick, bestValue = fitness(chroms)
    # print(fitnessVals)
    # parent.append(eliteChrom)
    # champs.append(elitePick)
    # print()
    # print("Tournament Selection Started.")
    pick = 0
    # bar = Bar('Processing', max=len(faces))
    i = 0
    while i < len(fitnessVals):
        fit, best, champ, j = 0, 0, 0, 0
        fitnesses = 100000000
        tournamentSize = randint(2, len(chroms))
        champs = []

        while j < tournamentSize:
            pick = randint(0, len(fitnessVals)-1)

            fit = fitnessVals[pick]

            # print("fit: "+str(fit))
            # print("fitnesses: "+str(fitnesses))

            if fit < fitnesses:
                fitnesses = fit
                best = chroms[pick]
                # champ = pick

            j += 1

        parent.append(best)
  
        i += 1
    #     bar.next()
    # bar.finish()
    
    # print(parent)
    # print(len(parent))
    # print(len(faces))

    # print("LOP: "+str(len(parent)))

    return parent, bestValue


def tournament10(chroms, fitnessVals):
    champs, parent = [], []
    fitnessVals, eliteChrom, elitePick, bestValue = fitness(chroms)
    # print(fitnessVals)
    # parent.append(eliteChrom)
    # champs.append(elitePick)
    # print()
    # print("Tournament Selection 10 Started.")
    pick = 0
    # bar = Bar('Processing', max=len(faces))
    i = 0
    while i < len(fitnessVals):
        fit, best, champ, j = 0, 0, 0, 0
        fitnesses = 100000000
        tournamentSize = 10
        champs = []

        while j < tournamentSize:
            pick = randint(0, len(fitnessVals)-1)

            fit = fitnessVals[pick]
            # print("fit: "+str(fit))
            # print("fitnesses: "+str(fitnesses))

            if fit < fitnesses:
                fitnesses = fit
                best = chroms[pick]
                # champ = pick

            j += 1

        parent.append(best)

        i += 1
    #     bar.next()
    # bar.finish()

    # print(parent)
    # print(len(parent))
    # print(len(faces))

    # print("LOP: "+str(len(parent)))

    return parent, bestValue

import copy

def parent(chroms, choice):
    # print()
    
    # path = randint(0, 1)

    fitnessVals, eliteChrom, elitePick, bestValue = fitness(chroms)

    if choice == 1:
        parents, bestValue = tournament10(chroms, fitnessVals)
    else:
        parents, bestValue = tournament(chroms, fitnessVals)

    tempChrom = copy.deepcopy(eliteChrom)

    # parents = tournament(chroms)

    return parents, bestValue, tempChrom
