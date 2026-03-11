# Design and implement a data structure for a compressed string iterator. The given compressed
# string will be in the form of each letter followed by a positive integer (its count).

# Author: Kaustav Ghosh

class StringIterator(object):
    def __init__(self, compressedString):
        self.tokens = []
        i = 0
        while i < len(compressedString):
            ch = compressedString[i]
            i += 1
            num = 0
            while i < len(compressedString) and compressedString[i].isdigit():
                num = num * 10 + int(compressedString[i])
                i += 1
            self.tokens.append([ch, num])
        self.idx = 0

    def next(self):
        if not self.hasNext(): return ' '
        ch, count = self.tokens[self.idx]
        self.tokens[self.idx][1] -= 1
        if self.tokens[self.idx][1] == 0: self.idx += 1
        return ch

    def hasNext(self):
        return self.idx < len(self.tokens)
