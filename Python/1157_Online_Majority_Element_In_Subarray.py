# Author: Kaustav Ghosh
# Boyer-Moore voting + binary search on stored indices per element

import bisect
import random
from collections import defaultdict

class MajorityChecker(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr = arr
        self.indices = defaultdict(list)
        for i, v in enumerate(arr):
            self.indices[v].append(i)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        # Random sampling: if majority exists, random pick has >50% chance
        for _ in range(20):
            idx = random.randint(left, right)
            candidate = self.arr[idx]
            lo = bisect.bisect_left(self.indices[candidate], left)
            hi = bisect.bisect_right(self.indices[candidate], right)
            if hi - lo >= threshold:
                return candidate
        return -1
