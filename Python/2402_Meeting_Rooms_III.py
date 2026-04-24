import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available = list(range(n))   # min-heap of free room indices
        occupied = []                # min-heap of (end_time, room)
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that have ended
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                # Delay to earliest ending room
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (end_time + (end - start), room))

            count[room] += 1

        return count.index(max(count))
