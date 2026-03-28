# Author: Kaustav Ghosh
# Problem: 2157. Groups of Strings
# URL: https://leetcode.com/problems/groups-of-strings/
# Approach: Union-Find with bitmask; two strings are connected if one can be
# obtained by adding, removing, or replacing exactly one character.
# Represent each word as a 26-bit bitmask of its unique characters.

class Solution(object):
    def groupStrings(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        parent = {}
        size = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                size[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size.get(rx, 0) < size.get(ry, 0):
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] = size.get(rx, 0) + size.get(ry, 0)

        mask_to_word = {}

        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            if mask not in parent:
                parent[mask] = mask
                size[mask] = 1
            else:
                size[find(mask)] += 1
                union(mask_to_word[mask], mask)
                continue
            mask_to_word[mask] = mask

        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))

            # try removing each set bit
            tmp = mask
            while tmp:
                bit = tmp & (-tmp)
                union(mask, mask ^ bit)
                tmp -= bit

            # try adding each unset bit
            tmp = (~mask) & ((1 << 26) - 1)
            while tmp:
                bit = tmp & (-tmp)
                union(mask, mask | bit)
                tmp -= bit

            # try replacing: remove one bit and add another
            tmp = mask
            while tmp:
                bit = tmp & (-tmp)
                tmp2 = (~mask) & ((1 << 26) - 1)
                while tmp2:
                    bit2 = tmp2 & (-tmp2)
                    union(mask, (mask ^ bit) | bit2)
                    tmp2 -= bit2
                tmp -= bit

        roots = {}
        for mask in parent:
            r = find(mask)
            if r not in roots:
                roots[r] = 0
            roots[r] += size.get(mask, 0) if mask == r else 0

        # recompute: count nodes per component and sum sizes
        comp_size = {}
        comp_count = {}
        for mask in parent:
            r = find(mask)
            comp_count[r] = comp_count.get(r, 0) + 1
        # size[root] holds total words in that component
        num_groups = len(comp_count)
        max_size = max(size[find(m)] for m in parent) if parent else 0
        return [num_groups, max_size]
