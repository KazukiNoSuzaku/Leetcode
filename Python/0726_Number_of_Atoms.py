# Parse a chemical formula and return the count of each element.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def countOfAtoms(self, formula):
        i = [0]
        def parse():
            counts = Counter()
            while i[0] < len(formula) and formula[i[0]] != ')':
                if formula[i[0]] == '(':
                    i[0] += 1
                    inner = parse()
                    i[0] += 1
                    num = 0
                    while i[0] < len(formula) and formula[i[0]].isdigit():
                        num = num * 10 + int(formula[i[0]]); i[0] += 1
                    for k in inner: counts[k] += inner[k] * (num or 1)
                elif formula[i[0]].isupper():
                    j = i[0] + 1
                    while j < len(formula) and formula[j].islower(): j += 1
                    elem = formula[i[0]:j]; i[0] = j
                    num = 0
                    while i[0] < len(formula) and formula[i[0]].isdigit():
                        num = num * 10 + int(formula[i[0]]); i[0] += 1
                    counts[elem] += num or 1
            return counts
        counts = parse()
        return ''.join(e + (str(counts[e]) if counts[e] > 1 else '') for e in sorted(counts))
