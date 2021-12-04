from numpy import loadtxt
import time

lines = loadtxt("input.txt", dtype=str)

start_time = time.time()
x, y = 0, 0
for l in lines:
    if l[0] == 'forward':
        x += int(l[1])
    elif l[0] == 'up':
        y -= int(l[1])
    elif l[0] == 'down':
        y += int(l[1])
print(x * y)
print(f"{((time.time() - start_time) * 1000)}ms")

start_time = time.time()
x, y, a = 0, 0, 0
for l in lines:
    if l[0] == 'forward':
        x += int(l[1])
        y += a * int(l[1])
    elif l[0] == 'up':
        a -= int(l[1])
    elif l[0] == 'down':
        a += int(l[1])
print(x * y)
print(f"{((time.time() - start_time) * 1000)}ms")