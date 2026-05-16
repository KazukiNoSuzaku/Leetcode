class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        # running[i] = True if second i is already scheduled to run
        max_end = tasks[-1][1]
        running = [False] * (max_end + 1)

        for start, end, duration in tasks:
            # Count already-scheduled seconds within [start, end]
            already = sum(running[start:end + 1])
            need = duration - already
            # Greedily fill from the right end of [start, end]
            i = end
            while need > 0:
                if not running[i]:
                    running[i] = True
                    need -= 1
                i -= 1

        return sum(running)
