# Author: Kaustav Ghosh

class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1
        # XOR of all numbers 1 to n
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        # XOR of encoded[1], encoded[3], ... gives xor of perm[1]^perm[2]^...^perm[n-1]
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]
        # perm[0] = total_xor ^ odd_xor
        perm = [total_xor ^ odd_xor]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
