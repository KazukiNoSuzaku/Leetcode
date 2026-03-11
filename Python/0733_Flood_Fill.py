# Perform flood fill on an image starting from pixel (sr, sc).

# Author: Kaustav Ghosh

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        orig = image[sr][sc]
        if orig == color: return image
        rows, cols = len(image), len(image[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != orig: return
            image[r][c] = color
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
        dfs(sr, sc)
        return image
