# Author: Kaustav Ghosh
# Sliding window: find minimum window where chars outside have count <= n/4

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        n = len(s)
        target = n // 4
        count = Counter(s)

        if all(count[c] <= target for c in "QWER"):
            return 0

        result = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while left <= right and all(count[c] <= target for c in "QWER"):
                result = min(result, right - left + 1)
                count[s[left]] += 1
                left += 1
        return result
