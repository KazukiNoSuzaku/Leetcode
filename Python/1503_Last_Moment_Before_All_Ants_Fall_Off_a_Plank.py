# Ants walk left or right on a plank of length n. When they collide they reverse.
# This is equivalent to ants passing through each other.
# Return the last moment before all ants fall off.

# Author: Kaustav Ghosh

class Solution(object):
    def getLastMoment(self, n, left, right):
        return max(
            max(left) if left else 0,
            max(n - x for x in right) if right else 0
        )
