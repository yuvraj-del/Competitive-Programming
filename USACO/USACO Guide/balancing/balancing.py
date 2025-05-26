"""
Problem: USACO 2016 February Contest, Bronze Problem 3. Load Balancing
Date Completed: 7/7/2024
"""

with open("balancing.in") as read:
    n, b = map(int, read.readline().split())
    coords = [[int(i) for i in read.readline().split()] for _ in range(n)]
    fenceX = set()
    fenceY = set()
    for i in coords:
        fenceX.add(i[0] + 1)
        fenceY.add(i[1] + 1)
    m = n

for i in fenceX:
    for j in fenceY:
        quad1 = 0
        quad2 = 0
        quad3 = 0
        quad4 = 0
        for k in range(n):
            if coords[k][0] > i and coords[k][1] > j:
                quad1 += 1
            if coords[k][0] < i and coords[k][1] > j:
                quad2 += 1
            if coords[k][0] < i and coords[k][1] < j:
                quad3 += 1
            if coords[k][0] > i and coords[k][1] < j:
                quad4 += 1
        m = min(m, max(quad1, quad2, quad3, quad4))

print(m, file=open("balancing.out", "w"))
