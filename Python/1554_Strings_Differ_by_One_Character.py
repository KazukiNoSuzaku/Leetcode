# Author: Kaustav Ghosh
# Problem: Strings Differ by One Character (Premium)
# Approach: For each column, mask that position with a wildcard; two words sharing a masked form differ only at that single column

class Solution(object):
    def differByOne(self, dict):
        """
        :type dict: List[str]
        :rtype: bool
        """
        m = len(dict[0])
        for i in range(m):
            seen = set()
            for word in dict:
                masked = word[:i] + '*' + word[i + 1:]
                if masked in seen:
                    return True
                seen.add(masked)
        return False
