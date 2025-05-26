"""
Problem: USACO 2016 February Contest, Bronze Problem 1. Milk Pails
Date Completed: 6/8/2024
"""

import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

x, y, m = map(int, input().split())


mm = 0
for i in range(m + 1):
    if x * i > m:
        break
    for j in range(m + 1):
        total = x*i + y*j
        if total > m:
            break
        mm = max(mm, total)

print(mm)
