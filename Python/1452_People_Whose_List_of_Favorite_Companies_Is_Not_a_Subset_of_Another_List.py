# Author: Kaustav Ghosh
# Problem: People Whose List of Favorite Companies Is Not a Subset of Another List
# Approach: Convert to sets, check if any set is a subset of another

class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        sets = [set(companies) for companies in favoriteCompanies]
        result = []
        for i in range(len(sets)):
            is_subset = False
            for j in range(len(sets)):
                if i != j and sets[i] <= sets[j]:
                    is_subset = True
                    break
            if not is_subset:
                result.append(i)
        return result
