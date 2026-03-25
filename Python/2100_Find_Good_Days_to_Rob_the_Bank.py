# Author: Kaustav Ghosh
# Problem 2100: Find Good Days to Rob the Bank

class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        n = len(security)
        # non_inc[i] = number of consecutive non-increasing days ending at i
        non_inc = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                non_inc[i] = non_inc[i - 1] + 1

        # non_dec[i] = number of consecutive non-decreasing days starting at i
        non_dec = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                non_dec[i] = non_dec[i + 1] + 1

        result = []
        for i in range(n):
            if non_inc[i] >= time and non_dec[i] >= time:
                result.append(i)
        return result
