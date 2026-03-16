# Author: Kaustav Ghosh
# Problem: Check If Array Pairs Are Divisible by k
# Approach: Count remainders and pair complements

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        count = [0] * k
        for num in arr:
            count[num % k] += 1
        if count[0] % 2 != 0:
            return False
        for i in range(1, k):
            if count[i] != count[k - i]:
                return False
        return True
