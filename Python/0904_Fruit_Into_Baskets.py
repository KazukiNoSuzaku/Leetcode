# Find longest subarray with at most 2 distinct fruit types.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def totalFruit(self, fruits):
        count = defaultdict(int)
        left = res = 0
        for right, fruit in enumerate(fruits):
            count[fruit] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0: del count[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
        return res
