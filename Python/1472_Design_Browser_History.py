# Author: Kaustav Ghosh
# Problem: Design Browser History
# Approach: List with current index pointer

class Solution(object):
    pass

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
