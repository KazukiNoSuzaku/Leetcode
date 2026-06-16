from typing import List
import bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp_search(pat: str, text: str) -> List[int]:
            if not pat:
                return []
            lps = [0] * len(pat)
            length = 0
            i = 1
            while i < len(pat):
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

            res = []
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pat[j]:
                    j = lps[j - 1]
                if text[i] == pat[j]:
                    j += 1
                if j == len(pat):
                    res.append(i - j + 1)
                    j = lps[j - 1]
            return res

        a_idx = kmp_search(a, s)
        b_idx = kmp_search(b, s)

        result = []
        for i in a_idx:
            pos = bisect.bisect_left(b_idx, i - k)
            if pos < len(b_idx) and b_idx[pos] <= i + k:
                result.append(i)
        return result
