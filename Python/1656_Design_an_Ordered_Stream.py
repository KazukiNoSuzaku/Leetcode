# Author: Kaustav Ghosh
# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey] = value
        result = []
        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        return result
