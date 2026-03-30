# Author: Kaustav Ghosh
# Problem: 2177. Find Three Consecutive Integers That Sum to a Given Number
# URL: https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
# Approach: Three consecutive integers are (n-1, n, n+1) summing to 3*n.
#           If num % 3 == 0, return [num//3 - 1, num//3, num//3 + 1], else [].

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
