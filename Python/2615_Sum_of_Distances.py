from collections import defaultdict

class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        groups: dict[int, list[int]] = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)

        for indices in groups.values():
            m = len(indices)
            prefix = [0] * (m + 1)
            for j in range(m):
                prefix[j + 1] = prefix[j] + indices[j]
            for j in range(m):
                left = indices[j] * j - prefix[j]
                right = (prefix[m] - prefix[j + 1]) - indices[j] * (m - j - 1)
                ans[indices[j]] = left + right

        return ans
