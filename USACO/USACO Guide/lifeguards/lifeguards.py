"""
Problem: USACO 2018 January Contest, Bronze Problem 2. Lifeguards
Date Completed: 7/4/2024
"""

with open("lifeguards.in") as read:
    n = int(read.readline())
    shifts = [[int(i) for i in read.readline().split()] for _ in range(n)]
    shifts = sorted(shifts, key=lambda x: x[1], reverse=True)
    time = [[i+1, 0] for i in range(shifts[0][1])]
    for i in range(n):
        for j in time:
            if shifts[i][0] <= j[0] < shifts[i][1]:
                j[1] += 1
    ans = 0
    temp = 0

for i in range(n):
    for j in time:
        if shifts[i][0] <= j[0] < shifts[i][1]:
            j[1] -= 1
    for j in time:
        if j[1] >= 1:
            temp += 1
        ans = max(ans, temp)
    temp = 0
    for j in time:
        if shifts[i][0] <= j[0] < shifts[i][1]:
            j[1] += 1

print(ans, file=open("lifeguards.out", "w"))
