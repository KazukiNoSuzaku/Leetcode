# Author: Kaustav Ghosh
# Problem: Design an Ordered Stream
# Approach: Store each value at its id slot; a pointer walks forward emitting the contiguous run that is now filled

class OrderedStream(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.data = [None] * (n + 1)  # 1-indexed ids
        self.ptr = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.data[idKey] = value
        chunk = []
        while self.ptr < len(self.data) and self.data[self.ptr] is not None:
            chunk.append(self.data[self.ptr])
            self.ptr += 1
        return chunk
