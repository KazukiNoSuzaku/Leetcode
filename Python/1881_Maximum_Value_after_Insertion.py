# Author: Kaustav Ghosh
# Problem: Maximum Value after Insertion
# Approach: Inserting a digit always lengthens the number, so the position is chosen by comparing magnitudes digit by digit from the left. For a positive number the value is largest when the inserted digit lands before the first digit smaller than it, since pushing a smaller digit rightwards raises every place it passes. For a negative number the aim is the smallest magnitude, so the digit goes before the first digit larger than it, and the leading minus sign is skipped over rather than compared. If no such digit exists the insertion belongs at the very end.

class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        digit = str(x)
        if n[0] == "-":
            for index in range(1, len(n)):
                if int(n[index]) > x:
                    return n[:index] + digit + n[index:]
        else:
            for index in range(len(n)):
                if int(n[index]) < x:
                    return n[:index] + digit + n[index:]
        return n + digit
