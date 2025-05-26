"""
Problem: USACO 2017 January Contest, Bronze Problem 3. Cow Tipping
Date Completed: 1/21/2025
"""

with open("cowtip.in") as read:
    n = int(read.readline())
    cows = [[int(i) for i in read.readline() if i != "\n"] for _ in range(n)]

ans = 0

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if cows[i][j] == 1:
            for k in range(i, -1, -1):
                for l in range(j, -1, -1):
                    if cows[k][l] == 0:
                        cows[k][l] = 1
                    else:
                        cows[k][l] = 0
            ans += 1

print(ans, file=open("cowtip.out", "w"))
