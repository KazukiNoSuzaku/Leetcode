# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make a Subsequence
# Approach: Insertions never reorder what is already present, so the elements of the target that are already usable in order can be kept and only the rest need inserting; the fewest insertions is therefore the target's length minus the longest piece of it that already appears as a subsequence of the array. Because the target's values are distinct, each can be replaced by its position in the target, and anything not in the target is discarded outright; a common subsequence then becomes an increasing run of those positions, which is a longest increasing subsequence. That is found in log-linear time by keeping, for each possible run length, the smallest value that can end such a run and binary searching the right slot for each element.

from bisect import bisect_left


class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        rank = {value: i for i, value in enumerate(target)}
        positions = [rank[value] for value in arr if value in rank]

        tails = []
        for position in positions:
            slot = bisect_left(tails, position)
            if slot == len(tails):
                tails.append(position)
            else:
                tails[slot] = position
        return len(target) - len(tails)
