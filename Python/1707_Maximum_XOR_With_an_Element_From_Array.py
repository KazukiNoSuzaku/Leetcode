# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        indexed = sorted(enumerate(queries), key=lambda x: x[1][1])
        result = [-1] * len(queries)

        trie = {}
        idx = 0

        def insert(num):
            node = trie
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        def query(num):
            if not trie:
                return -1
            node = trie
            xor_val = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                want = 1 - bit
                if want in node:
                    xor_val |= (1 << i)
                    node = node[want]
                elif bit in node:
                    node = node[bit]
                else:
                    return -1
            return xor_val

        for qi, (xi, mi) in indexed:
            while idx < len(nums) and nums[idx] <= mi:
                insert(nums[idx])
                idx += 1
            result[qi] = query(xi)
        return result
