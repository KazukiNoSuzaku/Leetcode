# Author: Kaustav Ghosh
# Problem: 2286. Booking Concert Tickets in Groups
# URL: https://leetcode.com/problems/booking-concert-tickets-in-groups/
# Difficulty: Hard
#
# Approach:
# Segment tree with each node storing max available seats in range and total
# available seats in range. For gather: find first row with enough seats.
# For scatter: check if total available >= k, then greedily fill rows.

class BookMyShow(object):

    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """
        self.n = n
        self.m = m
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.max_tree = [m] * (2 * self.size)
        self.sum_tree = [m] * (2 * self.size)
        # Initialize internal nodes
        for i in range(self.size - 1, 0, -1):
            left_idx = 2 * i
            right_idx = 2 * i + 1
            if left_idx < 2 * self.size:
                l_max = self.max_tree[left_idx] if left_idx - self.size < n else 0
                r_max = self.max_tree[right_idx] if right_idx - self.size < n else 0
                l_sum = self.sum_tree[left_idx] if left_idx - self.size < n else 0
                r_sum = self.sum_tree[right_idx] if right_idx - self.size < n else 0
            else:
                l_max = r_max = l_sum = r_sum = 0
            self.max_tree[i] = max(l_max, r_max)
            self.sum_tree[i] = l_sum + r_sum
        # Fix: properly initialize
        # Reset and rebuild
        self.max_tree = [0] * (2 * self.size)
        self.sum_tree = [0] * (2 * self.size)
        for i in range(n):
            self.max_tree[self.size + i] = m
            self.sum_tree[self.size + i] = m
        for i in range(self.size - 1, 0, -1):
            self.max_tree[i] = max(self.max_tree[2 * i], self.max_tree[2 * i + 1])
            self.sum_tree[i] = self.sum_tree[2 * i] + self.sum_tree[2 * i + 1]

    def _update(self, pos, val):
        pos += self.size
        self.max_tree[pos] = val
        self.sum_tree[pos] = val
        pos //= 2
        while pos >= 1:
            self.max_tree[pos] = max(self.max_tree[2 * pos], self.max_tree[2 * pos + 1])
            self.sum_tree[pos] = self.sum_tree[2 * pos] + self.sum_tree[2 * pos + 1]
            pos //= 2

    def _query_first(self, node, lo, hi, maxRow, k):
        if lo > maxRow or self.max_tree[node] < k:
            return -1
        if lo == hi:
            return lo
        mid = (lo + hi) // 2
        left = self._query_first(2 * node, lo, mid, maxRow, k)
        if left != -1:
            return left
        return self._query_first(2 * node + 1, mid + 1, hi, maxRow, k)

    def _query_sum(self, node, lo, hi, ql, qr):
        if ql > hi or qr < lo:
            return 0
        if ql <= lo and hi <= qr:
            return self.sum_tree[node]
        mid = (lo + hi) // 2
        return (self._query_sum(2 * node, lo, mid, ql, qr) +
                self._query_sum(2 * node + 1, mid + 1, hi, ql, qr))

    def gather(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: List[int]
        """
        row = self._query_first(1, 0, self.size - 1, maxRow, k)
        if row == -1:
            return []
        seat = self.m - self.max_tree[self.size + row]
        self._update(row, self.max_tree[self.size + row] - k)
        return [row, seat]

    def scatter(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: bool
        """
        total = self._query_sum(1, 0, self.size - 1, 0, maxRow)
        if total < k:
            return False
        # Find first row with available seats
        row = self._query_first(1, 0, self.size - 1, maxRow, 1)
        while k > 0:
            avail = self.max_tree[self.size + row]
            take = min(avail, k)
            self._update(row, avail - take)
            k -= take
            row += 1
        return True
