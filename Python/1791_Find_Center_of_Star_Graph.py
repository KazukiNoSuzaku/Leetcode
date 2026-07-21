# Author: Kaustav Ghosh
# Problem: Find Center of Star Graph
# Approach: The center touches every edge, so it is the node shared by the first two edges

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a, b = edges[0]
        c, d = edges[1]
        return a if a in (c, d) else b
