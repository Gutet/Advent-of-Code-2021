from numpy import loadtxt
import time

lines = loadtxt("input.txt", dtype=int)

start_time = time.time()
prev = float("inf")
numInc = 0
for l in lines:
    numInc = numInc + 1 if l > prev else numInc
    prev = l
print(numInc)
print(f"{((time.time() - start_time) * 1000)}ms")

start_time = time.time()
prev = float("inf")
numInc = 0
for i in range(len(lines) - 3 + 1):
    total = sum(lines[i: i + 3])
    numInc = numInc + 1 if total > prev else numInc
    prev = total
print(numInc)
print(f"{((time.time() - start_time) * 1000)}ms")