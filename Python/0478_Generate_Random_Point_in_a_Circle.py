# Given the radius and the position of the center of a circle, implement the function
# randPoint which generates a uniform random point inside the circle (including the boundary).

# Author: Kaustav Ghosh

import random
import math

class Solution(object):
    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        theta = random.uniform(0, 2 * math.pi)
        r = self.r * math.sqrt(random.uniform(0, 1))
        return [self.x + r * math.cos(theta), self.y + r * math.sin(theta)]
