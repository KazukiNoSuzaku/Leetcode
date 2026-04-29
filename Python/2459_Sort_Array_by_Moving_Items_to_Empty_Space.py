class Solution:
    def sortArray(self, nums: list[int]) -> int:
        # Premium: 0 is the empty space; swap any element into 0's position.
        # Two valid sorted targets: [0,1,...,n-1] or [1,...,n-1,0].
        # For each target, decompose into permutation cycles.
        # Cycle containing 0: (len - 1) moves. Cycle without 0: (len + 1) moves.
        n = len(nums)
        pos = {v: i for i, v in enumerate(nums)}

        def count_moves(target):
            visited = [False] * n
            moves = 0
            for start in range(n):
                if visited[start]:
                    continue
                cycle = []
                cur = start
                while not visited[cur]:
                    visited[cur] = True
                    cycle.append(target[cur])
                    cur = pos[target[cur]]
                if len(cycle) <= 1:
                    continue
                moves += (len(cycle) - 1) if 0 in cycle else (len(cycle) + 1)
            return moves

        target1 = list(range(n))
        target2 = list(range(1, n)) + [0]
        return min(count_moves(target1), count_moves(target2))
