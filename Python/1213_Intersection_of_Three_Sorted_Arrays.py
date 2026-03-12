# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Three pointers advancing the smallest

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        result = []
        i = j = k = 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                i += 1
            elif arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1
        return result
