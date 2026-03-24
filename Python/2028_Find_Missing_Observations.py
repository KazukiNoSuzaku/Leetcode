# Author: Kaustav Ghosh
# Problem 2028: Find Missing Observations

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_needed = mean * (n + m) - sum(rolls)
        if total_needed < n or total_needed > 6 * n:
            return []
        base = total_needed // n
        remainder = total_needed % n
        result = [base] * n
        for i in range(remainder):
            result[i] += 1
        return result
