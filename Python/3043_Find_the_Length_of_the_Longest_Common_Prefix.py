from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        for x in arr1:
            s = str(x)
            for i in range(1, len(s) + 1):
                prefix_set.add(s[:i])
        ans = 0
        for x in arr2:
            s = str(x)
            for i in range(1, len(s) + 1):
                if s[:i] in prefix_set:
                    ans = max(ans, i)
        return ans
