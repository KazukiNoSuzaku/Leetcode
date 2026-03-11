# A web developer needs to know how to design a web page's size.
# So, given a specific rectangular web page's area, your job by now is to design a rectangular
# web page, whose length L and width W satisfy: L * W = area, L >= W >= 1, L - W is minimized.
# Return [L, W].

# Author: Kaustav Ghosh

import math

class Solution(object):
    def constructRectangle(self, area):
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]
