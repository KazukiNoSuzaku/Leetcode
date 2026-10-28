# Author: Kaustav Ghosh
# Problem: Decode XORed Permutation
# Approach: The encoding alone cannot be unrolled without a starting value, but two facts recover it. First, the original is a permutation of one through n, so the exclusive-or of all its entries is known outright. Second, taking the encoded entries at odd positions pairs up the originals as the second with the third, the fourth with the fifth and so on, which because n is odd covers every entry except the first exactly once; combining that with the total therefore isolates the first entry. From there each encoded value unrolls the next, since exclusive-or undoes itself.

class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1

        everything = 0
        for value in range(1, n + 1):
            everything ^= value

        # Odd positions pair up every original except the first.
        without_first = 0
        for i in range(1, len(encoded), 2):
            without_first ^= encoded[i]

        original = [everything ^ without_first]
        for value in encoded:
            original.append(original[-1] ^ value)
        return original
