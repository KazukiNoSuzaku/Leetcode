# Author: Kaustav Ghosh
# Problem: Decode XORed Permutation
# Approach: XOR of 1..n gives the whole permutation's XOR. The odd-indexed encoded entries pair up perm[1..n-1] exactly, so XOR-ing them out leaves perm[0]; the rest unrolls

class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1

        total = 0
        for i in range(1, n + 1):
            total ^= i

        rest = 0  # perm[1] ^ perm[2] ^ ... ^ perm[n-1]
        for i in range(1, len(encoded), 2):
            rest ^= encoded[i]

        perm = [total ^ rest]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
