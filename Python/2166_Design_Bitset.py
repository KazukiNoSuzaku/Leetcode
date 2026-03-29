# Author: Kaustav Ghosh
# Problem: 2166. Design Bitset
# URL: https://leetcode.com/problems/design-bitset/
# Difficulty: Medium
# Note: Premium problem

# Approach:
# Maintain the bitset as a list and a complement list (flipped version).
# Track a flipped flag to toggle between the two views in O(1).
# count() tracks the number of set bits, adjusted on fix/unfix/flip.

class Bitset(object):
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.bits = [0] * size
        self.flipped = [1] * size
        self.cnt = 0
        self.is_flipped = False

    def fix(self, idx):
        """
        :type idx: int
        """
        arr = self.flipped if self.is_flipped else self.bits
        if arr[idx] == 0:
            arr[idx] = 1
            self.cnt += 1

    def unfix(self, idx):
        """
        :type idx: int
        """
        arr = self.flipped if self.is_flipped else self.bits
        if arr[idx] == 1:
            arr[idx] = 0
            self.cnt -= 1

    def flip(self):
        self.is_flipped = not self.is_flipped
        self.cnt = self.size - self.cnt

    def all(self):
        """
        :rtype: bool
        """
        return self.cnt == self.size

    def one(self):
        """
        :rtype: bool
        """
        return self.cnt > 0

    def count(self):
        """
        :rtype: int
        """
        return self.cnt

    def toString(self):
        """
        :rtype: str
        """
        arr = self.flipped if self.is_flipped else self.bits
        return ''.join(map(str, arr))


class Solution(object):
    pass
