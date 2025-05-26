"""
Problem: USACO 2016 December Contest, Bronze Problem 3. The Cow-Signal
Date Completed: 5/31/2024
"""

read = open("cowsignal.in")
open("cowsignal.out", "w")
m, n, k = map(int, [i for i in read.readline().split()])

world = [[i for i in read.readline() if i != "\n"] for j in range(m)]

for i in range(m*k):
    for j in range(n*k):
        print(world[int(i/k)][int(j/k)], end="", file=open("cowsignal.out", "a"))
    if i != m*k - 1:
        print("", file=open("cowsignal.out", "a"))
