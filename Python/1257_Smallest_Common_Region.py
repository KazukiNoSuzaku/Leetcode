# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Build parent map, find LCA of two regions

class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        parent = {}
        for region in regions:
            for i in range(1, len(region)):
                parent[region[i]] = region[0]

        ancestors = set()
        r = region1
        while r:
            ancestors.add(r)
            r = parent.get(r)

        r = region2
        while r:
            if r in ancestors:
                return r
            r = parent.get(r)
        return ""
