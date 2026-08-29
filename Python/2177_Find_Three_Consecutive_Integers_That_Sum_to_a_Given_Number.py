# Author: Kaustav Ghosh
# Problem: Find Three Consecutive Integers That Sum to a Given Number
# Approach: Three consecutive integers around x sum to 3x, so a solution exists only when num is divisible by 3; then the middle is num/3

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 != 0:
            return []
        mid = num // 3
        return [mid - 1, mid, mid + 1]
