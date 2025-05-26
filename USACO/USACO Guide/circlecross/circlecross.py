"""
Problem: USACO 2017 February Contest, Bronze Problem 2. Why Did the Cow Cross the Road II
Date Completed: 11/25/2024
"""

import string

with open("circlecross.in") as read:
    arr = list(read.readline())
    upper = list(string.ascii_uppercase)

ans = 0
for i in range(len(upper)):
    first = [a for a, x in enumerate(arr) if x == upper[i]]
    for j in range(len(upper)):
        if i != j:
            second = [b for b, y in enumerate(arr) if y == upper[j]]
            if first[0] < second[0] < first[1] < second[1]:
                ans += 1


with open("circlecross.out", "w") as write:
    print(ans, file=write)
