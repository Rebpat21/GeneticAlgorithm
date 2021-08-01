from random import *
from progress.bar import Bar


def mutation(chroms):
    # print()
    # print("Performing Mutation...")
    # print(chroms)
    # bar = Bar('Processing', max=len(children))

    test = (1/len(chroms))
    i = 0
    while i < len(chroms[0]):
        # score = uniform(0, (test*2))
        verts, edges, faces = chroms[i]

        # print(verts)
        j = 0
        while j < len(verts):
            score = uniform(0, (test*2))

            if score < test:
                x = round(uniform(-5, 5), 3)
                y = round(uniform(-5, 5), 3)
                z = round(uniform(-5, 5), 3)
            
                verts[j] = (x, y, z)
                # print("hit"+str(j))
            # else:


            j += 1
        i += 1
        # bar.next()

    # bar.finish()

    # print (children)
    return chroms

