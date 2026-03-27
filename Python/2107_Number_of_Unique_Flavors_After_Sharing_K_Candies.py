# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/
# Premium - Sliding window with Counter
#
# class Solution(object):
#     def shareCandies(self, candies, k):
#         """
#         :type candies: List[int]
#         :type k: int
#         :rtype: int
#         """
#         from collections import Counter
#         count = Counter(candies)
#         if k == 0:
#             return len(count)
#         # Remove first k elements from our pool
#         for i in range(k):
#             count[candies[i]] -= 1
#             if count[candies[i]] == 0:
#                 del count[candies[i]]
#         best = len(count)
#         for i in range(k, len(candies)):
#             count[candies[i]] -= 1
#             if count[candies[i]] == 0:
#                 del count[candies[i]]
#             count[candies[i - k]] += 1
#             best = max(best, len(count))
#         return best

class Solution(object):
    pass
