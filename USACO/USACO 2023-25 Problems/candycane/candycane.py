"""
Problem: USACO 2023 December Contest, Bronze Problem 1. Candy Cane Feast
Date Completed: 12/4/2024
"""

n, m = map(int, input().split())
cows = [int(i) for i in input().split()]
candy = [int(i) for i in input().split()]

for i in range(m):
    eaten = 0
    for j in range(n):
        eat = min(cows[j], candy[i]) - eaten
        if eat <= 0:
            continue
        cows[j] += eat
        eaten += eat
        if eaten == candy[i]:
            break

print(*cows, sep="\n")