# Author: Kaustav Ghosh
# Problem: Number of Pairs of Strings With Concatenation Equal to Target
# Approach: With at most a hundred strings there are only a few thousand ordered pairs, so every pair of distinct indices is examined directly, which also keeps the counting faithful to the statement's rule that the two orderings of a pair are separate answers and that duplicate strings at different indices count separately. Before joining two strings the test first compares their combined length against the target's, which rejects almost every pair immediately and means the actual concatenation is only built for candidates that could possibly match.

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        width = len(target)
        found = 0
        for first in range(len(nums)):
            head = nums[first]
            for second in range(len(nums)):
                if first == second:
                    continue
                tail = nums[second]
                if len(head) + len(tail) != width:
                    continue
                if head + tail == target:
                    found += 1
        return found
