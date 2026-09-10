# Author: Kaustav Ghosh
# Problem: Naming a Company
# Approach: Group ideas by their first letter, storing suffixes (everything after the first character). Swapping first letters of ideas from groups a and b yields two valid names only when neither swapped name already exists, i.e. the suffix is unique to its group. For each pair of groups, the count is (suffixes only in a) times (suffixes only in b), and each such unordered pair yields two ordered company names

class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        groups = {}
        for idea in ideas:
            groups.setdefault(idea[0], set()).add(idea[1:])

        letters = list(groups.keys())
        total = 0
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                a, b = groups[letters[i]], groups[letters[j]]
                common = len(a & b)
                total += (len(a) - common) * (len(b) - common)
        return total * 2
