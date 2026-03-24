# Author: Kaustav Ghosh
# Problem 1993: Operations on Tree

class LockingTree(object):
    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        self.children = [[] for _ in range(len(parent))]
        self.locked = [0] * len(parent)  # 0 means unlocked, else user id
        for i in range(1, len(parent)):
            self.children[parent[i]].append(i)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] != 0:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] != user:
            return False
        self.locked[num] = 0
        return True

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        # Check node is unlocked
        if self.locked[num] != 0:
            return False
        # Check no locked ancestors
        curr = self.parent[num]
        while curr != -1:
            if self.locked[curr] != 0:
                return False
            curr = self.parent[curr]
        # Check at least one locked descendant and unlock all
        if not self._unlockDescendants(num):
            return False
        self.locked[num] = user
        return True

    def _unlockDescendants(self, num):
        found = False
        stack = list(self.children[num])
        while stack:
            node = stack.pop()
            if self.locked[node] != 0:
                self.locked[node] = 0
                found = True
            stack.extend(self.children[node])
        return found
