# Author: Kaustav Ghosh
# Problem: Design a Text Editor
# Approach: Keep the text on two stacks split at the cursor: `left` holds characters before the cursor and `right` holds characters after it (top = nearest to cursor). Adding pushes onto left, deleting pops left, and moving the cursor transfers characters between the stacks. Each query returns the last up-to-10 characters left of the cursor

class TextEditor(object):
    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        self.left.extend(text)

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        d = min(k, len(self.left))
        for _ in range(d):
            self.left.pop()
        return d

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        m = min(k, len(self.left))
        for _ in range(m):
            self.right.append(self.left.pop())
        return "".join(self.left[-10:])

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        m = min(k, len(self.right))
        for _ in range(m):
            self.left.append(self.right.pop())
        return "".join(self.left[-10:])
