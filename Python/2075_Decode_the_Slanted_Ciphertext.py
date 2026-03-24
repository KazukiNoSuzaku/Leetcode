# Author: Kaustav Ghosh
# Problem 2075: Decode the Slanted Ciphertext

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 1:
            return encodedText
        cols = len(encodedText) // rows
        # Build grid
        grid = []
        for r in range(rows):
            grid.append(encodedText[r * cols:(r + 1) * cols])

        result = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                result.append(grid[r][c])
                r += 1
                c += 1

        # Remove trailing spaces
        text = ''.join(result).rstrip()
        return text
