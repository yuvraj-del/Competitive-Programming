"""
Problem: USACO 2015 February Contest, Bronze Problem 1. Censoring (Bronze)
Date Completed: 11/30/2024
"""

import sys
sys.stdin = open("censor.in")
sys.stdout = open("censor.out", "w")

s = input().strip()
t = input().strip()

ans = ""
for i in s:
    ans += i
    if ans[-len(t):] == t:
        ans = ans[: -len(t)]

print(ans)
