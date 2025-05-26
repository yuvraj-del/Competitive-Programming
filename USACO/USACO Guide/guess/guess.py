"""
Problem: USACO 2019 January Contest, Bronze Problem 3. Guess the Animal
Date Completed: 7/4/2024
"""

with open("guess.in") as read:
    n = int(read.readline())
    animals = [[i for i in read.readline().split()[2:]] for _ in range(n)]
    ans = 0

for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, len(set(animals[i]) & set(animals[j])))

print(ans + 1, file=open("guess.out", "w"))
