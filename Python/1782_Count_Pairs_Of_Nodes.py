# Author: Kaustav Ghosh
# Problem: Count Pairs Of Nodes
# Approach: The number of edges touching a or b is deg(a) + deg(b) minus the edges counted twice, which are exactly the ones running directly between them, so the quantity is almost a function of the two degrees alone. Sorting the degrees lets a two-pointer sweep count every pair whose degree sum exceeds the threshold in linear time, and the only pairs that estimate wrongly are those actually joined by an edge. Those are few, at most one per distinct edge, so each is revisited and dropped if subtracting its shared count pushes it back under the threshold.

class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        degree = [0] * (n + 1)
        shared = Counter()
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            shared[(u, v) if u < v else (v, u)] += 1

        ordered = sorted(degree[1:])
        answers = []
        for threshold in queries:
            count = 0
            low, high = 0, n - 1
            while low < high:
                if ordered[low] + ordered[high] > threshold:
                    count += high - low
                    high -= 1
                else:
                    low += 1
            for (u, v), together in shared.items():
                combined = degree[u] + degree[v]
                if combined > threshold and combined - together <= threshold:
                    count -= 1
            answers.append(count)
        return answers
