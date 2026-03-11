# Determine if two sentences are similar given transitive similar word pairs.

# Author: Kaustav Ghosh

class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2): return False
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        for a, b in similarPairs:
            parent[find(a)] = find(b)
        return all(find(w1) == find(w2) for w1, w2 in zip(sentence1, sentence2))
