"""
Problem: USACO 2019 December Contest, Bronze Problem 2. Where Am I?
Date Completed: 6/20/2024
"""

with open("whereami.in") as read:
    n = int(read.readline())
    color = read.readline()

total = n
for i in range(n):
    finder = set()
    for j in range(n - i + 1):
        finder.add(color[j: j + i])
    if len(finder) == (n - i + 1):
        total = i
        break
    print(finder)

print(total, file=open("whereami.out", "w"))
