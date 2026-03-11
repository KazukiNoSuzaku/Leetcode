# Given a list of equations like "a==b" or "a!=b", return whether they are satisfiable.

# Author: Kaustav Ghosh

class Solution(object):
    def equationsPossible(self, equations):
        parent = list(range(26))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parent[find(x)] = find(y)
        for eq in equations:
            if eq[1] == '=':
                union(ord(eq[0]) - 97, ord(eq[3]) - 97)
        for eq in equations:
            if eq[1] == '!':
                if find(ord(eq[0]) - 97) == find(ord(eq[3]) - 97):
                    return False
        return True
