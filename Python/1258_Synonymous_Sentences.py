# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Union-Find for synonyms, generate all combinations

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        from collections import defaultdict

        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for a, b in synonyms:
            union(a, b)

        groups = defaultdict(set)
        for word in parent:
            groups[find(word)].add(word)

        words = text.split()
        results = [[]]
        for word in words:
            root = find(word) if word in parent else word
            options = sorted(groups[root]) if root in groups else [word]
            new_results = []
            for sentence in results:
                for option in options:
                    new_results.append(sentence + [option])
            results = new_results

        return sorted(' '.join(s) for s in results)
