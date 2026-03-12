# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Group visits by user sorted by time, find most common 3-sequence

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        from itertools import combinations

        visits = defaultdict(list)
        data = sorted(zip(timestamp, username, website))
        for t, u, w in data:
            visits[u].append(w)

        pattern_count = defaultdict(int)
        for user, sites in visits.items():
            patterns = set(combinations(sites, 3))
            for p in patterns:
                pattern_count[p] += 1

        max_count = max(pattern_count.values())
        result = min(p for p, c in pattern_count.items() if c == max_count)
        return list(result)
