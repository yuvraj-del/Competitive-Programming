"""
Problem: USACO 2016 February Contest, Bronze Problem 2. Circular Barn
Date Completed: 6/25/2024
"""

with open("cbarn.in") as read:
    n = int(read.readline())
    ri = [int(read.readline()) for _ in range(n)]
    total = sum(ri)
    test = []
    hold = total
    ans = total * n

for i in range(n):

    for j in range(i, n + i):
        hold = hold - ri[j % n]
        test.append(hold)

    ans = min(ans, sum(test))
    hold = total
    test.clear()

with open("cbarn.out", "w") as write:
    print(ans, file=write)
