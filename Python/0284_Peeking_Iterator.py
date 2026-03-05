# Design an iterator that supports the peek operation on an existing iterator in addition to
# the hasNext and next operations.
# Implement the PeekingIterator class:
# - PeekingIterator(Iterator nums) Initializes the object with the given integer iterator iterator.
# - int next() Returns the next element in the array and moves the pointer to the next element.
# - boolean hasNext() Returns true if there are still some elements in the array.
# - int peek() Returns the next element in the array without moving the pointer.

# Example 1:
# Input: ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
#        [[[1, 2, 3]], [], [], [], [], []]
# Output: [null, 1, 2, 2, 3, false]

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# All calls to next and peek are valid.
# At most 1000 calls will be made to next, peek, and hasNext.

# Author: Kaustav Ghosh

class PeekingIterator(object):
    def __init__(self, iterator):
        self._iter = iterator
        self._peeked = False
        self._peek_val = None

    def peek(self):
        if not self._peeked:
            self._peek_val = self._iter.next()
            self._peeked = True
        return self._peek_val

    def next(self):
        if self._peeked:
            self._peeked = False
            return self._peek_val
        return self._iter.next()

    def hasNext(self):
        return self._peeked or self._iter.hasNext()
