# Author: Kaustav Ghosh
# Problem: Number of Visible People in a Queue
# Approach: Scan right to left with a decreasing monotonic stack. Person i sees every shorter person popped while placing them (each is visible until a taller one blocks), plus the first taller person still on the stack

class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        answer = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            count = 0
            while stack and stack[-1] < h:
                stack.pop()
                count += 1
            if stack:                 # a taller person blocks further view
                count += 1
            answer[i] = count
            stack.append(h)
        return answer
