# Author: Kaustav Ghosh
# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        result = []
        depth = 0
        for c in seq:
            if c == '(':
                depth += 1
                # Assign odd depths to group 1, even depths to group 0
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1
        return result
