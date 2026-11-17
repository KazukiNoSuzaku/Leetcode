# Author: Kaustav Ghosh
# Problem: Describe the Painting
# Approach: The mixture only ever changes at a segment's start or end, so between two consecutive such coordinates the set of overlapping colours, and therefore the sum, is constant. I accumulate a difference map keyed by coordinate, adding a colour at its start and subtracting it at its end, then sweep the coordinates in sorted order carrying a running sum. Each adjacent pair of coordinates with a positive running sum becomes one output piece. Painted stretches that happen to share the same sum but are made of different colours stay separate pieces, which is what the problem's third example requires, so no merging of equal sums is done. Sorting the at most 2 * 10^4 distinct coordinates dominates.

class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        delta = {}
        for start, end, colour in segments:
            delta[start] = delta.get(start, 0) + colour
            delta[end] = delta.get(end, 0) - colour

        marks = sorted(delta)
        pieces = []
        running = 0
        for index in range(len(marks) - 1):
            running += delta[marks[index]]
            if running > 0:
                pieces.append([marks[index], marks[index + 1], running])
        return pieces
