# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(chalk)
        k %= total
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
        return 0
