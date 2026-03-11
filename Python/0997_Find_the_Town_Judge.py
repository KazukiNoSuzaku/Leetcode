# The town judge trusts nobody and is trusted by everyone else.
# Find the judge or return -1.

# Author: Kaustav Ghosh

class Solution(object):
    def findJudge(self, n, trust):
        trust_count = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        for a, b in trust:
            trust_count[a] += 1
            trusted_by[b] += 1
        for i in range(1, n + 1):
            if trust_count[i] == 0 and trusted_by[i] == n - 1:
                return i
        return -1
