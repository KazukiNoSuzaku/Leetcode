# Author: Kaustav Ghosh
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/
# Premium - Track prefix/suffix digits and count trailing zeros
#
# class Solution(object):
#     def abbreviateProduct(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: str
#         """
#         # Count trailing zeros (factors of 2 and 5)
#         twos = fives = 0
#         for i in range(left, right + 1):
#             x = i
#             while x % 2 == 0:
#                 twos += 1
#                 x //= 2
#             x = i
#             while x % 5 == 0:
#                 fives += 1
#                 x //= 5
#         zeros = min(twos, fives)
#
#         # Compute full product without trailing zeros
#         product = 1
#         for i in range(left, right + 1):
#             product *= i
#         # Remove trailing zeros
#         for _ in range(zeros):
#             product //= 10
#         s = str(product)
#         if len(s) <= 10:
#             return s + 'e' + str(zeros)
#         return s[:5] + '...' + s[-5:] + 'e' + str(zeros)

class Solution(object):
    pass
