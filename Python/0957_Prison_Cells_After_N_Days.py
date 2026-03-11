# There are 8 prison cells. Each day, a cell becomes occupied if both neighbors
# were same state; otherwise empty. Return state after N days.

# Author: Kaustav Ghosh

class Solution(object):
    def prisonAfterNDays(self, cells, n):
        seen = {}
        day = 0
        while day < n:
            key = tuple(cells)
            if key in seen:
                cycle = day - seen[key]
                n = (n - day) % cycle
                day = 0
                seen = {}
            seen[key] = day
            cells = [0] + [1 if cells[i-1] == cells[i+1] else 0 for i in range(1, 7)] + [0]
            day += 1
        return cells
