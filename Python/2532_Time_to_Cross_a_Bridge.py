import heapq

class Solution:
    def findCrossingTime(self, n: int, k: int, time: list[list[int]]) -> int:
        # 4-heap simulation; right→left has priority; within each side highest (L+R) worker crosses first.
        eff = [time[i][0] + time[i][2] for i in range(k)]
        wl = [(-eff[i], -i) for i in range(k)]  # left_wait max-heap
        heapq.heapify(wl)
        wr = []       # right_wait max-heap
        workr = []    # (finish_time, -eff, -idx): picking up box on right
        workl = []    # (finish_time, -eff, -idx): putting down box on left

        t = 0
        while n > 0 or wr or workr:
            while workl and workl[0][0] <= t:
                _, ne, ni = heapq.heappop(workl)
                heapq.heappush(wl, (ne, ni))
            while workr and workr[0][0] <= t:
                _, ne, ni = heapq.heappop(workr)
                heapq.heappush(wr, (ne, ni))

            if wr:
                ne, ni = heapq.heappop(wr)
                i = -ni
                t += time[i][2]
                heapq.heappush(workl, (t + time[i][3], ne, ni))
            elif wl and n > 0:
                ne, ni = heapq.heappop(wl)
                i = -ni
                t += time[i][0]
                n -= 1
                heapq.heappush(workr, (t + time[i][1], ne, ni))
            else:
                nxt = workr[0][0] if workr else float('inf')
                if workl and n > 0:
                    nxt = min(nxt, workl[0][0])
                t = nxt

        return t
