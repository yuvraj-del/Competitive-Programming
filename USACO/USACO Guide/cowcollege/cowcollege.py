"""
Problem: USACO 2022 December Contest, Bronze Problem 1. Cow College
Date Completed: 6/19/24
"""

n = int(input())
money = [int(i) for i in input().split()]
money.sort()

total = 0
amount = 0
for i in range(n):
    temp = total
    total = max(money[i]*(n-i), total)
    if total > temp:
        amount = max(amount, money[i])

print(total, amount)
