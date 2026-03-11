# Return true if the array can be partitioned into three contiguous parts with equal sum.

# Author: Kaustav Ghosh

class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        parts = cur = 0
        for x in arr:
            cur += x
            if cur == target * (parts + 1):
                parts += 1
                if parts == 3:
                    return True
        return False
