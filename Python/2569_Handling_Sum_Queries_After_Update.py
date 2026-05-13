class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        # Segment tree with lazy flip on nums1; type-2 queries add count_ones * p to running sum.
        n = len(nums1)
        tree = [0] * (4 * n)
        lazy = [False] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = nums1[l]
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

        def push_down(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                for child, length in [(2 * node, mid - l + 1), (2 * node + 1, r - mid)]:
                    tree[child] = length - tree[child]
                    lazy[child] = not lazy[child]
                lazy[node] = False

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                tree[node] = (r - l + 1) - tree[node]
                lazy[node] = not lazy[node]
                return
            push_down(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(2 * node, l, mid, ql, qr)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

        build(1, 0, n - 1)
        total = sum(nums2)
        result = []
        for t, a, b in queries:
            if t == 1:
                update(1, 0, n - 1, a, b)
            elif t == 2:
                total += a * tree[1]
            else:
                result.append(total)
        return result
