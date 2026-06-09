from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        prefix = [0] * n
        suffix = [0] * n
        stack = []

        for i in range(n):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                j = stack[-1]
                prefix[i] = prefix[j] + maxHeights[i] * (i - j)
            else:
                prefix[i] = maxHeights[i] * (i + 1)
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                j = stack[-1]
                suffix[i] = suffix[j] + maxHeights[i] * (j - i)
            else:
                suffix[i] = maxHeights[i] * (n - i)
            stack.append(i)

        return max(prefix[i] + suffix[i] - maxHeights[i] for i in range(n))
