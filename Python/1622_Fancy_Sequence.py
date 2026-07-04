# Author: Kaustav Ghosh
# Problem: Fancy Sequence
# Approach: Keep global affine transform value = mul*x + add; store each appended element pre-normalized by the inverse transform so later ops apply lazily in O(1)

class Fancy(object):
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Undo the current transform so that mul*stored + add == val
        inv = pow(self.mul, self.MOD - 2, self.MOD)
        stored = (val - self.add) * inv % self.MOD
        self.seq.append(stored)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD
