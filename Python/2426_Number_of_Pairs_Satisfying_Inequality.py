class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        # Condition: nums1[i]-nums1[j] <= nums2[i]-nums2[j]
        # => (nums1[i]-nums2[i]) <= (nums1[j]-nums2[j])
        # Count pairs i<j where d[i] <= d[j], using merge sort
        d = [a - b for a, b in zip(nums1, nums2)]

        def merge_count(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, lc = merge_count(arr[:mid])
            right, rc = merge_count(arr[mid:])
            count = lc + rc
            j = 0
            for x in left:
                while j < len(right) and right[j] < x:
                    j += 1
                count += len(right) - j
            return sorted(left + right), count

        _, ans = merge_count(d)
        return ans
