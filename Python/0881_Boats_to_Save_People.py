# Minimum boats needed; each boat carries at most 2 people with total weight <= limit.

# Author: Kaustav Ghosh

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit: lo += 1
            hi -= 1
            boats += 1
        return boats
