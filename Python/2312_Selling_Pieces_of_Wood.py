# Author: Kaustav Ghosh
# Problem: Selling Pieces of Wood
# Approach: DP over sub-board dimensions. best[h][w] is the maximum money obtainable from an h x w piece: either sell it whole (if that exact size has a price), or make one full horizontal cut (split the height) or one full vertical cut (split the width) and sum the two resulting pieces' best values. Cuts up to the halves suffice by symmetry

class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        price = {}
        for h, w, p in prices:
            price[(h, w)] = p

        best = [[0] * (n + 1) for _ in range(m + 1)]
        for h in range(1, m + 1):
            for w in range(1, n + 1):
                cur = price.get((h, w), 0)
                for i in range(1, h // 2 + 1):
                    cur = max(cur, best[i][w] + best[h - i][w])
                for j in range(1, w // 2 + 1):
                    cur = max(cur, best[h][j] + best[h][w - j])
                best[h][w] = cur
        return best[m][n]
