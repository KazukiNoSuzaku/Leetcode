from typing import List

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def get_max(excl):
            s = [(x + y, i) for i, (x, y) in enumerate(points) if i != excl]
            t = [(x - y, i) for i, (x, y) in enumerate(points) if i != excl]
            return max(max(s)[0] - min(s)[0], max(t)[0] - min(t)[0])

        s = [(x + y, i) for i, (x, y) in enumerate(points)]
        t = [(x - y, i) for i, (x, y) in enumerate(points)]
        candidates = {max(s)[1], min(s)[1], max(t)[1], min(t)[1]}
        return min(get_max(i) for i in candidates)
