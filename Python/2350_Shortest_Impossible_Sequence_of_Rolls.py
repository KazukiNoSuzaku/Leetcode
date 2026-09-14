# Author: Kaustav Ghosh
# Problem: Shortest Impossible Sequence of Rolls
# Approach: Greedily cut rolls into consecutive segments that each contain all k faces. With c complete segments any sequence of length c can be taken one roll per segment, while the sequence made of the face completing each segment followed by a face missing from the leftover tail cannot, so the answer is c + 1

class Solution(object):
    def shortestSequence(self, rolls, k):
        """
        :type rolls: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        segments = 0
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                segments += 1
                seen = set()
        return segments + 1
