# You are given a nested list of integers nestedList. Each element is either an integer
# or a list whose elements may also be integers or other lists.
# The depth of an integer is the number of lists that it is inside of.
# For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.
# Let maxDepth be the maximum depth of any integer.
# The weight of an integer is maxDepth + 1 - (the depth of the integer).
# Return the sum of each integer in nestedList multiplied by its weight.

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 8
# Explanation: Four 1's with weight 1, one 2 with weight 2.

# Constraints:
# 1 <= nestedList.length <= 50

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def depthSumInverse(self, nestedList):
        # BFS level by level; accumulate unweighted sum and add to total each level
        queue = deque(nestedList)
        total = 0
        level_sum = 0
        while queue:
            for _ in range(len(queue)):
                item = queue.popleft()
                if item.isInteger():
                    level_sum += item.getInteger()
                else:
                    queue.extend(item.getList())
            total += level_sum
        return total
