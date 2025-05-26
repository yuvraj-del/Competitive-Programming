"""
Problem: USACO 2017 January Contest, Bronze Problem 1. Don't Be Last!
Date Completed: 7/2/2024
"""

with open("notlast.in") as read:
    n = int(read.readline())
    cows = [[i for i in read.readline().split()] for _ in range(n)]
    total = {
        "Bessie": 0,
        "Maggie": 0,
        "Elsie": 0,
        "Henrietta": 0,
        "Gertie": 0,
        "Daisy": 0,
        "Annabelle": 0
    }
    for i in cows:
        total[i[0]] += int(i[1])

last = list(total.values())
last.sort()
small = last[0]
final = []
for i in range(len(last)):
    if last[i] != small:
        final.append(last[i])

with open("notlast.out", "w") as write:
    if len(final) > 1:
        if final[0] == final[1]:
            print("Tie", file=write)
        else:
            print(list(total.keys())[list(total.values()).index(list(final)[0])], file=write)
    elif len(final) == 1:
        print(list(total.keys())[list(total.values()).index(list(final)[0])], file=write)
    else:
        print("Tie", file=write)
