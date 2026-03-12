# Author: Kaustav Ghosh
# BFS with keys and discovered boxes, open boxes when possible

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        from collections import deque
        has_box = set(initialBoxes)
        has_key = set()
        opened = set()
        queue = deque()
        total = 0

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
                opened.add(box)

        while queue:
            box = queue.popleft()
            total += candies[box]
            for key in keys[box]:
                has_key.add(key)
                if key in has_box and key not in opened:
                    opened.add(key)
                    queue.append(key)
            for contained in containedBoxes[box]:
                has_box.add(contained)
                if contained not in opened and (status[contained] == 1 or contained in has_key):
                    opened.add(contained)
                    queue.append(contained)
        return total
