# Author: Kaustav Ghosh

class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        # Trie-based approach
        def count_less(nums, limit):
            # Count pairs with XOR < limit
            trie = {}
            count = 0
            for num in nums:
                node = trie
                cur = trie
                bit = 14
                while bit >= 0:
                    b = (num >> bit) & 1
                    lb = (limit >> bit) & 1
                    if lb == 1:
                        # If limit bit is 1, pairs going same direction are all < limit
                        if b in cur:
                            count += cur[b].get('#', 0)
                        # Must go opposite direction
                        cur = cur.get(1 - b, None)
                    else:
                        # Must go same direction
                        cur = cur.get(b, None)
                    if cur is None:
                        break
                    bit -= 1
                # Insert num into trie
                node = trie
                for bit in range(14, -1, -1):
                    b = (num >> bit) & 1
                    if b not in node:
                        node[b] = {'#': 0}
                    node = node[b]
                    node['#'] = node.get('#', 0) + 1
            return count

        return count_less(nums, high + 1) - count_less(nums, low)
