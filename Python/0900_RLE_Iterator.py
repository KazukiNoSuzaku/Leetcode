# Iterate through run-length encoded sequence with next(n) advancing n elements.

# Author: Kaustav Ghosh

class RLEIterator(object):
    def __init__(self, encoding):
        self.enc = encoding
        self.idx = 0

    def next(self, n):
        while self.idx < len(self.enc):
            if self.enc[self.idx] >= n:
                self.enc[self.idx] -= n
                return self.enc[self.idx + 1]
            n -= self.enc[self.idx]
            self.idx += 2
        return -1
