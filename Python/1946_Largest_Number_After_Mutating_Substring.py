# Author: Kaustav Ghosh
# https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        num = list(num)
        started = False
        for i in range(len(num)):
            d = int(num[i])
            if change[d] > d:
                started = True
                num[i] = str(change[d])
            elif change[d] < d and started:
                break
        return ''.join(num)
