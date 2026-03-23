# Author: Kaustav Ghosh
# Problem 1850: Minimum Adjacent Swaps to Reach the Kth Smallest Number

class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        original = list(num)
        target = list(num)
        # Get kth next permutation
        for _ in range(k):
            self.nextPermutation(target)
        # Count swaps to transform original to target
        swaps = 0
        arr = original[:]
        for i in range(len(arr)):
            if arr[i] != target[i]:
                j = i + 1
                while arr[j] != target[i]:
                    j += 1
                while j > i:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                    swaps += 1
        return swaps

    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
