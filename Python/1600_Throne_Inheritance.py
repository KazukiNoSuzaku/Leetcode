# Author: Kaustav Ghosh
# Problem: Throne Inheritance
# Approach: The succession order is precisely a pre-order walk of the family tree, visiting each person before their children in birth order, so the structure to keep is just a children list per parent plus a set of the dead. Births and deaths are then constant time and all the work happens when the order is requested. The walk is done with an explicit stack rather than recursion, because a family that is one long line of single children would be as deep as the number of people and would overflow the call stack; pushing children in reverse keeps the eldest on top so they come out first.

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
            stack.extend(reversed(self.children[name]))
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
