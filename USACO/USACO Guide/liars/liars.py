"""
Problem: USACO 2016 December Contest, Bronze Problem 3. The Cow-Signal
Date Completed: 11/25/2024
"""

n = int(input())
arr = [[int(i) if i.isnumeric() else i for i in input().split()] for _ in range(n)]

ans = n
temp = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if arr[j][0] == "G":
                if arr[i][1] < arr[j][1]:
                    temp += 1
            if arr[j][0] == "L":
                if arr[i][1] > arr[j][1]:
                    temp += 1
    ans = min(ans, temp)
    temp = 0
print(ans)
