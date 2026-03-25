# Author: Kaustav Ghosh
# Problem 2092: Find All People With Secret

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        # Union-Find with reset
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # Person 0 and firstPerson share secret at time 0
        union(0, firstPerson)

        # Group meetings by time
        meetings.sort(key=lambda x: x[2])
        i = 0
        while i < len(meetings):
            j = i
            # Collect all meetings at the same time
            while j < len(meetings) and meetings[j][2] == meetings[i][2]:
                j += 1
            # Union all people in meetings at this time
            people_in_group = set()
            for k in range(i, j):
                union(meetings[k][0], meetings[k][1])
                people_in_group.add(meetings[k][0])
                people_in_group.add(meetings[k][1])
            # Reset people who don't know the secret
            for p in people_in_group:
                if find(p) != find(0):
                    parent[p] = p
                    rank[p] = 0
            i = j

        return [i for i in range(n) if find(i) == find(0)]
