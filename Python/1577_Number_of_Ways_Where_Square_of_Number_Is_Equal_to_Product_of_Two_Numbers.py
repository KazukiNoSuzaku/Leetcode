# Author: Kaustav Ghosh
# Problem: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# Approach: Enumerating every pair in the other array for every square would be a million pairs per square, so instead I note that a pair multiplying to a target is a pair of complementary divisors of it: for each square I walk the distinct values of the other array and ask whether the target divides evenly by that value and whether the quotient is also present. Each unordered pair is then seen twice (once from each side) except when the two factors coincide, which is why the equal case uses c*(c-1)/2 and the rest is halved. The whole thing is done once in each direction.

from collections import Counter


class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def count(squares, others):
            tally = Counter(others)
            items = list(tally.items())
            total = 0
            for value in squares:
                target = value * value
                pairs = 0
                for factor, times in items:
                    if target % factor:
                        continue
                    other = target // factor
                    if other == factor:
                        pairs += times * (times - 1)
                    elif other in tally:
                        pairs += times * tally[other]
                total += pairs // 2
            return total

        return count(nums1, nums2) + count(nums2, nums1)
