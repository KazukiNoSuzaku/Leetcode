# Author: Kaustav Ghosh
# https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

# Premium Problem
# Binary search on the target water level.
# Water poured out from buckets above target loses (1-loss)% when received.
# Find the level where total poured in equals total received.
#
# class Solution(object):
#     def equalizeWater(self, buckets, loss):
#         """
#         :type buckets: List[int]
#         :type loss: int
#         :rtype: float
#         """
#         lo, hi = 0.0, max(buckets)
#         percent_kept = (100 - loss) / 100.0
#         for _ in range(100):
#             mid = (lo + hi) / 2.0
#             excess = 0.0
#             deficit = 0.0
#             for b in buckets:
#                 if b > mid:
#                     excess += (b - mid) * percent_kept
#                 else:
#                     deficit += mid - b
#             if excess >= deficit:
#                 lo = mid
#             else:
#                 hi = mid
#         return lo

class Solution(object):
    pass
