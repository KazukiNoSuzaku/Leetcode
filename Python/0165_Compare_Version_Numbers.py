# Given two version strings, version1 and version2, compare them.
# A version string consists of revisions separated by dots '.'.
# The value of the revision is its integer value ignoring leading zeros.
# Compare revisions left to right. Return -1 if version1 < version2,
# 1 if version1 > version2, or 0 if they are equal.

# Example 1:
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1

# Example 2:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0

# Example 3:
# Input: version1 = "1.0", version2 = "1.0.0.0"
# Output: 0

# Constraints:
# 1 <= version1.length, version2.length <= 500

# Author: Kaustav Ghosh

class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n = max(len(v1), len(v2))
        for i in range(n):
            r1 = v1[i] if i < len(v1) else 0
            r2 = v2[i] if i < len(v2) else 0
            if r1 < r2:
                return -1
            if r1 > r2:
                return 1
        return 0
