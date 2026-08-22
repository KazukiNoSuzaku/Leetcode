# Author: Kaustav Ghosh
# Problem: Find All People With Secret
# Approach: Process meetings grouped by timestamp. Within a timestamp, union all meeting pairs; anyone whose component contains a current secret-holder learns it. People in the group who are not connected to a knower keep their state, so reset the union-find for those group members before moving to the next timestamp

from collections import defaultdict

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        knows = [False] * n
        knows[0] = True
        knows[firstPerson] = True

        by_time = defaultdict(list)
        for x, y, t in meetings:
            by_time[t].append((x, y))

        for t in sorted(by_time):
            people = set()
            for x, y in by_time[t]:
                union(x, y)
                people.add(x)
                people.add(y)
            # a component knows if any member currently knows
            root_knows = {}
            for p in people:
                if knows[p]:
                    root_knows[find(p)] = True
            for p in people:
                if root_knows.get(find(p)):
                    knows[p] = True
            for p in people:
                parent[p] = p

        return [i for i in range(n) if knows[i]]
