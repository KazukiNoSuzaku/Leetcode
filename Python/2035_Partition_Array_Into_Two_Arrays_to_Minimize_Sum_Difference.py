# Author: Kaustav Ghosh
# Problem: Partition Array Into Two Arrays to Minimize Sum Difference
# Approach: One side must hold exactly half the elements, so the difference between the two sides is the whole total minus twice the chosen side's sum, and the goal is a chosen sum as close as possible to half the total. Enumerating all ways to choose half of thirty elements is far too many, so the array is cut in two halves and every subset of each half is summed separately, which is only a few thousand sums per half. A valid choice takes some elements from the first half and exactly enough from the second to reach half the count, so the first half's sums are bucketed by how many elements they use and each bucket sorted; then each subset of the second half binary searches its own bucket for the nearest complement, with the immediate neighbours checked since the nearest value may sit on either side.

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        half = len(nums) // 2
        total = sum(nums)
        left = nums[:half]
        right = nums[half:]

        def subset_sums(values):
            sums = [0] * (1 << len(values))
            for mask in range(1, 1 << len(values)):
                lowest = mask & -mask
                index = lowest.bit_length() - 1
                sums[mask] = sums[mask ^ lowest] + values[index]
            return sums

        left_sums = subset_sums(left)
        right_sums = subset_sums(right)

        buckets = [[] for _ in range(half + 1)]
        for mask in range(1 << half):
            buckets[bin(mask).count('1')].append(left_sums[mask])
        for bucket in buckets:
            bucket.sort()

        best = None
        for mask in range(1 << half):
            taken = bin(mask).count('1')
            chosen = right_sums[mask]
            bucket = buckets[half - taken]
            wanted = total - 2 * chosen
            position = bisect.bisect_left(bucket, wanted // 2)
            for probe in (position - 1, position, position + 1):
                if 0 <= probe < len(bucket):
                    gap = total - 2 * (chosen + bucket[probe])
                    if gap < 0:
                        gap = -gap
                    if best is None or gap < best:
                        best = gap
        return best
