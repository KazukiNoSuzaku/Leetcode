class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = []
        for c in s:
            d = ord(c) - ord('a')
            cost = min(d, 26 - d)
            if k >= cost:
                k -= cost
                res.append('a')
            else:
                res.append(chr(ord(c) - k))
                k = 0
        return ''.join(res)
