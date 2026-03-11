# You are given an array of people where people[i] = [hi, ki] represents the ith person
# of height hi with exactly ki other people in front who have height >= hi.
# Reconstruct and return the queue that is represented by the input array people.

# Author: Kaustav Ghosh

class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
