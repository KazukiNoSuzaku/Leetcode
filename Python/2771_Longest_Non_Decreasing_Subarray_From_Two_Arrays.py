class Solution:
    def maxNonDecreasingLength(self, nums1: list[int], nums2: list[int]) -> int:
        dp1 = dp2 = 1
        ans = 1
        for i in range(1, len(nums1)):
            new1 = new2 = 1
            if nums1[i] >= nums1[i - 1]:
                new1 = max(new1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                new1 = max(new1, dp2 + 1)
            if nums2[i] >= nums1[i - 1]:
                new2 = max(new2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                new2 = max(new2, dp2 + 1)
            dp1, dp2 = new1, new2
            ans = max(ans, dp1, dp2)
        return ans
