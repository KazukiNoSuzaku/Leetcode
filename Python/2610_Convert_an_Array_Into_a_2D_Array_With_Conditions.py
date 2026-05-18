from collections import Counter

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = []
        freq: Counter = Counter()
        for x in nums:
            row = freq[x]
            if row == len(result):
                result.append([])
            result[row].append(x)
            freq[x] += 1
        return result
