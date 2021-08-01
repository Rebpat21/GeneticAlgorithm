from parent import parent
from crossover import crossover
from mutation import mutation
from random import *
import datetime
import os
import copy


# def doesneedEdges(tracker):
#     if 0 in tracker:
#         return True
#     else:
#         return False


def genetic():
    chroms = []
    # faces = input("Enter number of sides (Above 3):")
    population = randint(100, 500)
    # population = 50 # For presentation demo
    number = randint(4, 120)
    # number = 20

    # population = 3
    p = 0
    while p < population:
        print("Compiling Chromosome "+str(p+1)+"/"+str(population))
        # number = randint(4, 12)
        # print(number)
        # print()

        # if int(faces) <= 3:
        #     print("Error, Size needs to be above 3.")
        #     exit()
        
        # i = 0
        # while i < (int(size)/6):
        #     cubes.append(cube_verticies_vector3)
        #     i += 1
        # print(cubes)

        print()
        # print("Compiling Verticies...")
        verts = []
        # print("YES YES YES")

        i = 0
        # bar = Bar('Compiling Verticies', max=(int(number)*2))
        while i < (int(number)*2):
            x = round(uniform(-5, 5), 3)
            y = round(uniform(-5, 5), 3)
            z = round(uniform(-5, 5), 3)

            verts.append((x, y, z))

            i += 1
        #     bar.next()
        # bar.finish()

        edges = []
        # tracker = []

        # i = 0
        # while i < len(verts):
        #     tracker.append(0)
        #     i += 1

        # needsEdges = True

        # while needsEdges:

        #     point1 = randint(0, len(verts)-1)
        #     point2 = randint(0, len(verts)-1)
        #     j = 0
        #     while((point1, point2) in edges):
        #         point1 = randint(0, len(verts)-1)
        #         point2 = randint(0, len(verts)-1)
        #         j+=1

        #         if tracker[point1] == 5 or tracker[point2] == 5:
        #             continue
        #         if j == 50:
        #             print(tracker)

        #     tracker.insert(point1, tracker[point1]+1)

        #     edges.append((point1, point2))

        #     needsEdges = doesneedEdges(tracker)

        # print()
        # print("Compiling Edges...")

        i = 0
        total = 0
        # bar = Bar('Compiling Edges', max=len(verts))
        for vert in verts:
            connections = randint(2, 4)
            # print(i)

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
        #     bar.next()
        # bar.finish()


        # print()
        # print("Compiling Faces...")

        i=0
        faces = []
        # bar = Bar('Compiling Faces', max=len(verts))
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

            # print("List for "+str(i)+": "+str(temp))
            i += 1
        #     bar.next()
        # bar.finish()

        chroms.append((verts, edges, faces))
        p += 1
        os.system('cls')

    # print()
    # print(verts)
    # print()
    # print(edges)
    # print(len(edges))
    # print()
    # print(faces)


    # iterations = 5000
    iterations = 100
    # iterations = 2
    # h < iterations
    print("Please wait, this takes a very, very, very, very, very long time.")
    a = datetime.datetime.now().replace(microsecond=0)
    choices = [(1,1), (1, 2), (2, 1), (2, 2)]
    for c in choices:
        choice1, choice2 = c
        h, q = 0, 0
        # print("Run")
        chromsClone = copy.deepcopy(chroms)
        breaks = False
        
        while h < iterations:
            # print("Iteration: "+str(h+1))

            i = 0
            # i < population
            while i < population:
                # print("Iteration: "+str(h+1))
                # print("Performing on Population["+str(i+1)+"]")
                # print(chroms[i])
                # verts, edges, faces = chroms[i]
                # print(verts)
                # print(len(chroms))
                # print("Starting iteration "+str(i+1))
                parents, bestValue, eliteClone = parent(chromsClone, choice1)
                if bestValue <= 1:
                    print("Completion trigger activated.")
                    print("CONGRADULATIONS!")
                    print("Fitness: "+str(bestValue)+". Iteration: "+str(h+1))
                    breaks = True
                    break
                # print(elite)
                # print(chromE)
                # print(len(parents))
                # print(chroms[0])
                # print(parents[0])
                # print()

                children = crossover(parents, choice2)
                # print()
                # print(children[0])

                # print(children)
                # print(len(children))
                chromsClone = mutation(children)
                # print(len(chroms))
                # print(chroms[0])
                chromsClone[0] = copy.deepcopy(eliteClone)
                # chroms[i] = (verts, edges, faces)

                # os.system('cls')
                i += 1
            
                # i+=1
            if (h % 1 == 0 or h == iterations-1):
                print("Fitness: "+str(bestValue)+". Iteration: "+str(h+1))
                b = datetime.datetime.now().replace(microsecond=0)
                # print("Time between outputs: "+str(b-a))
                a = datetime.datetime.now().replace(microsecond=0)
            
            if breaks == True:
                break

            h+=1

        f = open("Results.txt", "a")
        if choice1 == 1:
            str1 = "Using pick 10 Tournament selection"
        else:
            str1 = "Using pick N Tournament selection"

        if choice2 == 1:
            str2 = "using Single point crossover"
        else:
            str2 = "using Double point crossover"

        f.write(str1+" and "+str2+". The best final fitness value was: "+str(bestValue)+" after "+str(iterations+1)+" iterations. Population:"+str(population)+" Chrom:"+str(number)+"\n")
        # f.write("\n")
        f.close()

    # print(verts)

    # print(verts)



