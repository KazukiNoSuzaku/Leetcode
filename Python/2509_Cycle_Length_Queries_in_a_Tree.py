# Author: Kaustav Ghosh
# Problem: Cycle Length Queries in a Tree
# Approach: In this tree a node's parent is simply its label halved, so the cycle created by joining two nodes runs up both sides to their lowest common ancestor. Repeatedly halve whichever label is larger, counting steps, until the two meet; the cycle is that many edges plus the added one

class Solution(object):
    def cycleLengthQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        for a, b in queries:
            length = 1
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                length += 1
            answer.append(length)
        return answer
