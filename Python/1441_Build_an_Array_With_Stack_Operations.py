# Author: Kaustav Ghosh
# Problem: Build an Array With Stack Operations
# Approach: Simulate push/pop to build target from stream 1..n

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result = []
        idx = 0
        for num in range(1, n + 1):
            if idx >= len(target):
                break
            result.append("Push")
            if num == target[idx]:
                idx += 1
            else:
                result.append("Pop")
        return result
