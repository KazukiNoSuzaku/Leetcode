# Author: Kaustav Ghosh
# Problem 2069: Walking Robot Simulation II

class Robot(object):
    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4
        self.pos = 0  # position along perimeter
        self.moved = False

    def _get_coords_and_dir(self):
        p = self.pos
        w, h = self.width, self.height
        if p < w:
            return (p, 0, "East" if (p > 0 or not self.moved) else "South")
        p -= w - 1
        if p < h:
            return (w - 1, p, "North" if p > 0 else "East")
        p -= h - 1
        if p < w:
            return (w - 1 - p, h - 1, "West" if p > 0 else "North")
        p -= w - 1
        return (0, h - 1 - p, "South" if p > 0 else "West")

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self):
        """
        :rtype: List[int]
        """
        x, y, _ = self._get_coords_and_dir()
        return [x, y]

    def getDir(self):
        """
        :rtype: str
        """
        _, _, d = self._get_coords_and_dir()
        return d
