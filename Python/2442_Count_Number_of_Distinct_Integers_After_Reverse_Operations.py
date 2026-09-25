# Author: Kaustav Ghosh
# Problem: Count Number of Distinct Integers After Reverse Operations
# Approach: The final array holds every original number plus the reverse of each one, and only distinct values matter, so collect both into a set and return its size

class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = set(nums)
        distinct.update(int(str(x)[::-1]) for x in nums)
        return len(distinct)
