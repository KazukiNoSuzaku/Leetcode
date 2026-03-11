# Smooth an image matrix by replacing each cell with the floor average of its 3x3 neighborhood.

# Author: Kaustav Ghosh

class Solution(object):
    def imageSmoother(self, img):
        rows, cols = len(img), len(img[0])
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                total = count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            total += img[nr][nc]
                            count += 1
                res[r][c] = total // count
        return res
