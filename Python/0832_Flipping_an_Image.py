# Flip binary matrix horizontally then invert each bit.

# Author: Kaustav Ghosh

class Solution(object):
    def flipAndInvertImage(self, image):
        return [[1 - x for x in row[::-1]] for row in image]
