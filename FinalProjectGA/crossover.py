from random import *
from progress.bar import Bar


def singlePoint(chroms):
    # print()
    # print("Performing Single-point Crossover...")
    # print(len(chroms))
    point = randint(0, len(chroms)-1)
    # print(point)
    # bar = Bar('Processing', max=len(parent)-point)

    i = point
    # print(parent)
    # i < len(chroms)
    while i < len(chroms):
        verts, edges, faces = chroms[i]
        # print(i)
        # print(chroms[i])
        # print(faces)
        # print(chroms[i])
        # print(verts[i])
        # print(i)
        o7 = 0
        while o7 < len(faces):
            # print(faces)
            face = faces[o7]
            try:
                face2 = faces[o7+1]
            except:
                break
            v1, v2, v3 = face
            v4, v5, v6 = face2
            
            choice = randint(1, 3)

            if choice == 1:
                a, b, c = verts[v1]
                d, e, f = verts[v4]
                verts[v1] = (d, e, f)
                verts[v4] = (a, b, c)

            elif choice == 2:
                g, h, z = verts[v3]
                j, k, l = verts[v6]
                verts[v3] = (j, k, l)
                verts[v6] = (g, h, z)

            elif choice == 3:
                m, n, o = verts[v2]
                p, q, r = verts[v5]
                verts[v2] = (p, q, r)
                verts[v5] = (m, n, o)

            else:
                print("Error, nothing appended.")

        # print(chroms[i])
        # print(chroms[i+1])
            o7 += 1
        # print(verts)
        # print()
        # print(i)
        # print(chroms[i])
        i += 2
    #     bar.next()
    # bar.finish()

    return chroms


def twoPoint(chroms):
    # print()
    # print("Performing Two-point Crossover...")
    startPoint = randint(1, len(chroms)-1)
    endPoint = randint(startPoint, len(chroms)-1)
    # bar = Bar('Processing', max=(endPoint-startPoint))

    i = startPoint
    # print(parent)
    while i < endPoint:
        verts, edges, faces = chroms[i]
        # print(faces)
        # print(chroms[i])
        # print(verts[i])
        # print(i)
        o7 = 0
        while o7 < len(faces):
            # print(faces)
            face = faces[o7]
            try:
                face2 = faces[o7+1]
            except:
                break
            v1, v2, v3 = face
            v4, v5, v6 = face2

            choice = randint(1, 3)

            if choice == 1:
                a, b, c = verts[v1]
                d, e, f = verts[v4]
                verts[v1] = (d, e, f)
                verts[v4] = (a, b, c)

            elif choice == 2:
                g, h, z = verts[v3]
                j, k, l = verts[v6]
                verts[v3] = (j, k, l)
                verts[v6] = (g, h, z)

            elif choice == 3:
                m, n, o = verts[v2]
                p, q, r = verts[v5]
                verts[v2] = (p, q, r)
                verts[v5] = (m, n, o)

            else:
                print("Error, nothing appended.")

        # print(chroms[i])
        # print(chroms[i+1])
            o7 += 1

        i += 2
    #     bar.next()
    # bar.finish()

    return chroms


def crossover(chroms, choice):
    # path = randint(0, 1)

    # print(chroms)

    if choice == 1:
        children = singlePoint(chroms)
    else:
        children = twoPoint(chroms)

    # children = singlePoint(chroms)

    # print(parent)
    # print(children)
    
    return children

