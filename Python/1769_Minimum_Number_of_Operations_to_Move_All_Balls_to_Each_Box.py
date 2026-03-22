# Author: Kaustav Ghosh

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        ans = [0] * n
        # Left to right pass
        count = 0
        ops = 0
        for i in range(n):
            ans[i] += ops
            count += int(boxes[i])
            ops += count
        # Right to left pass
        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += ops
            count += int(boxes[i])
            ops += count
        return ans
