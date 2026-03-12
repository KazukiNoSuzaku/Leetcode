# Author: Kaustav Ghosh
# 1053. Previous Permutation With One Swap
# https://leetcode.com/problems/previous-permutation-with-one-swap/

class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        # Find rightmost i where arr[i] > arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
        if i < 0:
            return arr
        # Find rightmost j > i where arr[j] < arr[i] and arr[j] is maximum such value
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        # Move j left to avoid duplicates (take the leftmost of duplicates)
        while j > i + 1 and arr[j] == arr[j-1]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr
