import numpy as np
import time

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

start_time = time.time()
a = np.column_stack([np.array(list(x), dtype=int) for x in lines])
gamma = ''.join([str(np.argmax(np.bincount(x))) for x in a])
epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
print(int(gamma, 2) * int(epsilon, 2))
print(f"{((time.time() - start_time) * 1000)}ms")

def getRating(selectIfEqual):
    O = lines.copy()
    Oa = np.column_stack([np.array(list(x), dtype=int) for x in O])
    for i in range(0, len(O[0])):
        counts = np.bincount(Oa[i])
        max = np.argmax(counts)
        min = np.argmin(counts)
        if selectIfEqual == 1:
            keep = max
        else:
            keep = min
        if counts[0] == counts[1]:
            keep = selectIfEqual
        Oc = []
        for x in O:
            if x[i] == str(keep):
                Oc.append(x) 
        if len(Oc) == 1:
            return(Oc)
        Oa = np.column_stack([np.array(list(x), dtype=int) for x in Oc])
        O = Oc.copy()

start_time = time.time()
print(int(''.join(getRating(1)), 2) * int(''.join(getRating(0)), 2))
print(f"{((time.time() - start_time) * 1000)}ms")