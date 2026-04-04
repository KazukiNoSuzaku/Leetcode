# Author: Kaustav Ghosh

# Premium Problem
# Given an array nums of positive integers, count triplets (i, j, k) where i < j < k
# such that exactly one of nums[i], nums[j], nums[k] divides nums[i]+nums[j]+nums[k].
#
# Approach: Count frequency of each value, then for each triplet of values (a, b, c),
# check divisibility of a+b+c by each of a, b, c. Multiply by frequency combinations.

class Solution(object):
    pass
