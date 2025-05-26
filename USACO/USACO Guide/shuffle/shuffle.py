"""
Problem: USACO 2017 December Contest, Bronze Problem 2. The Bovine Shuffle
Date Completed: 6/2/2024
"""

read = open("shuffle.in", "r")
write = open("shuffle.out", "a")

n = int(read.readline())
shuffle = [int(i) for i in read.readline().split()]
ids = [i for i in read.readline().split()]

new = [0] * n
for i in range(3):
    for j in range(n):
        new[j] = ids[shuffle[j] - 1]
    ids = new.copy()

for i in new:
    print(i, file=write)
