from progress.bar import Bar
import numpy as np


def find_nearest(array, value):     
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def fitness(chroms):
    # print()
    # print("Fitness Function Started.")

    total= []
    # bar = Bar('Processing', max=len(faces))
    i, maxNum, minNum = 0, 0, 0
    while i < len(chroms):
    # for verts, edges, faces in chroms:
        fitnessesesessses = []
        verts, edges, faces = chroms[i]
        # print(verts)
        # print(faces)
        j = 0
        while j < len(faces):
        # verts, edges, faces=chroms[i]
            # vert = verts[j]
            face = faces[j]

            x, y, z = face
            # print(verts[x])
            # print(verts[y])
            # print(verts[z])

            x1, y1, notused = verts[x]
            x2, y2, notused = verts[y]
            x3, y3, notused = verts[z]

            delta = round(abs(.5*((x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y1 - x1*y3))), 3)
            # print(delta)
            fitnessesesessses.append(delta)

            j+=1
        maxNum = np.argmax(fitnessesesessses)
        minNum = np.argmin(fitnessesesessses)

        total.append(round(fitnessesesessses[maxNum] - fitnessesesessses[minNum], 3))
        i+=1
    #     bar.next()
    # bar.finish()
    # print(total)

    elite = np.argmin(total)
    # print(total)
    # print(elite)
    # print(total[elite])
    bestValue = total[elite]

    return total, chroms[elite], elite, bestValue
