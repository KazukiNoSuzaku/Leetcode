# Author: Kaustav Ghosh
# Problem: Maximum XOR With an Element From Array
# Approach: Answer offline sorted by the limit m; insert nums <= m into a binary trie as m grows, then greedily walk the trie preferring the opposite bit to maximize XOR

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        HIGH = 29  # values < 2^30
        root = {}

        def insert(num):
            node = root
            for b in range(HIGH, -1, -1):
                bit = (num >> b) & 1
                node = node.setdefault(bit, {})

        def best_xor(num):
            node = root
            xor = 0
            for b in range(HIGH, -1, -1):
                bit = (num >> b) & 1
                want = 1 - bit
                if want in node:
                    xor |= (1 << b)
                    node = node[want]
                else:
                    node = node[bit]
            return xor

        nums.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i][1])
        res = [0] * len(queries)
        j = 0
        for qi in order:
            x, m = queries[qi]
            while j < len(nums) and nums[j] <= m:
                insert(nums[j])
                j += 1
            res[qi] = best_xor(x) if j > 0 else -1
        return res
