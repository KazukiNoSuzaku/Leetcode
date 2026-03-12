# Author: Kaustav Ghosh
# 1104. Path In Zigzag Labelled Binary Tree
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        result = []
        while label >= 1:
            result.append(label)
            # Find level of label
            level = label.bit_length() - 1
            # Mirror the label in its level
            level_min = 1 << level
            level_max = (1 << (level + 1)) - 1
            label = (level_min + level_max - label) // 2
        return result[::-1]
