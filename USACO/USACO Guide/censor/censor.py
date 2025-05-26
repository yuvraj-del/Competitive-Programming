"""
Problem: USACO 2016 December Contest, Bronze Problem 3. The Cow-Signal
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
