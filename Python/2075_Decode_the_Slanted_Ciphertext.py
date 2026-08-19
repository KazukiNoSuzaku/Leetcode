# Author: Kaustav Ghosh
# Problem: Decode the Slanted Ciphertext
# Approach: The encoded text is the row-major reading of a rows x cols matrix filled diagonally. Recover the original by reading each down-right diagonal (starting from each column of the top row) and removing the trailing padding spaces

class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if rows == 0:
            return ""
        cols = len(encodedText) // rows
        chars = []
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                chars.append(encodedText[r * cols + c])
                r += 1
                c += 1
        return ''.join(chars).rstrip(' ')
