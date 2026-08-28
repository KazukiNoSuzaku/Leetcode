# Author: Kaustav Ghosh
# Problem: Amount of New Area Painted Each Day
# Approach: Keep a jump-pointer union-find where each painted position points to the next free position. For a day's interval, repeatedly find the next free cell within it, paint it (link to the following cell), and count; path compression skips already-painted runs quickly

class Solution(object):
    def amountPainted(self, paint):
        """
        :type paint: List[List[int]]
        :rtype: List[int]
        """
        parent = {}

        def find(x):
            root = x
            while root in parent:
                root = parent[root]
            while x in parent:
                nxt = parent[x]
                parent[x] = root
                x = nxt
            return root

        result = []
        for start, end in paint:
            count = 0
            x = find(start)
            while x < end:
                count += 1
                parent[x] = x + 1
                x = find(x + 1)
            result.append(count)
        return result
