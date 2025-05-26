"""
Problem: USACO 2016 December Contest, Bronze Problem 2. Block Game
Date Completed: 11/28/2024
"""

import string

with open("blocks.in") as read:
    n = int(read.readline())
    arr = [[i for i in read.readline().split()] for _ in range(n)]
    letters = []
    for i in range(len(string.ascii_lowercase)):
        letters.append([list(string.ascii_lowercase)[i], 0])


for i in range(n):
    a = arr[i][0]
    b = arr[i][1]
    for j in range(len(string.ascii_lowercase)):
        temp1 = len([i for i, x in enumerate(a) if x == list(string.ascii_lowercase)[j]])
        temp2 = len([i for i, x in enumerate(b) if x == list(string.ascii_lowercase)[j]])
        letters[j][1] += max(temp1, temp2)

with open("blocks.out", "w"):
    pass
with open("blocks.out", "a") as write:
    for i, x in letters:
        print(x, file=write)
