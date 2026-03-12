# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: DP where dp[i] = min operations to make arr1[:i+1] strictly increasing ending with value i

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        import bisect
        arr2 = sorted(set(arr2))
        # dp: {last_value: min_operations}
        dp = {-1: 0}
        for num in arr1:
            new_dp = {}
            for prev, ops in dp.items():
                # Option 1: keep num if it's greater than prev
                if num > prev:
                    if num not in new_dp or new_dp[num] > ops:
                        new_dp[num] = ops
                # Option 2: replace with smallest value from arr2 > prev
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    val = arr2[idx]
                    if val not in new_dp or new_dp[val] > ops + 1:
                        new_dp[val] = ops + 1
            dp = new_dp
            if not dp:
                return -1
        return min(dp.values())
