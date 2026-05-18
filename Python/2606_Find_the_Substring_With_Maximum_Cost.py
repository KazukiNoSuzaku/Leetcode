class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        val_map = {c: v for c, v in zip(chars, vals)}

        def cost(c):
            return val_map.get(c, ord(c) - ord('a') + 1)

        max_sum = curr = 0
        for c in s:
            curr = max(0, curr + cost(c))
            max_sum = max(max_sum, curr)
        return max_sum
