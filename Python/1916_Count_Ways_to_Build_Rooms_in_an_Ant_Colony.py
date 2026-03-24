# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

from collections import defaultdict

class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(prevRoom)
        children = defaultdict(list)
        for i in range(1, n):
            children[prevRoom[i]].append(i)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        size = [0] * n
        ans = [1] * n

        # Iterative post-order traversal
        import sys
        sys.setrecursionlimit(200000)
        stack = [(0, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                size[node] = 1
                for c in children[node]:
                    ans[node] = ans[node] * ans[c] % MOD
                    ans[node] = ans[node] * inv_fact[size[c]] % MOD
                    size[node] += size[c]
                ans[node] = ans[node] * fact[size[node] - 1] % MOD
            else:
                stack.append((node, True))
                for c in children[node]:
                    stack.append((c, False))

        return ans[0]
