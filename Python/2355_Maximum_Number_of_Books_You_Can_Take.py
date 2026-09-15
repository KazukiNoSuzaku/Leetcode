# Author: Kaustav Ghosh
# Problem: Maximum Number of Books You Can Take
# Approach: If shelf i ends the chosen section and all books[i] are taken from it, the counts to the left must descend one by one. Keeping a monotonic stack of books[j] - j, the nearest j on the left with books[j] - j < books[i] - i is where that descending run must stop, so dp[i] = dp[j] + the series books[i], books[i]-1, ... over i - j shelves; with no such j the run reaches the start or runs out of books, whichever comes first

class Solution(object):
    def maximumBooks(self, books):
        """
        :type books: List[int]
        :rtype: int
        """
        def series(top, count):
            return count * top - count * (count - 1) // 2

        dp = [0] * len(books)
        stack = []
        best = 0
        for i, b in enumerate(books):
            while stack and books[stack[-1]] - stack[-1] >= b - i:
                stack.pop()
            if stack:
                j = stack[-1]
                dp[i] = dp[j] + series(b, i - j)
            else:
                dp[i] = series(b, min(i + 1, b))
            stack.append(i)
            best = max(best, dp[i])
        return best
