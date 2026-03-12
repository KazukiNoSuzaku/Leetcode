# Author: Kaustav Ghosh
# 1096. Brace Expansion II
# https://leetcode.com/problems/brace-expansion-ii/

class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def parse(s, i):
            groups = [[]]
            while i < len(s) and s[i] != '}':
                if s[i] == '{':
                    words, i = parse(s, i + 1)
                    i += 1  # skip '}'
                    groups[-1] = [a + b for a in groups[-1] for b in words] if groups[-1] else words
                elif s[i] == ',':
                    groups.append([])
                    i += 1
                else:
                    j = i
                    while j < len(s) and s[j].isalpha():
                        j += 1
                    word = s[i:j]
                    groups[-1] = [a + word for a in groups[-1]] if groups[-1] else [word]
                    i = j
            result = set()
            for g in groups:
                result.update(g)
            return sorted(result), i

        result, _ = parse(expression, 0)
        return result
