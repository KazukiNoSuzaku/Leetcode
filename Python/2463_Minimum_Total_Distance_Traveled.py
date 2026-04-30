class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        # Expand each factory into individual unit slots
        slots = []
        for pos, lim in factory:
            slots.extend([pos] * lim)

        m, n = len(robot), len(slots)
        INF = float('inf')
        # dp[j] = min cost to assign first i robots using first j slots (rolling)
        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [INF] * (n + 1)
            for j in range(i, n + 1):
                # Either skip slot j (don't assign robot i to it)
                # or assign robot i to slot j (order-preserving since both sorted)
                skip = curr[j - 1]
                assign = (prev[j - 1] if prev[j - 1] < INF else INF) + abs(robot[i - 1] - slots[j - 1])
                curr[j] = min(skip, assign)
            prev = curr

        return prev[n]
