# Author: Kaustav Ghosh
# Problem: Find Missing Observations
# Approach: The missing rolls must sum to mean*(m+n) minus the known sum. If that target is outside [n, 6n] it is impossible; otherwise spread it as evenly as possible, giving the remainder dice one extra pip

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        missing_sum = mean * (m + n) - sum(rolls)
        if missing_sum < n or missing_sum > 6 * n:
            return []
        base, rem = divmod(missing_sum, n)
        return [base + 1] * rem + [base] * (n - rem)
