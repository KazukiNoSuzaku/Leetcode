# Author: Kaustav Ghosh
# Problem: Design Bitset
# Approach: Store bits alongside a flip flag so flip() is O(1) (toggle the flag, complement the count). The actual bit is stored XOR flag. Maintain a running count of set bits for all/one/count in O(1)

class Bitset(object):
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.bits = [0] * size
        self.flip_flag = 0
        self.cnt = 0

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.bits[idx] ^ self.flip_flag == 0:
            self.bits[idx] = 1 ^ self.flip_flag
            self.cnt += 1

    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if self.bits[idx] ^ self.flip_flag == 1:
            self.bits[idx] = 0 ^ self.flip_flag
            self.cnt -= 1

    def flip(self):
        """
        :rtype: None
        """
        self.flip_flag ^= 1
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
        return ''.join(str(b ^ self.flip_flag) for b in self.bits)
