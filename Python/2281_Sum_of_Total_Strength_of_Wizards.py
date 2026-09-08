# Author: Kaustav Ghosh
# Problem: Sum of Total Strength of Wizards
# Approach: For each element as the minimum of a subarray, a monotonic stack gives the span (prev strictly-smaller, next smaller-or-equal) over which it is the minimum. Within that span the contribution is strength[i] times the sum over all subarrays containing i of their element sums. Using prefix-of-prefix sums, that inner quantity has a closed form: (right side prefix mass)*(left count) - (left side prefix mass)*(right count). Accumulate modulo 1e9+7

class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(strength)

        # prefix[i] = sum of strength[0..i-1]; then prefix-of-prefix ss
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + strength[i]
        ss = [0] * (n + 2)  # ss[i] = sum of prefix[0..i-1]
        for i in range(n + 1):
            ss[i + 1] = ss[i] + prefix[i]

        # previous strictly smaller (left boundary), next smaller-or-equal (right)
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        total = 0
        for i in range(n):
            l, r = left[i], right[i]
            # subarrays where i is the min: start in (l, i], end in [i, r)
            # sum over such subarrays of (subarray sum) using ss
            left_count = i - l
            right_count = r - i
            # positive part: prefix sums at ends [i+1 .. r] weighted by left_count
            pos = (ss[r + 1] - ss[i + 1]) * left_count
            neg = (ss[i + 1] - ss[l + 1]) * right_count
            total = (total + strength[i] * (pos - neg)) % MOD
        return total % MOD
