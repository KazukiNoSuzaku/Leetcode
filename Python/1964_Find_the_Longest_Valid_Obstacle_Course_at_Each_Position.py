# Author: Kaustav Ghosh
# Problem: Find the Longest Valid Obstacle Course at Each Position
# Approach: A valid course ending at position i is a non-decreasing subsequence that must include obstacles[i], so each answer is the length of the longest non-decreasing subsequence ending there. I keep the usual patience-sorting array where entry j holds the smallest possible last obstacle of a non-decreasing subsequence of length j + 1, which stays sorted, so each new obstacle is placed by binary search. Because the subsequence may repeat equal heights, the search has to land after any equal entries rather than before them, which is what bisect_right gives; the found index is then the answer for this position, and the entry there is overwritten or appended. One binary search per obstacle makes this O(n log n).

from bisect import bisect_right

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        tails = []
        answers = []
        for height in obstacles:
            spot = bisect_right(tails, height)
            if spot == len(tails):
                tails.append(height)
            else:
                tails[spot] = height
            answers.append(spot + 1)
        return answers
