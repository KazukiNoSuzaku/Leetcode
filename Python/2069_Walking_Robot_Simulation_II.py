# Author: Kaustav Ghosh
# Problem: Walking Robot Simulation II
# Approach: The robot only travels the boundary, a cycle of length 2*(width-1)+2*(height-1). Precompute the cell and facing direction for each step index around the loop (the direction is the edge along which the cell is reached). Moves just advance a position modulo the perimeter; the origin faces East initially and South after any full loop

class Robot(object):
    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w = width
        self.h = height
        self.per = 2 * (width - 1) + 2 * (height - 1)
        self.pos = 0
        self.moved = False

        cells = [(0, 0)]
        dirs = ['East']
        for x in range(1, width):
            cells.append((x, 0)); dirs.append('East')
        for y in range(1, height):
            cells.append((width - 1, y)); dirs.append('North')
        for x in range(width - 2, -1, -1):
            cells.append((x, height - 1)); dirs.append('West')
        for y in range(height - 2, 0, -1):
            cells.append((0, y)); dirs.append('South')
        self.cells = cells
        self.dirs = dirs

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.moved = True
        self.pos = (self.pos + num) % self.per

    def getPos(self):
        """
        :rtype: List[int]
        """
        return list(self.cells[self.pos])

    def getDir(self):
        """
        :rtype: str
        """
        if self.pos == 0:
            return 'South' if self.moved else 'East'
        return self.dirs[self.pos]
