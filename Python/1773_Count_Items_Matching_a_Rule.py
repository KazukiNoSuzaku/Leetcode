# Author: Kaustav Ghosh
# Problem: Count Items Matching a Rule
# Approach: Map the rule key to its column index and count items whose value in that column matches

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        column = {'type': 0, 'color': 1, 'name': 2}[ruleKey]
        return sum(1 for item in items if item[column] == ruleValue)
