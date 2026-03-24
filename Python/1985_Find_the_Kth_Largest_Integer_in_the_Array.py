# Author: Kaustav Ghosh
# Problem 1985: Find the Kth Largest Integer in the Array

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=lambda x: (len(x), x), reverse=True)
        return nums[k - 1]
