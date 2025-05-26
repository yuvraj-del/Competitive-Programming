"""
Problem: USACO 2016 January Contest, Bronze Problem 3. Mowing the Field
Date Completed: 11/21/2024
"""

with open("mowing.in") as read:
    n = int(read.readline())
    data = [[int(i) if i.isnumeric() else i for i in read.readline().split()] for _ in range(n)]

coords = {(0, 0)}
places = [[0, 0]]
pos = (0, 0)
x = None
size = 1
time = 0
ans = 100000
for i in range(n):
    for j in range(data[i][1]):
        time += 1
        size += 1
        if data[i][0] == "N":
            x = list(pos)
            x = [x[0], x[1] + 1]
            places.append(x)
            pos = tuple(x)
            coords.add(pos)
        if data[i][0] == "E":
            x = list(pos)
            x = [x[0] + 1, x[1]]
            places.append(x)
            pos = tuple(x)
            coords.add(pos)
        if data[i][0] == "S":
            x = list(pos)
            x = [x[0], x[1] - 1]
            places.append(x)
            pos = tuple(x)
            coords.add(pos)
        if data[i][0] == "W":
            x = list(pos)
            x = [x[0] - 1, x[1]]
            places.append(x)
            pos = tuple(x)
            coords.add(pos)
        if len(coords) != size:
            new = [*(idx for idx, char in enumerate(places) if char == x)]
            ans = min(ans, time - new[-2])
            size -= 1
if ans == 100000:
    ans = -1
print(ans, file=open("mowing.out", "w"))
