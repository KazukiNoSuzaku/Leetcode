# Given a stream of integers and a window size, calculate the moving average of all integers
# in the sliding window.
# Implement the MovingAverage class:
# - MovingAverage(int size) Initializes the object with the size of the window size.
# - double next(int val) Returns the moving average of the last size values of the stream.

# Example 1:
# Input: ["MovingAverage","next","next","next","next"]
#        [[3],[1],[10],[3],[5]]
# Output: [null,1.0,5.5,4.666...,6.0]

# Constraints:
# 1 <= size <= 1000
# -10^5 <= val <= 10^5

# Author: Kaustav Ghosh

from collections import deque

class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val):
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return self.total / float(len(self.queue))
