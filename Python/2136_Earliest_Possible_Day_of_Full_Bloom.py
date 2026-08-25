# Author: Kaustav Ghosh
# Problem: Earliest Possible Day of Full Bloom
# Approach: Planting is sequential, so the total planting time is fixed; only the growing overlaps. Planting the seeds with the longest grow time first lets their growth run while later seeds are still being planted. Track cumulative planting time and maximize plant-completion + grow

class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        seeds = sorted(zip(plantTime, growTime), key=lambda s: -s[1])
        planted = 0
        answer = 0
        for plant, grow in seeds:
            planted += plant
            answer = max(answer, planted + grow)
        return answer
