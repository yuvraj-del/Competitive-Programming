"""
Problem: USACO 2018 December Contest, Bronze Problem 1. Mixing Milk
Date Completed: 7/29/2024
"""

with open("mixmilk.in") as read:
    amount = [[int(i) for i in read.readline().split()] for _ in range(3)]
    bucket = [amount[0][1], amount[1][1], amount[2][1]]


def swap(x, y):
    if bucket[y] + bucket[x] > amount[y][0]:
        bucket[x] = bucket[x] - (amount[y][0] - bucket[y])
        bucket[y] = amount[y][0]
    else:
        bucket[y] = bucket[y] + bucket[x]
        bucket[x] = 0


for i in range(100):
    if i % 3 == 0:
        swap(0, 1)
    if i % 3 == 1:
        swap(1, 2)
    if i % 3 == 2:
        swap(2, 0)

with open("mixmilk.out", "w") as write:
    for i in bucket:
        print(i, file=write)
