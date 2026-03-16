# Author: Kaustav Ghosh
# Problem: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
# Approach: Greedy subtract largest Fibonacci number

class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        count = 0
        for f in reversed(fibs):
            if f <= k:
                k -= f
                count += 1
            if k == 0:
                break
        return count
