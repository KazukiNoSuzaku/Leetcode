# Author: Kaustav Ghosh
# Problem: Destination City
# Approach: Find city with no outgoing edge

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = set(p[0] for p in paths)
        for p in paths:
            if p[1] not in sources:
                return p[1]
