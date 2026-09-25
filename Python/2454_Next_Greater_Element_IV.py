# Author: Kaustav Ghosh
# Problem: Next Greater Element IV
# Approach: Two monotonic stacks. The first holds indices still waiting for any greater value; when one arrives they graduate to the second stack, which holds indices waiting for their second greater value. Moving them across in decreasing order of value keeps both stacks monotonic, so each index is pushed and popped once

class Solution(object):
    def secondGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [-1] * len(nums)
        waiting_first = []
        waiting_second = []
        for i, x in enumerate(nums):
            while waiting_second and nums[waiting_second[-1]] < x:
                answer[waiting_second.pop()] = x
            graduated = []
            while waiting_first and nums[waiting_first[-1]] < x:
                graduated.append(waiting_first.pop())
            waiting_second.extend(reversed(graduated))
            waiting_first.append(i)
        return answer
