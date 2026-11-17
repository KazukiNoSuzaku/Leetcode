# Author: Kaustav Ghosh
# Problem: Maximum of Minimum Values in All Subarrays
# Approach: Instead of asking which window gives each answer, I ask what each element can be the answer for. Monotonic stacks give every element the widest window in which it is the minimum, bounded by the nearest strictly smaller element on each side; call that width w. Then nums[i] is attainable as the minimum of a window of size w, and of every smaller size inside that window, but of nothing larger. So I record nums[i] as a candidate at size w only, and finish with one sweep from the largest size down to the smallest that carries each answer backwards, since whatever is attainable at a size is attainable at every smaller one. The whole array's minimum always has the full width, so the largest size is always filled and the sweep fills the rest; the result is O(n) time.

class Solution(object):
    def findMaximums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = len(nums)
        left = [-1] * total
        right = [total] * total

        stack = []
        for index in range(total):
            while stack and nums[stack[-1]] >= nums[index]:
                stack.pop()
            if stack:
                left[index] = stack[-1]
            stack.append(index)

        stack = []
        for index in range(total - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[index]:
                stack.pop()
            if stack:
                right[index] = stack[-1]
            stack.append(index)

        answers = [0] * total
        for index in range(total):
            width = right[index] - left[index] - 1
            if nums[index] > answers[width - 1]:
                answers[width - 1] = nums[index]

        for size in range(total - 2, -1, -1):
            if answers[size + 1] > answers[size]:
                answers[size] = answers[size + 1]

        return answers
