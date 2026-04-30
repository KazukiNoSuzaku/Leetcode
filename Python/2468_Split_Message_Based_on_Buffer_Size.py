class Solution:
    def splitMessage(self, message: str, limit: int) -> list[str]:
        n = len(message)

        def digits(x):
            return len(str(x))

        def can_split(k):
            dk = digits(k)
            total_avail = 0
            # Group parts by digit length of i
            for length in range(1, dk + 1):
                lo = 10 ** (length - 1) if length > 1 else 1
                hi = min(10 ** length - 1, k)
                count = hi - lo + 1
                avail_per = limit - 3 - length - dk  # chars left after "<i/k>"
                if avail_per <= 0:
                    return False
                total_avail += count * avail_per
                if total_avail >= n:
                    return True
            return total_avail >= n

        lo, hi, k = 1, n, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                k = mid
                hi = mid - 1
            else:
                lo = mid + 1

        if k == -1:
            return []

        result, idx = [], 0
        for i in range(1, k + 1):
            suffix = f"<{i}/{k}>"
            avail = limit - len(suffix)
            result.append(message[idx:idx + avail] + suffix)
            idx += avail
        return result
