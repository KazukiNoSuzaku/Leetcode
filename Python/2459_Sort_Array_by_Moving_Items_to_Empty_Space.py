# Author: Kaustav Ghosh
# Problem: Sort Array by Moving Items to Empty Space
# Approach: Every move drops an item into the empty space, so the arrangement decomposes into cycles of items that need to rotate. A cycle that already contains the empty space costs one move per item but one, while any other cycle costs an extra move to open it up. Both finished layouts are allowed, so count the cycles for the empty space at the front and at the back and take the cheaper

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def moves(destination):
            visited = [False] * n
            total = 0
            for start in range(n):
                if visited[start] or destination(nums[start]) == start:
                    continue
                length = 0
                holds_empty = False
                i = start
                while not visited[i]:
                    visited[i] = True
                    length += 1
                    holds_empty = holds_empty or nums[i] == 0
                    i = destination(nums[i])
                total += length - 1 if holds_empty else length + 1
            return total

        return min(moves(lambda value: value),
                   moves(lambda value: n - 1 if value == 0 else value - 1))
