# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Simulate rounds until array is stable

class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        changed = True
        while changed:
            changed = False
            new_arr = list(arr)
            for i in range(1, len(arr) - 1):
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new_arr[i] -= 1
                    changed = True
                elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new_arr[i] += 1
                    changed = True
            arr = new_arr
        return arr
