"""
Problem: USACO 2024 January Contest, Bronze Problem 3. Balancing Bacteria
Date Completed: 12/8/2024
"""

n = int(input())
arr = [int(i) for i in input().split()]

change = 0
up = 0
down = 0

for i in range(n):
    arr[i] += change
    if arr[i] < 0:
        up -= arr[i]
    else:
        down += arr[i]
    change = change + up - down - arr[i]

print(up + down)