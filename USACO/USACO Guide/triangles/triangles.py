"""
Problem: USACO 2020 February Contest, Bronze Problem 1. Triangles
Date Completed: 7/2/2024
"""

with open("triangles.in") as read:
    n = int(read.readline())
    points = [[int(i) for i in read.readline().split()] for _ in range(n)]
    ans = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if points[i][0] == points[j][0] and points[i][1] == points[k][1] and points[i] != points[j] and points[i] != points[k]:
                ans = max(ans, abs((points[j][1] - points[i][1]) * (points[k][0] - points[i][0])))

print(ans, file=open("triangles.out", "w"))
