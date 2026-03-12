# Author: Kaustav Ghosh
# Group by size greedily, emit group when full

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        groups = defaultdict(list)
        result = []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []
        return result
