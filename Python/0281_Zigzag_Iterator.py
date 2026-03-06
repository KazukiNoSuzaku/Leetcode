# Given two vectors of integers v1 and v2, implement an iterator to return their elements
# alternately. Implement the ZigzagIterator class:
# - ZigzagIterator(List[int] v1, List[int] v2) initializes the object with the two vectors.
# - boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# - int next() returns the current element of the iterator and moves the iterator to the next element.

# Example 1:
# Input: v1 = [1,2], v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]

# Constraints:
# 0 <= v1.length, v2.length <= 1000

# Author: Kaustav Ghosh

class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.queues = [iter(v) for v in [v1, v2] if v]
        self.current = 0

    def next(self):
        val = next(self.queues[self.current])
        try:
            next_q = (self.current + 1) % len(self.queues)
            next(self.queues[next_q])
            # put it back - use a wrapper approach
        except StopIteration:
            self.queues.pop(next_q)
        # simpler approach: store as lists
        pass

# Simpler implementation:
class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.data = []
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1):
                self.data.append(v1[i]); i += 1
            if j < len(v2):
                self.data.append(v2[j]); j += 1
        self.idx = 0

    def next(self):
        val = self.data[self.idx]
        self.idx += 1
        return val

    def hasNext(self):
        return self.idx < len(self.data)
