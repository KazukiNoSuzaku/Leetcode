# Author: Kaustav Ghosh
# 1105. Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            width = 0
            height = 0
            for j in range(i, 0, -1):
                w, h = books[j-1]
                width += w
                if width > shelfWidth:
                    break
                height = max(height, h)
                dp[i] = min(dp[i], dp[j-1] + height)
        return dp[n]
