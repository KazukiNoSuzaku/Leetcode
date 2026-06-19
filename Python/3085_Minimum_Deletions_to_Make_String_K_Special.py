from collections import Counter
import bisect

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())
        n = len(freq)
        # suffix_sum[i] = sum of freq[i:]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + freq[i]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + freq[i]

        ans = float('inf')
        for i in range(n):
            min_f = freq[i]
            cap = min_f + k
            # Delete all chars with freq < min_f
            cost = prefix_sum[i]
            # Cap chars with freq > cap down to cap
            j = bisect.bisect_right(freq, cap)
            cost += suffix_sum[j] - (n - j) * cap
            ans = min(ans, cost)
        return ans
