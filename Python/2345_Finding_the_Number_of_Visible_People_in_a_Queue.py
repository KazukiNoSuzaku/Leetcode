# Author: Kaustav Ghosh
# 2345. Finding the Number of Visible People in a Queue
# https://leetcode.com/problems/finding-the-number-of-visible-people-in-a-queue/
# Difficulty: Hard
#
# Monotonic stack from right: for each person, count how many people they can see.
# Pop shorter people from stack (they are visible), then if stack non-empty,
# the next taller person is also visible.

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stack = []  # decreasing monotonic stack
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1  # can see the next taller person
            ans[i] = count
            stack.append(heights[i])
        return ans
