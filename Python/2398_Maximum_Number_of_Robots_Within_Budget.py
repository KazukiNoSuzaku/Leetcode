from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        dq = deque()  # monotonic decreasing deque of indices for max chargeTimes
        window_sum = 0
        left = 0
        ans = 0
        for right, (ct, rc) in enumerate(zip(chargeTimes, runningCosts)):
            while dq and chargeTimes[dq[-1]] <= ct:
                dq.pop()
            dq.append(right)
            window_sum += rc
            k = right - left + 1
            while dq and chargeTimes[dq[0]] + k * window_sum > budget:
                if dq[0] == left:
                    dq.popleft()
                window_sum -= runningCosts[left]
                left += 1
                k -= 1
            ans = max(ans, right - left + 1)
        return ans
