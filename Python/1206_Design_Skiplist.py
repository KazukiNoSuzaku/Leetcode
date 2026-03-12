# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Skiplist with multiple levels for O(log n) operations

import random

class Node(object):
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist(object):
    def __init__(self):
        self.head = Node()

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        node = self.head
        while node:
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            node = node.down
        return False

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        nodes = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            node = node.down

        insert = True
        down = None
        while insert and nodes:
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = random.random() < 0.5

        if insert:
            self.head = Node(-1, None, self.head)

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        found = False
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                node.right = node.right.right
                found = True
            node = node.down
        return found
