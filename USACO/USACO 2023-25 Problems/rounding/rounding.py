"""
Problem: USACO 2024 December Contest, Bronze Problem 1. Roundabout Rounding
Date Completed: 12/13/2024
"""

t = int(input())

ans = 0
for i in range(t):
    n = int(input())
    p = len(str(n)) - 1 if n / 10**len(str(n)) == .1 else len(str(n))

    for j in range(1, p + 1):
        if j >= 2:
            ans += int("5" * (j-1))
    if n < int("4" * (p-1) + "5"):
        ans -= int("4" + "9" * (p-1)) - int("4" * (p-1) + "5") + 1
    elif int("4" * (p - 1) + "5") <= n < int("4" + "9" * (p - 1)):
        ans -= int("4" + "9" * (p - 1)) - n
    print(ans)
    ans = 0
