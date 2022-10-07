import re

# N = 5
# input_values = [
#     "....#....",  # i=1
#     "...##X...",  # i=2
#     "..#####..",  # i=3
#     ".#X#####.",  # i=4
#     "#########",  # i=5
# ]

N = 6
input_values = [
    ".....#.....",  # i=1
    "....###....",  # i=2
    "...#####...",  # i=3
    "..#X#####..",  # i=4
    ".#########.",  # i=5
    "#X########X",  # i=6
]


class Updater:
    def __init__(self, lines):
        self.lines = lines
        self.n = len(lines)
        self.w = self.n * 2 - 1

    def update(self, i, j):
        my = self.lines[i][j]
        if my == ".":
            return
        r = j + 1
        l = j - 1
        if (l >= 0 and self.lines[i + 1][l] == "X") or (self.lines[i + 1][j] == "X") or (r < self.w and self.lines[i + 1][r] == "X"):
            self.lines[i] = self.lines[i][:j] + "X" + self.lines[i][j+1:]

    def run(self):
        for i in range(self.n-2, -1, -1):
            for j in range(self.w):
                self.update(i, j)
        return self.lines


res = Updater(input_values).run()

for v in res:
    print(v)
