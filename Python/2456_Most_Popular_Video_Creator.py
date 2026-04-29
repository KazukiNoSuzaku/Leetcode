from collections import defaultdict

class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        total = defaultdict(int)
        best = {}  # creator -> (max_views, best_id)

        for c, vid, v in zip(creators, ids, views):
            total[c] += v
            if c not in best or v > best[c][0] or (v == best[c][0] and vid < best[c][1]):
                best[c] = (v, vid)

        max_total = max(total.values())
        return [[c, best[c][1]] for c, t in total.items() if t == max_total]
