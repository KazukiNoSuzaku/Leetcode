# Author: Kaustav Ghosh
# Problem: Longest Substring of One Repeating Character
# Approach: A segment tree over the string where each node stores the longest single-character run inside its range, plus the run lengths touching its left and right ends and the boundary characters. Merging two children combines their runs when the touching boundary characters match. Each query is a point update followed by reading the root's best run

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        arr = list(s)
        size = 1
        while size < n:
            size <<= 1

        # node stored as [pref, suf, best, lchar, rchar, length]
        pref = [0] * (2 * size)
        suf = [0] * (2 * size)
        best = [0] * (2 * size)
        lch = [''] * (2 * size)
        rch = [''] * (2 * size)
        length = [0] * (2 * size)

        def pull(i):
            l, r = 2 * i, 2 * i + 1
            if length[l] == 0:
                pref[i], suf[i], best[i] = pref[r], suf[r], best[r]
                lch[i], rch[i], length[i] = lch[r], rch[r], length[r]
                return
            if length[r] == 0:
                pref[i], suf[i], best[i] = pref[l], suf[l], best[l]
                lch[i], rch[i], length[i] = lch[l], rch[l], length[l]
                return
            length[i] = length[l] + length[r]
            lch[i] = lch[l]
            rch[i] = rch[r]
            joined = rch[l] == lch[r]
            pref[i] = pref[l] + (pref[r] if pref[l] == length[l] and joined else 0)
            suf[i] = suf[r] + (suf[l] if suf[r] == length[r] and joined else 0)
            best[i] = max(best[l], best[r])
            if joined:
                best[i] = max(best[i], suf[l] + pref[r])

        # build leaves
        for idx in range(n):
            node = size + idx
            pref[node] = suf[node] = best[node] = length[node] = 1
            lch[node] = rch[node] = arr[idx]
        for i in range(size - 1, 0, -1):
            pull(i)

        def update(idx, ch):
            node = size + idx
            lch[node] = rch[node] = ch
            node >>= 1
            while node:
                pull(node)
                node >>= 1

        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(idx, ch)
            res.append(best[1])
        return res
