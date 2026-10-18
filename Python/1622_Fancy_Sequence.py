# Author: Kaustav Ghosh
# Problem: Fancy Sequence
# Approach: Touching every element on each addAll or multAll would be quadratic, so instead I keep one affine transform, a multiplier and an offset, that is understood to apply to the whole sequence; the two bulk operations just update that pair in constant time. The catch is append, since a value arriving later must not pick up the transform that was already in force, so it is stored pre-divided by the current multiplier and pre-shifted by the current offset, which makes the stored form transform-invariant. Dividing is multiplying by the modular inverse, and the multiplier is never zero because every multiplier given is at least one, so the inverse always exists; it is recomputed only when the multiplier actually changes rather than on every append.

class Fancy(object):
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.stored = []
        self.multiplier = 1
        self.offset = 0
        self.inverse = 1
        self.inverse_valid = True

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.inverse_valid:
            self.inverse = pow(self.multiplier, self.MOD - 2, self.MOD)
            self.inverse_valid = True
        self.stored.append((val - self.offset) * self.inverse % self.MOD)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.offset = (self.offset + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.multiplier = self.multiplier * m % self.MOD
        self.offset = self.offset * m % self.MOD
        self.inverse_valid = False

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.stored):
            return -1
        return (self.stored[idx] * self.multiplier + self.offset) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
