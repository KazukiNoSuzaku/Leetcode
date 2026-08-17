# Author: Kaustav Ghosh
# Problem: Minimum Operations to Convert Number
# Approach: BFS over reachable values. From any x in [0,1000] apply x+num, x-num, x^num for each num. Reaching goal returns the step count; only values within [0,1000] can be operated on further

from collections import deque

class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        visited = [False] * 1001
        visited[start] = True
        dq = deque([(start, 0)])
        while dq:
            x, steps = dq.popleft()
            for num in nums:
                for nxt in (x + num, x - num, x ^ num):
                    if nxt == goal:
                        return steps + 1
                    if 0 <= nxt <= 1000 and not visited[nxt]:
                        visited[nxt] = True
                        dq.append((nxt, steps + 1))
        return -1
