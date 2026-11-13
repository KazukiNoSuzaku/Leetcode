# Author: Kaustav Ghosh
# Problem: Minimum Absolute Difference Queries
# Approach: The values only run to a hundred, so the smallest difference inside a range depends on nothing more than which of those hundred values appear in it; once the present values are known in ascending order the answer is the smallest gap between consecutive ones. Presence is decided without scanning the range by keeping, for each value, the sorted list of positions where it occurs, locating the first occurrence at or after the range start and checking it has not passed the range end, which is a single binary search rather than a pair of them. A query therefore costs a hundred such checks rather than its own length, and the memory stays proportional to the array rather than to values times length, which a table of prefix counts per value would not.

class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from bisect import bisect_left

        LIMIT = 101
        places = [[] for _ in range(LIMIT)]
        for index, value in enumerate(nums):
            places[value].append(index)

        answers = []
        for left, right in queries:
            previous = 0
            best = -1
            for value in range(1, LIMIT):
                spots = places[value]
                at = bisect_left(spots, left)
                if at == len(spots) or spots[at] > right:
                    continue
                if previous and (best < 0 or value - previous < best):
                    best = value - previous
                previous = value
            answers.append(best)
        return answers
