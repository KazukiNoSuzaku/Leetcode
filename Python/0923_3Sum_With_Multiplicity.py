# Count ordered triples with i<j<k and arr[i]+arr[j]+arr[k]==target. Mod 10^9+7.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def threeSumMulti(self, arr, target):
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        res = 0
        for i, a in enumerate(keys):
            for b in keys[i:]:
                c = target - a - b
                if c < b: continue
                if c not in count: continue
                if a == b == c:
                    n = count[a]
                    res += n * (n-1) * (n-2) // 6
                elif a == b:
                    n = count[a]
                    res += n * (n-1) // 2 * count[c]
                elif b == c:
                    n = count[b]
                    res += count[a] * n * (n-1) // 2
                else:
                    res += count[a] * count[b] * count[c]
        return res % MOD
