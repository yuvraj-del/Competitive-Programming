"""
Problem: USACO 2017 February Contest, Bronze Problem 3. Why Did the Cow Cross the Road III
Date Completed: 6/18/2024
"""

import sys
sys.stdin = open("cowqueue.in")
sys.stdout = open("cowqueue.out", "w")

n = int(input())
cows = [[int(i) for i in input().split()] for _ in range(n)]
cows.sort()

time = 0
for i in cows:
    if time > i[0]:
        time += i[1]
    else:
        time = i[0] + i[1]

print(time)
