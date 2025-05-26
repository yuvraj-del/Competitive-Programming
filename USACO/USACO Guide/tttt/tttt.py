"""
Problem: USACO 2018 US Open Contest, Bronze Problem 1. Team Tic Tac Toe
Date Completed: 6/21/2024
"""

with open(file="tttt.in") as read:
    row1 = [i for i in read.readline() if i != "\n"]
    row2 = [i for i in read.readline() if i != "\n"]
    row3 = [i for i in read.readline() if i != "\n"]
    column1 = [row1[0], row2[0], row3[0]]
    column2 = [row1[1], row2[1], row3[1]]
    column3 = [row1[2], row2[2], row3[2]]
    dig1 = [row1[0], row2[1], row3[2]]
    dig2 = [row1[2], row2[1], row3[0]]
    game = [row1, row2, row3, column1, column2, column3, dig1, dig2]


def one_letter():
    counter = set()
    counter1 = set()
    finder = set()
    temp = ""
    for i in game:
        finder.clear()
        for j in range(3):
            finder.add(i[j])
        if len(finder) == 1:
            counter.update(finder)
        elif len(finder) == 2:
            temp = temp + "".join(finder)
            counter1.add(temp)
        temp = ""
        print(counter1)
        print(i)
    return len(counter), len(counter1)


total1, total2 = one_letter()

with open("tttt.out", "w") as write:
    print(total1, file=write)
    print(total2, file=write)
