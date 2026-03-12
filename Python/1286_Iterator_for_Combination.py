# Author: Kaustav Ghosh
# Generate all combinations upfront, iterate through them

class CombinationIterator(object):
    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        from itertools import combinations
        self.combos = [''.join(c) for c in combinations(characters, combinationLength)]
        self.index = 0

    def next(self):
        """
        :rtype: str
        """
        result = self.combos[self.index]
        self.index += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.combos)
