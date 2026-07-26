# Author: Kaustav Ghosh
# Problem: Closest Room
# Approach: Answer queries offline in decreasing minSize order, inserting rooms (also sorted by size descending) into a sorted id list once they qualify; each query binary-searches that list for the id closest to the preferred one

from bisect import insort, bisect_left

class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rooms.sort(key=lambda r: r[1], reverse=True)  # by size desc
        order = sorted(range(len(queries)), key=lambda i: queries[i][1], reverse=True)

        answer = [-1] * len(queries)
        ids = []  # sorted room ids currently large enough
        r = 0
        for qi in order:
            pref, min_size = queries[qi]
            while r < len(rooms) and rooms[r][1] >= min_size:
                insort(ids, rooms[r][0])
                r += 1
            if not ids:
                continue
            pos = bisect_left(ids, pref)
            best = -1
            best_diff = float('inf')
            for p in (pos, pos - 1):
                if 0 <= p < len(ids):
                    diff = abs(ids[p] - pref)
                    if diff < best_diff or (diff == best_diff and ids[p] < best):
                        best_diff = diff
                        best = ids[p]
            answer[qi] = best
        return answer
