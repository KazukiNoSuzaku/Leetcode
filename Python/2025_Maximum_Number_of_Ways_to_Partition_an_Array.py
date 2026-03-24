# Author: Kaustav Ghosh
# Problem 2025: Maximum Number of Ways to Partition an Array

from collections import Counter

class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        # diff[i] = prefix[i] - (total - prefix[i]) = 2*prefix[i] - total for i in [0, n-2]
        # Without changing: count how many i where diff[i] == 0

        # If we change nums[j] to k, delta = k - nums[j]
        # For i < j: new diff = diff[i] - delta (prefix unchanged, total changes)
        # Wait, let's think differently.
        # Original: partition at i means left = prefix[i], right = total - prefix[i]
        # Equal when prefix[i] = total - prefix[i] => 2*prefix[i] = total

        # If change nums[j] to k: delta = k - nums[j]
        # For i >= j: new prefix[i] = prefix[i] + delta, new total = total + delta
        #   Equal when 2*(prefix[i]+delta) = total+delta => 2*prefix[i]+delta = total
        # For i < j: new prefix[i] = prefix[i], new total = total + delta
        #   Equal when 2*prefix[i] = total + delta

        # Count of 2*prefix[i] - total for i < j (right side needs val == delta)
        # Count of 2*prefix[i] - total for i >= j (left side needs val == -delta... wait)

        # For i < j: need 2*prefix[i] = total + delta => 2*prefix[i] - total = delta
        # For i >= j: need 2*prefix[i] + delta = total => 2*prefix[i] - total = -delta

        diffs = [2 * prefix[i] - total for i in range(n - 1)]

        # No change: count diffs == 0
        result = diffs.count(0)

        # right_count starts with count of all diffs
        right_count = Counter(diffs)
        left_count = Counter()

        for j in range(n):
            delta = k - nums[j]
            # partitions before j need diff == delta
            # partitions at or after j need diff == -delta
            ways = left_count.get(delta, 0) + right_count.get(-delta, 0)
            result = max(result, ways)
            # Move diff[j] from right to left (if j < n-1, diff[j] exists)
            if j < n - 1:
                right_count[diffs[j]] -= 1
                left_count[diffs[j]] += 1

        return result
