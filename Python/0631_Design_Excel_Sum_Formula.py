# Design an Excel-like table supporting set and sum operations with cell references.

# Author: Kaustav Ghosh

class Excel(object):
    def __init__(self, height, width):
        self.table = [[0] * (ord(width) - ord('A') + 1) for _ in range(height)]
        self.formulas = {}

    def set(self, row, column, val):
        r, c = row - 1, ord(column) - ord('A')
        self.table[r][c] = val
        self.formulas.pop((r, c), None)

    def get(self, row, column):
        r, c = row - 1, ord(column) - ord('A')
        if (r, c) in self.formulas:
            return sum(self.get(rr + 1, chr(ord('A') + cc)) for rr, cc in self.formulas[(r, c)])
        return self.table[r][c]

    def sum(self, row, column, numbers):
        r, c = row - 1, ord(column) - ord('A')
        cells = []
        for ref in numbers:
            if ':' in ref:
                a, b = ref.split(':')
                for rr in range(int(a[1:]) - 1, int(b[1:])):
                    for cc in range(ord(a[0]) - ord('A'), ord(b[0]) - ord('A') + 1):
                        cells.append((rr, cc))
            else:
                cells.append((int(ref[1:]) - 1, ord(ref[0]) - ord('A')))
        self.formulas[(r, c)] = cells
        return self.get(row, column)
