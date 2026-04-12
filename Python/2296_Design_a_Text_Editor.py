# Author: Kaustav Ghosh
# Problem: 2296. Design a Text Editor
# URL: https://leetcode.com/problems/design-a-text-editor/
# Difficulty: Hard

class TextEditor(object):

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        for c in text:
            self.left.append(c)

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        deleted = min(k, len(self.left))
        for _ in range(deleted):
            self.left.pop()
        return deleted

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        moves = min(k, len(self.left))
        for _ in range(moves):
            self.right.append(self.left.pop())
        return ''.join(self.left[-10:])

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        moves = min(k, len(self.right))
        for _ in range(moves):
            self.left.append(self.right.pop())
        return ''.join(self.left[-10:])
