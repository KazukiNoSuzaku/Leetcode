# Author: Kaustav Ghosh
# Problem: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
# Approach: Build the answer left to right, each time pulling forward the smallest digit still affordable. Moving a digit costs one swap per digit still standing in front of it, which is its index minus however many earlier digits have already been pulled out; a Fenwick tree over the removed positions keeps that count cheap, and a queue per digit value gives its earliest remaining position

from collections import deque


class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        positions = [deque() for _ in range(10)]
        for i, ch in enumerate(num):
            positions[int(ch)].append(i)
        tree = [0] * (n + 1)

        def mark(index):
            index += 1
            while index <= n:
                tree[index] += 1
                index += index & -index

        def removed_before(index):
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & -index
            return total

        digits = []
        for _ in range(n):
            for value in range(10):
                if positions[value]:
                    position = positions[value][0]
                    cost = position - removed_before(position)
                    if cost <= k:
                        k -= cost
                        positions[value].popleft()
                        mark(position)
                        digits.append(str(value))
                        break
        return "".join(digits)
