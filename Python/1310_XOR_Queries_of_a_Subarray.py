# For each query [l, r], return the XOR of elements arr[l] XOR ... XOR arr[r].

# Author: Kaustav Ghosh

class Solution(object):
    def xorQueries(self, arr, queries):
        prefix = [0] * (len(arr) + 1)
        for i, x in enumerate(arr):
            prefix[i+1] = prefix[i] ^ x
        return [prefix[r+1] ^ prefix[l] for l, r in queries]
