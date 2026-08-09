# Author: Kaustav Ghosh
# Problem: Number of Ways to Separate Numbers
# Approach: f[i][k] counts splits of num[i:] whose first chunk has length k (no leading zero). The next chunk must be at least as large: any longer chunk works, an equal-length chunk works only if it is lexicographically >=, decided in O(1) via a longest-common-prefix table. Suffix sums g[i][k] make each transition O(1)

class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(num)
        if num[0] == '0':
            return 0

        # lcp[i][j] = length of longest common prefix of num[i:] and num[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def next_ge(a, b, length):
            # is num[b:b+length] >= num[a:a+length] ?
            l = lcp[a][b]
            if l >= length:
                return True
            return num[b + l] >= num[a + l]

        # f[i][k], g[i][k] = sum_{k'>=k} f[i][k']
        f = [[0] * (n + 2) for _ in range(n + 1)]
        g = [[0] * (n + 2) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(n - i, 0, -1):
                if num[i] == '0':
                    val = 0
                elif i + k == n:
                    val = 1
                else:
                    nxt = i + k
                    val = g[nxt][k + 1]
                    if nxt + k <= n and next_ge(i, nxt, k):
                        val += f[nxt][k]
                    val %= MOD
                f[i][k] = val
                g[i][k] = (val + g[i][k + 1]) % MOD

        return g[0][1] % MOD
