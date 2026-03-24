# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stack = []  # monotonic decreasing stack
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1  # can see the first taller person
            ans[i] = count
            stack.append(heights[i])
        return ans
