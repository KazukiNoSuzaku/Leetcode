# Author: Kaustav Ghosh
# Problem: Count Items Matching a Rule
# Approach: The rule key only selects which of the three fields to compare, so resolving it once to a column index turns the whole question into counting the items whose chosen field equals the rule value. One generator expression over the items then does the work in a single pass.

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        column = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(item[column] == ruleValue for item in items)
