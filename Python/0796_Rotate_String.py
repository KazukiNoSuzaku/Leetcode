# Check if s can become goal by rotating.

# Author: Kaustav Ghosh

class Solution(object):
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in s + s
