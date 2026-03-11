# Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

# Author: Kaustav Ghosh

class Solution(object):
    def findKthNumber(self, n, k):
        def count_steps(prefix, n):
            cur, nxt = prefix, prefix + 1
            steps = 0
            while cur <= n:
                steps += min(n + 1, nxt) - cur
                cur *= 10
                nxt *= 10
            return steps

        cur = 1
        k -= 1
        while k > 0:
            steps = count_steps(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
