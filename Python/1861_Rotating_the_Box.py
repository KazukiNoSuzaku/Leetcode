# Author: Kaustav Ghosh
# Problem: Rotating the Box
# Approach: In each original row let stones fall toward the right wall/obstacles (two-pointer settle), then rotate the box 90 degrees clockwise so gravity points down

class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        rows, cols = len(box), len(box[0])

        for row in box:
            write = cols - 1  # rightmost slot a falling stone can land in
            for c in range(cols - 1, -1, -1):
                if row[c] == '*':
                    write = c - 1
                elif row[c] == '#':
                    row[c] = '.'
                    row[write] = '#'
                    write -= 1

        # Rotate 90 degrees clockwise: column c (top->bottom) becomes new row
        return [[box[rows - 1 - r][c] for r in range(rows)] for c in range(cols)]
