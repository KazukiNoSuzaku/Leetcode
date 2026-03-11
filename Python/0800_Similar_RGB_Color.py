# Find the shortest hex color that is most similar to the given hex color.

# Author: Kaustav Ghosh

class Solution(object):
    def similarRGB(self, color):
        def nearest(c):
            v = int(c, 16)
            best = min(range(0, 256, 17), key=lambda x: abs(x - v))
            return '%02x' % best
        return '#' + nearest(color[1:3]) + nearest(color[3:5]) + nearest(color[5:7])
