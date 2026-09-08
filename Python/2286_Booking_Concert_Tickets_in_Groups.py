# Author: Kaustav Ghosh
# Problem: Booking Concert Tickets in Groups
# Approach: Keep a segment tree over rows storing, per row, the number of available seats, maintaining both the subtree maximum (for gather: find the leftmost row with enough contiguous free seats) and the subtree sum (for scatter: check total availability, then fill seats row by row from the first available row). Point updates keep both aggregates in sync

class BookMyShow(object):
    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """
        self.n = n
        self.m = m
        self.avail = [m] * n          # seats still free in each row
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.tmax = [0] * (2 * size)
        self.tsum = [0] * (2 * size)
        for i in range(n):
            self.tmax[size + i] = m
            self.tsum[size + i] = m
        for i in range(size - 1, 0, -1):
            self.tmax[i] = max(self.tmax[2 * i], self.tmax[2 * i + 1])
            self.tsum[i] = self.tsum[2 * i] + self.tsum[2 * i + 1]

    def _update(self, idx, value):
        node = self.size + idx
        self.tmax[node] = value
        self.tsum[node] = value
        node >>= 1
        while node:
            self.tmax[node] = max(self.tmax[2 * node], self.tmax[2 * node + 1])
            self.tsum[node] = self.tsum[2 * node] + self.tsum[2 * node + 1]
            node >>= 1

    def _first_with_at_least(self, k, maxRow):
        # leftmost index in [0, maxRow] whose avail >= k, else -1
        if self.tmax[1] < k:
            pass  # global check not sufficient because of maxRow; do guided descent
        node = 1
        lo, hi = 0, self.size - 1
        if self.tmax[node] < k:
            return -1

        def descend(node, lo, hi):
            if lo > maxRow or self.tmax[node] < k:
                return -1
            if lo == hi:
                return lo if lo <= maxRow else -1
            mid = (lo + hi) // 2
            res = descend(2 * node, lo, mid)
            if res != -1:
                return res
            return descend(2 * node + 1, mid + 1, hi)

        return descend(1, 0, self.size - 1)

    def _sum_prefix(self, maxRow):
        # sum of avail over [0, maxRow]
        l, r = self.size + 0, self.size + maxRow
        res = 0
        l_bound, r_bound = l, r + 1
        while l_bound < r_bound:
            if l_bound & 1:
                res += self.tsum[l_bound]
                l_bound += 1
            if r_bound & 1:
                r_bound -= 1
                res += self.tsum[r_bound]
            l_bound >>= 1
            r_bound >>= 1
        return res

    def gather(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: List[int]
        """
        row = self._first_with_at_least(k, maxRow)
        if row == -1:
            return []
        used_before = self.m - self.avail[row]
        self.avail[row] -= k
        self._update(row, self.avail[row])
        return [row, used_before]

    def scatter(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: bool
        """
        if self._sum_prefix(maxRow) < k:
            return False
        remaining = k
        while remaining > 0:
            row = self._first_with_at_least(1, maxRow)
            take = min(self.avail[row], remaining)
            self.avail[row] -= take
            self._update(row, self.avail[row])
            remaining -= take
        return True
