class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        # Segment tree for range max query on values 1..max(nums)
        m = max(nums)
        tree = [0] * (2 * m + 2)

        def update(i, val):
            i += m + 1
            tree[i] = val
            i //= 2
            while i:
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
                i //= 2

        def query(l, r):  # [l, r] inclusive, 1-indexed
            res = 0
            l += m + 1
            r += m + 2
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, tree[r])
                l //= 2
                r //= 2
            return res

        ans = 0
        for x in nums:
            best = query(max(1, x - k), x - 1) + 1 if x > 1 else 1
            ans = max(ans, best)
            if best > query(x, x):
                update(x, best)
        return ans
