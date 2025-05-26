"""
Problem: USACO 2016 December Contest, Bronze Problem 3. The Cow-Signal
Date Completed: 6/13/2024
"""

with open("gymnastics.in") as read:
    ats, n = map(int, read.readline().split())
    rank = [[int(i) for i in read.readline().split()] for _ in range(ats)]
    table = [[0 for _ in range(n)] for _ in range(n)]

for i in range(ats):
    for j in range(n):
        row = rank[i][j]-1
        for k in range(n-1-j):
            table[row][rank[i][j+1+k]-1] += 1

pairs = 0
for i in range(n):
    for j in range(n):
        if table[i][j] == ats:
            pairs += 1

with open("gymnastics.out", "w") as write:
    print(pairs, file=write)

