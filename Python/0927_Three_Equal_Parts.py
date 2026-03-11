# Split array into three equal binary value parts.

# Author: Kaustav Ghosh

class Solution(object):
    def threeEqualParts(self, arr):
        ones = arr.count(1)
        if ones % 3: return [-1, -1]
        if ones == 0: return [0, 2]
        k = ones // 3
        p1 = p2 = p3 = 0
        cnt = 0
        for i, x in enumerate(arr):
            if x:
                cnt += 1
                if cnt == 1: p1 = i
                if cnt == k + 1: p2 = i
                if cnt == 2*k + 1: p3 = i
        while p3 < len(arr) and arr[p1] == arr[p2] == arr[p3]:
            p1 += 1; p2 += 1; p3 += 1
        if p3 == len(arr): return [p1 - 1, p2]
        return [-1, -1]
