class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        # Two-pointer merge on sorted id arrays; sum values for matching ids.
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            id1, v1 = nums1[i]
            id2, v2 = nums2[j]
            if id1 < id2:
                result.append([id1, v1]); i += 1
            elif id1 > id2:
                result.append([id2, v2]); j += 1
            else:
                result.append([id1, v1 + v2]); i += 1; j += 1
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        return result
