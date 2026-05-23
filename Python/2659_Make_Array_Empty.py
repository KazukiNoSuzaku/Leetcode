class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        n = len(nums)
        order = sorted(range(n), key=lambda i: (nums[i], i))

        bit = [0] * (n + 1)

        def update(i, v):
            i += 1
            while i <= n:
                bit[i] += v
                i += i & -i

        def prefix(i):
            if i < 0:
                return 0
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in range(n):
            update(i, 1)

        ans = 0
        ptr = 0
        for pos in order:
            if pos >= ptr:
                ans += prefix(pos) - prefix(ptr - 1)
            else:
                ans += prefix(n - 1) - prefix(ptr - 1) + prefix(pos)
            update(pos, -1)
            ptr = (pos + 1) % n
        return ans
