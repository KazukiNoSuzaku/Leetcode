# Author: Kaustav Ghosh
# Problem: Crawler Log Folder
# Approach: Only the distance from the main folder matters, never the folder names, so the whole log collapses to a single depth counter: a named folder goes one level deeper, "../" comes back up but never past the main folder, and "./" changes nothing. The remaining depth at the end is exactly how many steps back are needed.

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        depth = 0
        for entry in logs:
            if entry == '../':
                if depth:
                    depth -= 1
            elif entry != './':
                depth += 1
        return depth
