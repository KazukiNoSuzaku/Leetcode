# Simulate pouring water droplets onto terrain; return final heights.

# Author: Kaustav Ghosh

class Solution(object):
    def pourWater(self, heights, volume, k):
        for _ in range(volume):
            pos = k
            while pos > 0 and heights[pos-1] <= heights[pos]:
                pos -= 1
            while pos < len(heights)-1 and heights[pos+1] <= heights[pos]:
                pos += 1
            while pos > k and heights[pos-1] <= heights[pos]:
                pos -= 1
            heights[pos] += 1
        return heights
