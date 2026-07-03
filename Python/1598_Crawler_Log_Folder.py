# Author: Kaustav Ghosh
# Problem: Crawler Log Folder
# Approach: Track depth only; "../" steps up (never past root), "./" stays, any other op goes one level deeper. Depth is the answer

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        depth = 0
        for op in logs:
            if op == '../':
                depth = max(0, depth - 1)
            elif op != './':
                depth += 1
        return depth
