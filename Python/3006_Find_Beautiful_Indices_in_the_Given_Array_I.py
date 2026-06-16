from typing import List
import bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def find_all(pat: str) -> List[int]:
            res = []
            start = 0
            while True:
                idx = s.find(pat, start)
                if idx == -1:
                    break
                res.append(idx)
                start = idx + 1
            return res

        a_idx = find_all(a)
        b_idx = find_all(b)

        result = []
        for i in a_idx:
            pos = bisect.bisect_left(b_idx, i - k)
            if pos < len(b_idx) and b_idx[pos] <= i + k:
                result.append(i)
        return result
