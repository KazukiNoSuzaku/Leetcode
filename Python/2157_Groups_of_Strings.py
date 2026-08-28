# Author: Kaustav Ghosh
# Problem: Groups of Strings
# Approach: Represent each word by its 26-bit letter set. Two words connect if their sets are equal, differ by one added/removed letter, or by one replaced letter. Union masks over delete-edges (which also cover adds from the larger side) and replace-edges; then count components and the largest by total word multiplicity

from collections import Counter

class Solution(object):
    def groupStrings(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        def to_mask(w):
            m = 0
            for c in w:
                m |= 1 << (ord(c) - 97)
            return m

        counts = Counter(to_mask(w) for w in words)
        parent = {m: m for m in counts}
        size = dict(counts)          # component word count keyed by root
        self_groups = [len(counts)]  # number of components

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            parent[ra] = rb
            size[rb] += size[ra]
            self_groups[0] -= 1

        for m in counts:
            # delete a letter (also covers add from the larger mask's side)
            for i in range(26):
                if m >> i & 1:
                    nb = m ^ (1 << i)
                    if nb in counts:
                        union(m, nb)
            # replace a letter
            for i in range(26):
                if m >> i & 1:
                    for j in range(26):
                        if not (m >> j & 1):
                            nb = (m ^ (1 << i)) | (1 << j)
                            if nb in counts:
                                union(m, nb)

        largest = max(size[find(m)] for m in counts)
        return [self_groups[0], largest]
