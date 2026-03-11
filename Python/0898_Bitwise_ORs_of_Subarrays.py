# Count distinct results of bitwise OR of all subarrays.

# Author: Kaustav Ghosh

class Solution(object):
    def subarrayBitwiseORs(self, arr):
        res = set()
        cur = set()
        for x in arr:
            cur = {x | y for y in cur} | {x}
            res |= cur
        return len(res)
