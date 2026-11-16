# Author: Kaustav Ghosh
# Problem: Painting a Grid With Three Different Colors
# Approach: A column is painted independently of every column but the one before it, so the whole grid is a walk through the set of legal columns. With m at most five there are only 3 * 2^(m-1) = 48 columns whose vertically adjacent cells differ, so I enumerate those by extending partial columns one row at a time, then precompute for every column the list of columns that may follow it, which is simply those sharing no colour in any row. Counting the walks of length n is then a plain dynamic program over columns: start with one way to use each legal column, and repeatedly replace each count by the sum of the counts of its predecessors. That is O(n * 48^2) in the worst case, and each row of the table is taken modulo 10^9 + 7.

class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        columns = [()]
        for _ in range(m):
            grown = []
            for column in columns:
                for colour in range(3):
                    if not column or column[-1] != colour:
                        grown.append(column + (colour,))
            columns = grown

        total = len(columns)
        followers = []
        for first in columns:
            allowed = []
            for index, second in enumerate(columns):
                if all(a != b for a, b in zip(first, second)):
                    allowed.append(index)
            followers.append(allowed)

        ways = [1] * total
        for _ in range(n - 1):
            nxt = [0] * total
            for index in range(total):
                count = ways[index]
                if count:
                    for follower in followers[index]:
                        nxt[follower] = (nxt[follower] + count) % MOD
            ways = nxt

        return sum(ways) % MOD
