# Author: Kaustav Ghosh
# Problem: Stone Game V
# Approach: Interval DP where dp[i][j] is Alice's best total from the stones i..j, but the naive version tries every split point and costs O(n^3), so I exploit that the sums grow monotonically with the split: there is a single pivot where the left half stops being lighter than the right. Left of the pivot Alice always keeps the left half, right of it she always keeps the right half, so running prefix maxima of sum + dp over each row and suffix maxima over each column let me read off the best choice on either side of the pivot in constant time, leaving only the pivot itself (the one split that can tie) to be checked by hand.

from bisect import bisect_left


class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i, value in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + value

        dp = [[0] * n for _ in range(n)]
        # best_left[i][j]  = max over k in [i, j] of sum(i..k) + dp[i][k]
        # best_right[i][j] = max over t in [i, j] of sum(t..j) + dp[t][j]
        best_left = [[0] * n for _ in range(n)]
        best_right = [[0] * n for _ in range(n)]
        for i in range(n):
            best_left[i][i] = best_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                # Smallest split k whose left half is at least half of the row.
                pivot = bisect_left(prefix, prefix[i] + (total + 1) // 2, i + 1, j + 1) - 1
                if pivot < i:
                    pivot = j
                best = 0
                if pivot > i:
                    # Every split before the pivot leaves the left half lighter.
                    best = best_left[i][pivot - 1]
                if pivot <= j - 1:
                    left = prefix[pivot + 1] - prefix[i]
                    right = total - left
                    if left == right:
                        tie = left + max(dp[i][pivot], dp[pivot + 1][j])
                        if tie > best:
                            best = tie
                    else:
                        heavier = right + dp[pivot + 1][j]
                        if heavier > best:
                            best = heavier
                    if pivot + 2 <= j and best_right[pivot + 2][j] > best:
                        best = best_right[pivot + 2][j]
                dp[i][j] = best
                row = total + best
                best_left[i][j] = row if row > best_left[i][j - 1] else best_left[i][j - 1]
                best_right[i][j] = row if row > best_right[i + 1][j] else best_right[i + 1][j]

        return dp[0][n - 1]
