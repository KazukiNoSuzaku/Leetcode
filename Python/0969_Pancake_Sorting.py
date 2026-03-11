# Sort an array using pancake flips. Return any sequence of flips.
# A flip of k reverses the first k elements.

# Author: Kaustav Ghosh

class Solution(object):
    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_idx = arr.index(size)
            if max_idx == size - 1: continue
            if max_idx != 0:
                res.append(max_idx + 1)
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
            res.append(size)
            arr[:size] = arr[:size][::-1]
        return res
