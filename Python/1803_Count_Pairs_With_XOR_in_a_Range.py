# Author: Kaustav Ghosh
# Problem: Count Pairs With XOR in a Range
# Approach: countInRange = countLess(high+1) - countLess(low). A bitwise trie of previously seen numbers lets each new value count how many partners give XOR below a limit in O(bits)

class Solution(object):
    BITS = 14  # values < 2^15

    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        return self._count_less(nums, high + 1) - self._count_less(nums, low)

    def _count_less(self, nums, limit):
        root = {}

        def insert(num):
            node = root
            for b in range(self.BITS, -1, -1):
                bit = (num >> b) & 1
                if bit not in node:
                    node[bit] = {'cnt': 0}
                node = node[bit]
                node['cnt'] += 1

        def query(num):
            node = root
            total = 0
            for b in range(self.BITS, -1, -1):
                if node is None:
                    break
                num_bit = (num >> b) & 1
                lim_bit = (limit >> b) & 1
                if lim_bit == 1:
                    same = node.get(num_bit)          # XOR bit 0 here -> all below limit
                    if same:
                        total += same['cnt']
                    node = node.get(1 - num_bit)       # continue where XOR bit is 1
                else:
                    node = node.get(num_bit)           # XOR bit must be 0 to stay below
            return total

        count = 0
        for num in nums:
            count += query(num)
            insert(num)
        return count
