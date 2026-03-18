# Author: Kaustav Ghosh
# Problem: 1600 - Throne Inheritance (Premium)
# Approach: N-ary tree with DFS preorder, skip dead members

from collections import defaultdict

class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.children[parentName].append(childName)

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

        def dfs(name):
            if name not in self.dead:
                order.append(name)
            for child in self.children[name]:
                dfs(child)

        dfs(self.king)
        return order
