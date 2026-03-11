# Split a digit string into a Fibonacci-like sequence.

# Author: Kaustav Ghosh

class Solution(object):
    def splitIntoFibonacci(self, num):
        n = len(num)
        def backtrack(idx, seq):
            if idx == n and len(seq) >= 3: return seq
            for end in range(idx + 1, n + 1):
                part = num[idx:end]
                if len(part) > 1 and part[0] == '0': break
                val = int(part)
                if val > 2**31 - 1: break
                if len(seq) >= 2 and val != seq[-1] + seq[-2]: continue
                res = backtrack(end, seq + [val])
                if res: return res
            return []
        return backtrack(0, [])
