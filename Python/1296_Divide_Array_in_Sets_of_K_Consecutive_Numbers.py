# Author: Kaustav Ghosh
# Greedy: always start from smallest available number, form k consecutive

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        if len(nums) % k != 0:
            return False
        count = Counter(nums)
        for num in sorted(count):
            if count[num] > 0:
                freq = count[num]
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False
                    count[i] -= freq
        return True
