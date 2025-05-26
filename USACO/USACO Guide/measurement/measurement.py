"""
Problem: USACO 2017 December Contest, Bronze Problem 3. Milk Measurement
Date Completed: 7/3/2024
"""

with open("measurement.in") as read:
    n = int(read.readline())
    measure = []
    for _ in range(n):
        inside = []
        for i in read.readline().split():
            try:
                inside.append(int(i))
            except ValueError:
                inside.append(i)
        measure.append(inside)
    measure.sort()
    total = {
        "Bessie": 7,
        "Elsie": 7,
        "Mildred": 7
    }
    wall = []
    ans = 0


def highest():
    now = list(total.values())
    now.sort()
    pictures = []
    for name in total:
        if total[name] == now[-1]:
            pictures.append(name)
    return pictures


for i in range(n):
    total[measure[i][1]] += measure[i][2]
    if wall != highest():
        ans += 1
    wall = highest()
    

print(ans, file=open("measurement.out", "w"))
