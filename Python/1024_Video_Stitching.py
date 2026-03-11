# Given clips and a time range [0, time], return the minimum number of clips
# needed to cover the entire range, or -1 if impossible.

# Author: Kaustav Ghosh

class Solution(object):
    def videoStitching(self, clips, time):
        clips.sort()
        res = end = farthest = 0
        i = 0
        while end < time:
            while i < len(clips) and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == end:
                return -1
            end = farthest
            res += 1
        return res
