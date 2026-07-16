# Author: Kaustav Ghosh
# Problem: Design Most Recently Used Queue (Premium)
# Approach: Keep the order in a list; fetch pops the kth element and re-appends it. O(n) per call, which the small constraints comfortably allow

class MRUQueue(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.queue = list(range(1, n + 1))

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        value = self.queue.pop(k - 1)  # k is 1-indexed
        self.queue.append(value)
        return value
