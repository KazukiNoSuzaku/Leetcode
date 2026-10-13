# Author: Kaustav Ghosh
# Problem: Strange Printer II
# Approach: Each colour is laid down once as a solid rectangle, which must be at least the bounding box of where that colour still shows, so any foreign colour sitting inside that bounding box had to be printed later to cover the overspill. That gives a precedence edge from the enclosing colour to every colour appearing inside its box, and a legal printing order is exactly a topological order of those edges, so the grid is printable precisely when the precedence graph has no cycle. I settle that with Kahn's algorithm rather than by searching print orders.

from collections import deque


class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(targetGrid), len(targetGrid[0])
        boxes = {}
        for r in range(rows):
            for c in range(cols):
                colour = targetGrid[r][c]
                if colour in boxes:
                    box = boxes[colour]
                    if r < box[0]:
                        box[0] = r
                    if r > box[1]:
                        box[1] = r
                    if c < box[2]:
                        box[2] = c
                    if c > box[3]:
                        box[3] = c
                else:
                    boxes[colour] = [r, r, c, c]

        colours = list(boxes)
        later = {colour: set() for colour in colours}
        for colour in colours:
            top, bottom, left, right = boxes[colour]
            for r in range(top, bottom + 1):
                row = targetGrid[r]
                for c in range(left, right + 1):
                    if row[c] != colour:
                        later[colour].add(row[c])

        incoming = {colour: 0 for colour in colours}
        for colour in colours:
            for after in later[colour]:
                incoming[after] += 1

        queue = deque(colour for colour in colours if incoming[colour] == 0)
        printed = 0
        while queue:
            colour = queue.popleft()
            printed += 1
            for after in later[colour]:
                incoming[after] -= 1
                if incoming[after] == 0:
                    queue.append(after)
        return printed == len(colours)
