# Author: Kaustav Ghosh
# Problem: Find Center of Star Graph
# Approach: In a star every edge touches the centre, so any two edges already pin it down: the node they have in common can only be the centre, because the two leaves at their other ends are distinct. Looking at the first two edges is therefore enough and the rest of the input never has to be read.

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        first, second = edges[0], edges[1]
        return first[0] if first[0] in second else first[1]
