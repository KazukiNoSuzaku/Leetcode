# Author: Kaustav Ghosh
# Binary search on per-index snapshot history

import bisect

class SnapshotArray(object):
    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.history = [[[0, 0]] for _ in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.history[index][-1][0] == self.snap_id:
            self.history[index][-1][1] = val
        else:
            self.history[index].append([self.snap_id, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        hist = self.history[index]
        i = bisect.bisect_right(hist, [snap_id, float('inf')]) - 1
        return hist[i][1]
