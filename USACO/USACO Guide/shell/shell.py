"""
Problem: USACO 2019 January Contest, Bronze Problem 1. Shell Game
Date Completed: 7/28/2024
"""

with open("shell.in") as read:
    n = int(read.readline())
    shells = [[int(i) for i in read.readline().split()] for _ in range(n)]
    org = [1, 2, 3]
    ans = []
    mode = 0


def swapper(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


for i in range(n):
    swapper(org, shells[i][0]-1, shells[i][1]-1)
    ans.append(org[shells[i][2]-1])

with open("shell.out", "w") as write:
    mode = max(set(ans), key=ans.count)
    print(ans.count(mode), file=write)
