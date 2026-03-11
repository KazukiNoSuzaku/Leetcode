# A query matches a pattern if you can insert lowercase letters into pattern to get query.

# Author: Kaustav Ghosh

class Solution(object):
    def camelMatch(self, queries, pattern):
        def match(query, pattern):
            j = 0
            for c in query:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    return False
            return j == len(pattern)
        return [match(q, pattern) for q in queries]
