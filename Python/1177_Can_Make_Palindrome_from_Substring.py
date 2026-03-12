# Author: Kaustav Ghosh
# Prefix XOR bitmask per character, check odd count chars <= 2*k+1

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(s[i]) - ord('a')))

        result = []
        for left, right, k in queries:
            diff = prefix[right + 1] ^ prefix[left]
            odd_count = bin(diff).count('1')
            result.append(odd_count // 2 <= k)
        return result
