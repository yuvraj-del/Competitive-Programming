"""
Problem: USACO 2016 December Contest, Silver Problem 2. Cities and States
Date Completed: 11/29/2024
"""

import sys
from collections import defaultdict

sys.stdin = open("citystate.in")
sys.stdout = open("citystate.out", "w")

n = int(input())
arr = [[i[:2] for i in input().split()] for _ in range(n)]

seen = defaultdict(int)
ans = 0

for x, y in arr:
    if x != y:
        ans += seen[y + x]
    seen[x + y] += 1

print(ans)
