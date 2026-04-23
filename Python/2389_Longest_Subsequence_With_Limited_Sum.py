import bisect
from itertools import accumulate

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        prefix = list(accumulate(sorted(nums)))
        return [bisect.bisect_right(prefix, q) for q in queries]
