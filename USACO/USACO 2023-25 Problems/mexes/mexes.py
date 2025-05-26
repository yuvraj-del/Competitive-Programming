"""
Problem: USACO 2025 February Contest, Bronze Problem 2. Making Mexes
Date Completed: 2/22/2025
"""

n = int(input())
nums = [int(i) for i in input().split()]

counts = [0] * (n + 1)
for i in nums:
    counts[i] += 1

need = [0] * (n + 1)
counter = 0
for i in range(n + 1):
    if counts[i] == 0:
        counter += 1
    need[i] = counter
need.append(0)

for i in range(n + 1):
    print(max(counts[i], need[i - 1]))
