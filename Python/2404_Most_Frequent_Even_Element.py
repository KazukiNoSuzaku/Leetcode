from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq = Counter(x for x in nums if x % 2 == 0)
        if not freq:
            return -1
        return min(freq, key=lambda x: (-freq[x], x))
