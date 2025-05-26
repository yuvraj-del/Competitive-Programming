"""
Problem: USACO 2024 January Contest, Bronze Problem 1. Majority Opinion
Date Completed: 12/7/2024
"""

t = int(input())
for _ in range(t):
    n = int(input())
    cow = [int(i) for i in input().split()]
    ans = set()
    for i in range(len(cow)):
        if cow[i] == cow[i - 1] and i > 0 or cow[i] == cow[i - 2] and i > 1:
            ans.add(cow[i])
    if ans == set():
        print("-1")
    else:
        print(*sorted(list(ans)))
    ans = set()
