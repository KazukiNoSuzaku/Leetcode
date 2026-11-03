# Author: Kaustav Ghosh
# Problem: Maximum Score of a Good Subarray
# Approach: Every candidate subarray has to contain index k, so the search can start from that single element and widen one step at a time, which means only the n windows that grow outward from k need to be considered rather than all pairs. At each step the side with the larger neighbour is taken, because extending towards the smaller value would drop the running minimum earlier than necessary while adding the same single unit of length. The minimum only ever changes to the newly admitted element, so each step is constant work.

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = right = k
        smallest = nums[k]
        best = nums[k]
        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
                value = nums[right]
            elif right == n - 1 or nums[left - 1] >= nums[right + 1]:
                left -= 1
                value = nums[left]
            else:
                right += 1
                value = nums[right]
            if value < smallest:
                smallest = value
            score = smallest * (right - left + 1)
            if score > best:
                best = score
        return best
