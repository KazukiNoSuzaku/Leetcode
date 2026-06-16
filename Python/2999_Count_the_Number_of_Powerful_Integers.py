class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(x: int) -> int:
            # Count powerful integers in [0, x]
            x_str = str(x)
            n, m = len(x_str), len(s)
            if n < m:
                return 0
            if any(int(c) > limit for c in s):
                return 0

            prefix_len = n - m
            prefix_x = x_str[:prefix_len]

            total = 0
            for i in range(prefix_len):
                d = int(prefix_x[i])
                cnt_less = min(d, limit + 1)  # digits 0..d-1 capped at limit
                total += cnt_less * (limit + 1) ** (prefix_len - i - 1)
                if d > limit:
                    return total  # can't match prefix exactly past here

            # Prefix matches x's prefix exactly; check the suffix part
            suffix_x = x_str[prefix_len:]
            if s <= suffix_x:
                total += 1
            return total

        return count(finish) - count(start - 1)
