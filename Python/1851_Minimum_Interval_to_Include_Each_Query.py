# Author: Kaustav Ghosh
# Problem: Minimum Interval to Include Each Query
# Approach: Answering the queries in increasing order means an interval becomes available once its left end is passed and stays relevant until its right end falls behind, so the intervals are sorted by left end and fed in as the queries advance. A heap keyed on interval size then holds the candidates, and the intervals whose right end has already been overtaken are discarded from the top as they surface; each one is discarded at most once overall. Whatever sits on top is the smallest interval still covering the query, so the answers are filled back into the original query positions at the end.

class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        from heapq import heappop, heappush

        ordered = sorted(intervals)
        asked = sorted(range(len(queries)), key=lambda j: queries[j])

        answers = [-1] * len(queries)
        candidates = []
        placed = 0
        for j in asked:
            query = queries[j]
            while placed < len(ordered) and ordered[placed][0] <= query:
                left, right = ordered[placed]
                heappush(candidates, (right - left + 1, right))
                placed += 1
            while candidates and candidates[0][1] < query:
                heappop(candidates)
            if candidates:
                answers[j] = candidates[0][0]
        return answers
