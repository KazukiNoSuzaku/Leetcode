# Author: Kaustav Ghosh
# Problem: Most Popular Video Creator
# Approach: One pass accumulates each creator's total views and tracks their best single video, keeping the lexicographically smaller id when two of their videos tie on views. The answer lists every creator whose total matches the highest total, paired with that best video

class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        totals = {}
        best_video = {}
        for creator, video, count in zip(creators, ids, views):
            totals[creator] = totals.get(creator, 0) + count
            current = best_video.get(creator)
            if current is None or count > current[0] or (count == current[0] and video < current[1]):
                best_video[creator] = (count, video)
        highest = max(totals.values())
        return [[creator, best_video[creator][1]]
                for creator, total in totals.items() if total == highest]
