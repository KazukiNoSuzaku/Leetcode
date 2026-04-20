class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        def get_dist(start):
            dist = {}
            d = 0
            while start != -1 and start not in dist:
                dist[start] = d
                start = edges[start]
                d += 1
            return dist

        d1, d2 = get_dist(node1), get_dist(node2)
        ans, best = -1, float('inf')
        for node in range(len(edges)):
            if node in d1 and node in d2:
                val = max(d1[node], d2[node])
                if val < best:
                    best, ans = val, node
        return ans
