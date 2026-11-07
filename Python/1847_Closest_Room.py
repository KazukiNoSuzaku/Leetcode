# Author: Kaustav Ghosh
# Problem: Closest Room
# Approach: A query only cares which rooms are large enough, and that set only grows as the size requirement falls, so the queries are answered offline in decreasing order of requirement while rooms are admitted in decreasing order of size; each room is admitted once and never removed. Among the admitted rooms the nearest id to the preferred one is either the largest id at or below it or the smallest at or above it, so a Fenwick tree over the compressed room ids answers both by counting how many admitted ids fall at or below the preference and then descending the tree to that rank and the next. That keeps every query logarithmic rather than rescanning the admitted set, and ties in distance are broken towards the smaller id by checking the lower candidate first.

class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from bisect import bisect_right

        ids = sorted(room[0] for room in rooms)
        size = len(ids)
        tree = [0] * (size + 1)
        power = 1
        while power * 2 <= size:
            power *= 2

        def admit(rank):
            while rank <= size:
                tree[rank] += 1
                rank += rank & -rank

        def admitted_upto(rank):
            total = 0
            while rank > 0:
                total += tree[rank]
                rank -= rank & -rank
            return total

        def id_at_rank(wanted):
            # Smallest index whose admitted count reaches `wanted`.
            node = 0
            step = power
            while step:
                nxt = node + step
                if nxt <= size and tree[nxt] < wanted:
                    node = nxt
                    wanted -= tree[node]
                step >>= 1
            return ids[node]

        order = sorted(range(len(rooms)), key=lambda i: -rooms[i][1])
        asked = sorted(range(len(queries)), key=lambda j: -queries[j][1])

        answers = [-1] * len(queries)
        placed = 0
        live = 0
        for j in asked:
            preferred, minimum = queries[j]
            while placed < len(rooms) and rooms[order[placed]][1] >= minimum:
                admit(bisect_right(ids, rooms[order[placed]][0]))
                placed += 1
                live += 1
            if not live:
                continue
            below = admitted_upto(bisect_right(ids, preferred))
            best = None
            if below:
                best = id_at_rank(below)
            if below < live:
                above = id_at_rank(below + 1)
                if best is None or above - preferred < preferred - best:
                    best = above
            answers[j] = best
        return answers
