# Author: Kaustav Ghosh
# Problem: Count Hills and Valleys in an Array
# Approach: Collapse consecutive equal values (they share hill/valley status), then any interior element that is greater than both neighbors is a hill and any that is smaller than both is a valley

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # remove consecutive duplicates
        dedup = [nums[0]]
        for x in nums[1:]:
            if x != dedup[-1]:
                dedup.append(x)

        count = 0
        for i in range(1, len(dedup) - 1):
            if dedup[i] > dedup[i - 1] and dedup[i] > dedup[i + 1]:
                count += 1
            elif dedup[i] < dedup[i - 1] and dedup[i] < dedup[i + 1]:
                count += 1
        return count
