from random import *
import os
import numpy as np
import copy

def mutation(chroms):
    # print()
    # print("Performing Mutation...")
    # print(chroms)
    # bar = Bar('Processing', max=len(children))

    test = (1/len(chroms[0]))
    i = 0
    while i < len(chroms):
        score = uniform(0, (test*2))
        verts, edges, faces = chroms[i]

        # print(verts)
        j = 0
        while j < len(verts):

            if score < test:
                x = round(uniform(-5, 5), 3)
                y = round(uniform(-5, 5), 3)
                z = round(uniform(-5, 5), 3)

                verts[j] = (x, y, z)

            j += 1
        i += 1

    return chroms


def fitness(chroms):
    total = []
    i, maxNum, minNum = 0, 500000000000, 0
    while i < len(chroms):
        fitnessesesessses = []
        verts, edges, faces = chroms[i]
        j = 0
        while j < len(faces):
            face = faces[j]

            x, y, z = face

            x1, y1, notused = verts[x]
            x2, y2, notused = verts[y]
            x3, y3, notused = verts[z]

            delta = round(abs(.5*((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3))), 3)
            fitnessesesessses.append(delta)

            j += 1
        maxNum = np.argmax(fitnessesesessses)
        minNum = np.argmin(fitnessesesessses)

        total.append(round(fitnessesesessses[maxNum] - fitnessesesessses[minNum], 3))
        i += 1
    return total


def NGA():
    chroms = []
    population = randint(100, 500)
    population = 50
    number = randint(4, 120)
    number = 20
    p = 0
    while p < population:
        print("Compiling Chromosome "+str(p+1)+"/"+str(population))
        print()
        verts = []

        i = 0
        while i < (int(number)*2):
            x = round(uniform(-5, 5), 3)
            y = round(uniform(-5, 5), 3)
            z = round(uniform(-5, 5), 3)

            verts.append((x, y, z))

            i += 1

        edges = []

        i = 0
        total = 0
        for vert in verts:
            connections = randint(2, 4)

            j = 0
            while j < connections:
                point2 = randint(0, len(verts)-1)

                q = 0
                while((i, point2) in edges or (point2, i) in edges or (i == point2)):
                    point2 = randint(0, len(verts)-1)
                    q += 1
                    if q == 235:
                        break

                edges.append((i, point2))

                if connections == 2 and j == 1:
                    point1, point2 = edges[total-1]
                    point3, point4 = edges[total]
                    if (((point2, point4) not in edges) and ((point4, point2) not in edges)):
                        edges.append((point2, point4))
                        total += 1

                elif connections == 3 and j == 2:
                    point1, point2 = edges[total-2]
                    point3, point4 = edges[total]
                    if (((point2, point4) not in edges) and ((point4, point2) not in edges)):
                        edges.append((point2, point4))
                        total +=1

                elif connections == 4 and j == 3:
                    point1, point2 = edges[total-3]
                    point3, point4 = edges[total]
                    if (((point2, point4) not in edges) and ((point4, point2) not in edges)):
                        edges.append((point2, point4))
                        total += 1

                j += 1
                total += 1
            i += 1

        i=0
        faces = []
        while i < len(verts):
            temp = []

            for x, y in edges:
                if x == i:
                    temp.append(y)
                elif y == i:
                    temp.append(x)

            for j in temp:
                for x, y in edges:
                    if (x == j and y != j and x != y and y in temp):
                        if (((i, j, y) not in faces) and ((i, y, j) not in faces) and ((j, i, y)not in faces) and ((j, y, i) not in faces) and ((y, i, j) not in faces) and ((y, j, i) not in faces)):
                            faces.append((i, j, y))
                    elif (y == j and x != j and y != x and x in temp):
                        if (((i, j, x) not in faces) and ((i, x, j) not in faces) and ((j, i, x)not in faces) and ((j, x, i) not in faces) and ((x, i, j) not in faces) and ((x, j, i) not in faces)):
                            faces.append((i, j, x))

            i += 1

        chroms.append((verts, edges, faces))
        p += 1
        os.system('cls')

    iterations = 100
    q = 0
    fitnessVals, mutatedChroms, mutatedFitness = [], [], []

    while i < iterations:
        chromsCopy = copy.deepcopy(chroms)
        fitnessVals = fitness(chroms)

        if i%10 == 0:
            print(min(fitnessVals))
        if min(fitnessVals) <= 1:
            print("Ideal Value hit!")
            break
            # print(np.argmin(fitnessVals))
            # f = open("STUFF.txt", "r")
            # f.write()

            # exit()

        mutatedChroms = mutation(chromsCopy)

        mutatedFitness = fitness(mutatedChroms)

        j = 0
        while j < len(fitnessVals):
            if mutatedFitness[j] < fitnessVals[j]:
                chroms[j] = copy.deepcopy(mutatedChroms[j])
            j += 1
        
        i += 1

    f = open("Non-Results.txt", "a")
    f.write(str(min(fitnessVals))+" Size: "+str(number)+"\n")
    f.close()



# NGA()

