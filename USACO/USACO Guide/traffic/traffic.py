"""
Problem: USACO 2019 February Contest, Bronze Problem 3. Measuring Traffic
Date Completed: 11/20/2024
"""

with open("traffic.in") as read:
    n = int(read.readline())
    data = [[int(i) if i.isnumeric() else str(i) for i in read.readline().split()] for _ in range(n)]

first = [0, 1000]

for i in range(n):
    if data[i][0] == "none":
        first[0] = max(first[0], data[i][1])
        first[1] = min(first[1], data[i][2])
    if data[i][0] == "on":
        first[0], first[1] = first[0] + data[i][1], first[1] + data[i][2]
    if data[i][0] == "off":
        first[0], first[1] = first[0] - data[i][2], first[1] - data[i][1]
        first[0] = max(first[0], 0)
ansA = first.copy()

first[0], first[1] = 0, 1000
for i in range(n - 1, -1, -1):
    if data[i][0] == "none":
        first[0] = max(first[0], data[i][1])
        first[1] = min(first[1], data[i][2])
    if data[i][0] == "on":
        first[0], first[1] = first[0] - data[i][2], first[1] - data[i][1]
        first[0] = max(first[0], 0)
    if data[i][0] == "off":
        first[0], first[1] = first[0] + data[i][1], first[1] + data[i][2]

with open("traffic.out", "w") as write:
    ans = str(first[0]) + " " + str(first[1]) + "\n" + str(ansA[0]) + " " + str(ansA[1])
    print(ans, file=write)
