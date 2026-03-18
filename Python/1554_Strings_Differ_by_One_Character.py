# Author: Kaustav Ghosh
# Problem: 1554 - Strings Differ by One Character (Premium)
# Approach: Hash each string with wildcard at each position to detect collisions

class Solution(object):
    def differByOne(self, dict):
        """
        :type dict: List[str]
        :rtype: bool
        """
        if not dict:
            return False
        m = len(dict[0])
        for j in range(m):
            seen = set()
            for word in dict:
                masked = word[:j] + '*' + word[j+1:]
                if masked in seen:
                    return True
                seen.add(masked)
        return False
