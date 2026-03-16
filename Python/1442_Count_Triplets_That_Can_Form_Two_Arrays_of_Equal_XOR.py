# Author: Kaustav Ghosh
# Problem: Count Triplets That Can Form Two Arrays of Equal XOR
# Approach: XOR prefix; if prefix[i] == prefix[k+1], count (k-i) pairs

class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        count = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    count += k - i
        return count
