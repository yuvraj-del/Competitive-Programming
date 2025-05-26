"""
Problem: USACO 2015 December Contest, Bronze Problem 2. Speeding Ticket
Date Completed: 6/2/2024
"""

with open("speeding.in") as read:
    n, m = [int(i) for i in read.readline().split()]
    road = [[int(i) for i in read.readline().split()] for _ in range(n)]
    cow = [[int(i) for i in read.readline().split()] for _ in range(m)]

limit = []
for i in road:
    for _ in range(i[0]):
        limit.append(i[1])

bessie = []
for i in cow:
    for _ in range(i[0]):
        bessie.append(i[1])

max_speed = 0
for i in range(100):
    max_speed = max(max_speed, bessie[i] - limit[i])

print(max_speed, file=open("speeding.out", "w"))
