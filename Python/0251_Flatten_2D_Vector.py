# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
# Implement the Vector2D class:
# - Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# - int next() returns the next element from the 2D vector and moves the pointer one step forward.
# - boolean hasNext() returns true if there are still some elements in the vector.

# Example 1:
# Input: ["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]
#        [[[[1,2],[3],[4]]],[],[],[],[],[],[],[]]
# Output: [null,1,2,3,true,true,4,false]

# Constraints:
# 0 <= vec.length <= 200
# 0 <= vec[i].length <= 500

# Author: Kaustav Ghosh

class Vector2D(object):
    def __init__(self, vec):
        self.data = []
        for row in vec:
            self.data.extend(row)
        self.idx = 0

    def next(self):
        val = self.data[self.idx]
        self.idx += 1
        return val

    def hasNext(self):
        return self.idx < len(self.data)
