# Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of
# black lonely pixels. A black lonely pixel is a 'B' that is alone in its row and column.

# Author: Kaustav Ghosh

class Solution(object):
    def findLonelyPixel(self, picture):
        rows = [row.count('B') for row in picture]
        cols = [sum(r[j] == 'B' for r in picture) for j in range(len(picture[0]))]
        return sum(
            1 for i in range(len(picture)) for j in range(len(picture[0]))
            if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1
        )
