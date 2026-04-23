from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = Counter(num)
        half = []
        for d in '9876543210':
            half.append(d * (freq[d] // 2))
        middle = max((d for d in freq if freq[d] % 2), default='')
        half_str = ''.join(half).lstrip('0') or ''
        if not half_str:
            return middle or '0'
        return half_str + middle + half_str[::-1]
