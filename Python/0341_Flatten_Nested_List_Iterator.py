# You are given a nested list of integers nestedList. Each element is either an integer or a
# list whose elements may also be integers or other lists. Implement an iterator to flatten it.
# Implement the NestedIterator class:
# - NestedIterator(List[NestedInteger] nestedList) initializes the iterator with the nested list.
# - int next() returns the next integer in the nested list.
# - boolean hasNext() returns true if there are still some integers in the nested list.

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]

# Constraints:
# 1 <= nestedList.length <= 500

# Author: Kaustav Ghosh

class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self._flatten(nestedList)

    def _flatten(self, lst):
        for item in reversed(lst):
            self.stack.append(item)

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self._flatten(top.getList())
        return False
