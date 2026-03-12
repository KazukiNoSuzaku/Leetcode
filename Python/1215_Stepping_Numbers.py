# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: BFS generating stepping numbers from each digit 1-9

class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        from collections import deque
        result = []
        if low == 0:
            result.append(0)

        queue = deque(range(1, 10))
        while queue:
            num = queue.popleft()
            if num > high:
                continue
            if num >= low:
                result.append(num)
            last_digit = num % 10
            if last_digit > 0:
                queue.append(num * 10 + last_digit - 1)
            if last_digit < 9:
                queue.append(num * 10 + last_digit + 1)
        return sorted(result)
