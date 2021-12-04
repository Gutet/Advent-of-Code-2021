from numpy import loadtxt
import time

lines = loadtxt("test.txt", dtype=int)

start_time = time.time()

print(f"{((time.time() - start_time) * 1000)}ms")

start_time = time.time()

print(f"{((time.time() - start_time) * 1000)}ms")