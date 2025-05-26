"""
Problem: USACO 2017 US Open Contest, Bronze Problem 1. The Lost Cow
Date Completed: 6/2/2024
"""

read = open("lostcow.in")
x, y = map(int, read.readline().split())

if y > x:
    p = 0
    while (2 ** p) + x < y:
        p += 2
else:
    p = 1
    while x - (2 ** p) > y:
        p += 2

total_distance = 0
if p == 0:
    print(1)
else:
    total_distance = 1
    for i in range(1, p):
        total_distance += (2 ** i) + (2 ** (i - 1))
    total_distance += (2 ** (p - 1)) + abs(x - y)

print(total_distance, file=open("lostcow.out", "w"))
