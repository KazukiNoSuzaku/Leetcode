# Return the transpose of a matrix.

# Author: Kaustav Ghosh

class Solution(object):
    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]
