# Author: Kaustav Ghosh
# Problem: Longest Cycle in a Graph
# Approach: Every node has at most one outgoing edge, so each walk either runs off the graph or closes into a cycle. Walk from every unvisited node stamping each node with a global clock; if the walk reaches a node stamped during this same walk, the difference between the current clock and that stamp is the cycle's length

class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        visit_time = [0] * len(edges)
        best = -1
        clock = 1
        for start in range(len(edges)):
            if visit_time[start]:
                continue
            start_clock = clock
            node = start
            while node != -1 and visit_time[node] == 0:
                visit_time[node] = clock
                clock += 1
                node = edges[node]
            if node != -1 and visit_time[node] >= start_clock:
                best = max(best, clock - visit_time[node])
        return best
