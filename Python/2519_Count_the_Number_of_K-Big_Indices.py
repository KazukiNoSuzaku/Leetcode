class Solution:
    def kBigIndices(self, nums: list[int], k: int) -> int:
        # Premium: BIT from left and right counts strictly smaller elements; check both >= k.
        n = len(nums)
        sorted_vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_vals)}
        m = len(sorted_vals)

        class BIT:
            def __init__(self):
                self.tree = [0] * (m + 1)

            def update(self, i: int) -> None:
                while i <= m:
                    self.tree[i] += 1
                    i += i & (-i)

            def query(self, i: int) -> int:
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s

        left = [0] * n
        bit = BIT()
        for i in range(n):
            left[i] = bit.query(rank[nums[i]] - 1)
            bit.update(rank[nums[i]])

        right = [0] * n
        bit = BIT()
        for i in range(n - 1, -1, -1):
            right[i] = bit.query(rank[nums[i]] - 1)
            bit.update(rank[nums[i]])

        return sum(1 for i in range(n) if left[i] >= k and right[i] >= k)
