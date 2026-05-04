from collections import Counter

class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        # Must fix all positions where nums1[i] == nums2[i] via swaps within nums1.
        # Collect those bad positions into a swap pool. If one value dominates
        # (count > pool_size/2), we must pull in extra good positions (cheapest first)
        # with non-dominant values until the pool is balanced enough to permute freely.
        n = len(nums1)
        total_cost = 0
        swap_count = 0
        freq = Counter()
        dominant_val = -1
        dominant_count = 0

        for i in range(n):
            if nums1[i] == nums2[i]:
                total_cost += i
                swap_count += 1
                freq[nums1[i]] += 1
                if freq[nums1[i]] > dominant_count:
                    dominant_count = freq[nums1[i]]
                    dominant_val = nums1[i]

        for i in range(n):
            if dominant_count * 2 <= swap_count:
                break
            # Add good position i with a non-dominant value to balance the pool
            if nums1[i] != nums2[i] and nums1[i] != dominant_val:
                total_cost += i
                swap_count += 1

        return total_cost
