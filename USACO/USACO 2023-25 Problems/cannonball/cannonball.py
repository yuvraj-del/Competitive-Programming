"""
Problem: USACO 2024 January Contest, Bronze Problem 2. Cannonball
Date Completed: 12/7/2024
"""

n, s = map(int, input().split())
s -= 1
pad = [[int(i) for i in input().split()] for _ in range(n)]

pow = 1
ans = 0
edge = 0

while 1 <= s + 1 <= n and edge != 2:
    if pad[s][0] == 1 and pad[s][1] <= abs(pow):
        ans += 1
        pad[s][1] = n ** 10
    if pad[s][0] == 0:
        if pad[s][1] == 0:
            edge += 1
        else:
            edge = 0
        if pow < 0:
            pow = abs(pow) + pad[s][1]
        else:
            pow = (pow + pad[s][1]) * -1
    s += pow

print(ans)