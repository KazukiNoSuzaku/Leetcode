from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)
        # Array must be periodic with period gcd(n,k); equalize each orbit to its median.
        result = 0
        for start in range(g):
            group = sorted(arr[start::g])
            median = group[len(group) // 2]
            result += sum(abs(x - median) for x in group)
        return result
