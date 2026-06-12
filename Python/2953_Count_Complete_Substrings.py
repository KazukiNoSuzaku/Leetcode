class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def count_segment(seg: str) -> int:
            n = len(seg)
            res = 0
            for m in range(1, 27):
                w = m * k
                if w > n:
                    break
                freq = [0] * 26
                exact = 0  # letters whose window count is exactly k
                for i, ch in enumerate(seg):
                    c = ord(ch) - 97
                    freq[c] += 1
                    if freq[c] == k:
                        exact += 1
                    elif freq[c] == k + 1:
                        exact -= 1
                    if i >= w:
                        d = ord(seg[i - w]) - 97
                        if freq[d] == k:
                            exact -= 1
                        freq[d] -= 1
                        if freq[d] == k:
                            exact += 1
                    # window of size m*k with m letters at count k has no others
                    if i >= w - 1 and exact == m:
                        res += 1
            return res

        ans = start = 0
        for i in range(1, len(word) + 1):
            if i == len(word) or abs(ord(word[i]) - ord(word[i - 1])) > 2:
                ans += count_segment(word[start:i])
                start = i
        return ans
