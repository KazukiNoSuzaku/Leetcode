# Author: Kaustav Ghosh
# Count numbers with even number of digits

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(1 for n in nums if len(str(n)) % 2 == 0)
