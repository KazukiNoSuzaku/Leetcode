# Author: Kaustav Ghosh
# Problem: Sequentially Ordinal Rank Tracker
# Approach: Keep two heaps. `left` holds the already-returned top items, worst-first; `right` holds the remaining candidates, best-first (higher score, then lexicographically smaller name). get() moves the best candidate into left and returns it; add() pushes to right and, if the new best now beats the worst returned, swaps them so left stays the exact top-k

import heapq

class _Rev(object):
    # wrapper so a min-heap surfaces the lexicographically LARGER name first
    __slots__ = ('s',)

    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        return self.s > other.s

    def __eq__(self, other):
        return self.s == other.s


class SORTracker(object):
    def __init__(self):
        self.left = []   # min-heap of (score, _Rev(name)): top = worst returned
        self.right = []  # min-heap of (-score, name): top = best candidate

    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        heapq.heappush(self.right, (-score, name))
        if self.left:
            score_l, rev_l = self.left[0]
            name_l = rev_l.s
            nsc_r, name_r = self.right[0]
            score_r = -nsc_r
            if score_r > score_l or (score_r == score_l and name_r < name_l):
                heapq.heappop(self.right)
                heapq.heappop(self.left)
                heapq.heappush(self.left, (score_r, _Rev(name_r)))
                heapq.heappush(self.right, (-score_l, name_l))

    def get(self):
        """
        :rtype: str
        """
        nsc, name = heapq.heappop(self.right)
        heapq.heappush(self.left, (-nsc, _Rev(name)))
        return name
