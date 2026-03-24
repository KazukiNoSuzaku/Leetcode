# Author: Kaustav Ghosh
# Problem 2059: Minimum Operations to Convert Number

from collections import deque

class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        visited = set()
        visited.add(start)
        queue = deque([(start, 0)])
        while queue:
            val, steps = queue.popleft()
            for num in nums:
                for nxt in [val + num, val - num, val ^ num]:
                    if nxt == goal:
                        return steps + 1
                    if 0 <= nxt <= 1000 and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
        return -1
