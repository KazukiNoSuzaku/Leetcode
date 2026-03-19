# Author: Kaustav Ghosh
# https://leetcode.com/problems/fancy-sequence/

class Fancy(object):
    def __init__(self):
        self.vals = []
        self.add_val = 0
        self.mul_val = 1
        self.MOD = 10 ** 9 + 7
        self.inv_muls = []
        self.adds = []
        self.muls = []

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.vals.append(val)
        self.adds.append(self.add_val)
        self.muls.append(self.mul_val)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.add_val = (self.add_val + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.add_val = self.add_val * m % self.MOD
        self.mul_val = self.mul_val * m % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.vals):
            return -1
        m = self.mul_val * pow(self.muls[idx], self.MOD - 2, self.MOD) % self.MOD
        a = (self.add_val - self.adds[idx] * m) % self.MOD
        return (self.vals[idx] * m + a) % self.MOD
