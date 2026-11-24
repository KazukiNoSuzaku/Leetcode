# Author: Kaustav Ghosh
# Problem: Average Height of Buildings in Each Segment
# Approach: Between two consecutive coordinates where some building starts or ends, the set of buildings covering the street never changes, so the average is constant across that whole stretch. Recording each building as a pair of changes, adding its height and one to the count at its start and removing both at its end, lets one sweep over the sorted coordinates carry the running height total and building count and emit the average for each stretch that is covered at all. Adjacent stretches are folded together only when they share a boundary and report the same average, which keeps the segment count minimal while refusing to bridge a gap where no building stands.

class Solution(object):
    def averageHeightOfBuildings(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        height_change = defaultdict(int)
        count_change = defaultdict(int)
        for start, end, height in buildings:
            height_change[start] += height
            count_change[start] += 1
            height_change[end] -= height
            count_change[end] -= 1

        street = []
        total_height = 0
        covered = 0
        previous = None
        for point in sorted(height_change):
            if covered > 0:
                average = total_height // covered
                if street and street[-1][1] == previous and street[-1][2] == average:
                    street[-1][1] = point
                else:
                    street.append([previous, point, average])
            total_height += height_change[point]
            covered += count_change[point]
            previous = point
        return street
