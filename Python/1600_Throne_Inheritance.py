# Author: Kaustav Ghosh
# Problem: Throne Inheritance
# Approach: Keep a children map and a dead set; the succession order is a pre-order DFS from the king, skipping the deceased

class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.king = kingName
        self.children = {kingName: []}
        self.dead = set()

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.children[parentName].append(childName)
        self.children[childName] = []

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.dead.add(name)

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        order = []
        stack = [self.king]
        while stack:
            name = stack.pop()
            if name not in self.dead:
                order.append(name)
            # Push children in reverse so the eldest is processed first
            stack.extend(reversed(self.children[name]))
        return order
