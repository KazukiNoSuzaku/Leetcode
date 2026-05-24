import heapq

class Solution:
    def minimumCost(self, start: list[int], target: list[int], specialRoads: list[list[int]]) -> int:
        def taxi(x1, y1, x2, y2):
            return abs(x2 - x1) + abs(y2 - y1)

        sx, sy = start
        tx, ty = target

        heap = [(0, sx, sy)]
        visited = set()

        while heap:
            cost, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == tx and y == ty:
                return cost

            heapq.heappush(heap, (cost + taxi(x, y, tx, ty), tx, ty))

            for x1, y1, x2, y2, c in specialRoads:
                if (x2, y2) not in visited:
                    heapq.heappush(heap, (cost + taxi(x, y, x1, y1) + c, x2, y2))

        return taxi(sx, sy, tx, ty)
