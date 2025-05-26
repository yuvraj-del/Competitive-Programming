"""
Problem: USACO 2025 US Open Contest, Bronze Problem 2. More Cow Photos
Date Completed: 3/23/2025
"""

t = int(input())
for _ in range(t):
    ans = 1
    n = int(input())
    cows = list(map(int, input().split()))
    m = [0] * n
    for i in range(n):
        m[cows[i] - 1] += 1
    tall = max(cows)
    for i in range(1, tall):
        if m[i - 1] >= 2:
            ans += 2
    print(ans)
