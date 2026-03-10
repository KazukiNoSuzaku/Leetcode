# You are given a nested list of integers nestedList. Each element is either an integer or
# a list whose elements may also be integers or other lists.
# The depth of an integer is the number of lists that it is inside of.
# Return the sum of each integer in nestedList multiplied by its depth.

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2 plus one 2 at depth 1.

# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, one 6 at depth 3: 1 + 4*2 + 6*3 = 27.

# Constraints:
# 1 <= nestedList.length <= 50
# The values of the integers in the nested list are in the range [-100, 100].
# The maximum depth of any integer is 50.

# Author: Kaustav Ghosh

class Solution(object):
    def depthSum(self, nestedList):
        def dfs(lst, depth):
            total = 0
            for item in lst:
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    total += dfs(item.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)
