# Author: Kaustav Ghosh
# Problem: Minimum Number of Removals to Make Mountain Array
# Approach: Removing the fewest elements is the same as keeping the most, and what must be kept is a strictly increasing run up to some peak followed by a strictly decreasing run, which is exactly a longest increasing subsequence ending at the peak glued to a longest decreasing subsequence starting there. So I compute, for every index, the longest strictly increasing subsequence ending at it and the longest strictly decreasing one starting at it, and the best mountain through that index is their sum less one for the shared peak. An index only qualifies as a peak if both sides have at least two elements, since a mountain needs a genuine rise and a genuine fall.

class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        rising = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and rising[j] + 1 > rising[i]:
                    rising[i] = rising[j] + 1

        falling = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i] and falling[j] + 1 > falling[i]:
                    falling[i] = falling[j] + 1

        tallest = 0
        for i in range(n):
            if rising[i] > 1 and falling[i] > 1:
                height = rising[i] + falling[i] - 1
                if height > tallest:
                    tallest = height
        return n - tallest
