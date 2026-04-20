class Solution:
    def maximumBooks(self, books: list[int]) -> int:
        n = len(books)
        # dp[i] = max books taking shelf i as rightmost
        dp = [0] * n
        stack = []  # monotonic stack of indices

        def triangle(lo, hi):
            # sum of consecutive integers ending at hi, starting from lo
            count = hi - lo + 1
            return count * (lo + hi) // 2

        for i in range(n):
            # books must be strictly increasing ending at books[i]
            # we can take at most books[i], books[i]-1, ... from the right
            while stack and books[stack[-1]] >= books[i] - (i - stack[-1]):
                stack.pop()
            if stack:
                j = stack[-1]
                lo = books[i] - (i - j) + 1
                dp[i] = dp[j] + triangle(lo, books[i])
            else:
                lo = max(1, books[i] - i)
                dp[i] = triangle(lo, books[i])
            stack.append(i)

        return max(dp)
