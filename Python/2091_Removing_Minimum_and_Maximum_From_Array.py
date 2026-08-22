# Author: Kaustav Ghosh
# Problem: Removing Minimum and Maximum From Array
# Approach: Deletions only come from the front or back. Given the positions of the min and max (i < j), the options are: both from the front (j+1), both from the back (n-i), or one from each end ((i+1) + (n-j)). Take the minimum

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        i, j = min(i, j), max(i, j)
        return min(j + 1, n - i, (i + 1) + (n - j))
